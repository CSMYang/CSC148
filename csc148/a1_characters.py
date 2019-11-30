"""
This class describes the behavior of a character and sets the characters stats
for a player to use.
"""
from typing import List
from a1_battle_queue import BattleQueue
from a1_playstyle import Playstyle


class Characters:
    """ A class representing a character of this game."""

    def __init__(self, character_name: str, battle_queue: BattleQueue,
                 playstyle: Playstyle) -> None:
        """ Initialize a character with character_name.

        >>> bq = BattleQueue()
        >>> from a1_playstyle import AutomatedPlaystyle
        >>> auto = AutomatedPlaystyle()
        >>> p1 = Characters('Alex', bq, auto)
        """
        self._character_name = character_name
        self.hp = 100
        self._sp = 100
        self.playstyle = playstyle
        self.battle_queue = battle_queue
        self.enemy = None

    def __repr__(self) -> str:
        """ Returns the representation of a character."""
        raise NotImplementedError

    def get_hp(self) -> int:
        """ Returns the current health point of a character."""
        return self.hp

    def get_sp(self) -> int:
        """ Return the current skill point of a character."""
        return self._sp

    def get_name(self) -> str:
        """ Return the name of the character."""
        return self._character_name

    def attack(self) -> None:
        """ This function is called when an attack is performed by a
        character.
        """
        raise NotImplementedError

    def is_valid_action(self, action: str) -> bool:
        """ Return true iff the action provided is an valid action."""
        raise NotImplementedError

    def special_attack(self) -> None:
        """ This function is called when a special attack is performed
        by a character.
        """
        raise NotImplementedError

    def get_available_actions(self) -> List:
        """ Return a list of available actions based on current sp."""
        raise NotImplementedError

    def get_next_sprite(self) -> str:
        """ Return the name of next sprite to be drawn to a character."""
        raise NotImplementedError


class Mage(Characters):
    """ A class representing a Mage."""

    def __init__(self, character_name: str, battle_queue: BattleQueue,
                 playstyle: Playstyle) -> None:
        """ Initialize a mage character, which initially has 100 hp ,100 sp
        and 8 defense.

        >>> bq = BattleQueue()
        >>> from a1_playstyle import AutomatedPlaystyle
        >>> auto = AutomatedPlaystyle()
        >>> p1 = Mage('Alex', bq, auto)
        >>> p1
        Alex (Mage): 100/100
        """
        super().__init__(character_name, battle_queue, playstyle)
        self.defense = 8
        self.next_sprite = 'mage_idle_0'

    def attack(self) -> None:
        """ This function is called when performing an attack which deals 20
         damage and consumes 5 skill point, and adds self into battle queue.

        >>> bq = BattleQueue()
        >>> from a1_playstyle import AutomatedPlaystyle
        >>> auto = AutomatedPlaystyle()
        >>> p1 = Mage('Alex', bq, auto)
        >>> p2 = Mage('Bob', bq, auto)
        >>> p1.enemy = p2
        >>> p1.attack()
        >>> p1
        Alex (Mage): 100/95
        >>> p2
        Bob(Mage): 88/100
        """
        self._sp -= 5
        self.enemy.hp = max(0, self.enemy.hp - (20 - self.enemy.defense))
        self.battle_queue.add(self)
        self.next_sprite = 'mage_attack_0'

    def get_available_actions(self) -> List[str]:
        """ Return a list of available actions based on current sp.

        >>> bq = BattleQueue()
        >>> from a1_playstyle import AutomatedPlaystyle
        >>> auto = AutomatedPlaystyle()
        >>> p1 = Mage('Alex', bq, auto)
        >>> p1.get_available_actions()
        ['A', 'S']
        """
        list_of_actions = []
        if self.is_valid_action('A'):
            list_of_actions.append('A')
        if self.is_valid_action('S'):
            list_of_actions.append('S')
        return list_of_actions

    def special_attack(self) -> None:
        """ This function is called when performing a special attack, which
        deals 40 damage and consumes 30 skill point and adds enemy into the
        battle queue before adding self into battle queue.

        >>> bq = BattleQueue()
        >>> from a1_playstyle import AutomatedPlaystyle
        >>> auto = AutomatedPlaystyle()
        >>> p1 = Mage('Alex', bq, auto)
        >>> p2 = Mage('Bob', bq, auto)
        >>> p1.enemy = p2
        >>> p1.special_attack()
        >>> p1
        Alex (Mage): 100/70
        >>> p2
        Bob(Mage): 68/100
        """
        self._sp -= 30
        self.enemy.hp = max(0, self.enemy.hp - (40 - self.enemy.defense))
        self.battle_queue.add(self.enemy)
        self.battle_queue.add(self)
        self.next_sprite = 'mage_special_0'

    def is_valid_action(self, action: str) -> bool:
        """ Returns the list of valid actions for a character to perform.

        >>> bq = BattleQueue()
        >>> from a1_playstyle import AutomatedPlaystyle
        >>> auto = AutomatedPlaystyle()
        >>> p1 = Mage('Alex', bq, auto)
        >>> p1.is_valid_action('A')
        True
        >>> p1.is_valid_action('C')
        False
        """
        if action == 'A':
            return self.get_sp() >= 5
        elif action == 'S':
            return self.get_sp() >= 30
        return False

    def __repr__(self) -> str:
        """ Returns a representation of a Mage.

        >>> bq = BattleQueue()
        >>> from a1_playstyle import AutomatedPlaystyle
        >>> auto = AutomatedPlaystyle()
        >>> p1 = Mage('Alex', bq, auto)
        >>> p1
        Alex (Mage): 100/100
        """
        return '{} (Mage): {}/{}'.format(self.get_name(), self.get_hp(),
                                         self.get_sp())

    def get_next_sprite(self) -> str:
        """ Return the name of next sprite to be drawn to a character.

        >>> bq = BattleQueue()
        >>> from a1_playstyle import AutomatedPlaystyle
        >>> auto = AutomatedPlaystyle()
        >>> p1 = Mage('Alex', bq, auto)
        >>> p1.get_next_sprite()
        'mage_idle_0'
        >>> p1.get_next_sprite()
        'mage_idle_1'
        """
        current_sprite = self.next_sprite
        if (self.next_sprite == 'mage_idle_9' or
                self.next_sprite == 'mage_special_9' or
                self.next_sprite == 'mage_attack_9'):
            self.next_sprite = 'mage_idle_0'
        elif self.next_sprite.split(sep='_')[1] == 'attack':
            self.next_sprite = 'mage_attack_{}'.format(
                int(self.next_sprite[-1]) + 1)
        elif self.next_sprite.split(sep='_')[1] == 'special':
            self.next_sprite = 'mage_special_{}'.format(
                int(self.next_sprite[-1]) + 1)
        elif self.next_sprite.split(sep='_')[1] == 'idle':
            self.next_sprite = 'mage_idle_{}'.format(
                int(self.next_sprite[-1]) + 1)
        return current_sprite


class Rogue(Characters):
    """ A class representing Rogue characters."""

    def __init__(self, character_name: str, battle_queue: BattleQueue,
                 playstyle: Playstyle) -> None:
        """ Initialize a rogue character, which initially has 100 hp, 100 sp
        and 10 defense.

        >>> bq = BattleQueue()
        >>> from a1_playstyle import AutomatedPlaystyle
        >>> auto = AutomatedPlaystyle()
        >>> p1 = Rogue('Alex', bq, auto)
        >>> p1
        Alex (Rogue): 100/100
        """
        super().__init__(character_name, battle_queue, playstyle)
        self.defense = 10
        self.next_sprite = 'rogue_idle_0'

    def get_available_actions(self) -> List[str]:
        """ Return a list of available actions based on current sp.

        >>> bq = BattleQueue()
        >>> from a1_playstyle import AutomatedPlaystyle
        >>> auto = AutomatedPlaystyle()
        >>> p1 = Characters('Alex', bq, auto)
        >>> p1.get_available_actions()
        ['A', 'S']
        """
        list_of_actions = []
        if self.is_valid_action('A'):
            list_of_actions.append('A')
        if self.is_valid_action('S'):
            list_of_actions.append('S')
        return list_of_actions

    def attack(self) -> None:
        """ This function is called when performing an attack, which deals 15
        damage, consumes 3 sp and adds self into battle queue.

        >>> bq = BattleQueue()
        >>> from a1_playstyle import AutomatedPlaystyle
        >>> auto = AutomatedPlaystyle()
        >>> p1 = Rogue('Alex', bq, auto)
        >>> p2 = Rogue('Bob', bq, auto)
        >>> p1.enemy = p2
        >>> p1.attack()
        >>> p1
        Alex (Rogue): 100/97
        >>> p2
        Bob (Rogue): 95/100
        """
        self._sp -= 3
        self.enemy.hp = max(0, self.enemy.hp - (15 - self.enemy.defense))
        self.battle_queue.add(self)
        self.next_sprite = 'rogue_attack_0'

    def special_attack(self) -> None:
        """ This function is called when performing a special attack, which
        deals 20 damage, consumes 10 sp and adds self into battle queue two
        times.

        >>> bq = BattleQueue()
        >>> from a1_playstyle import AutomatedPlaystyle
        >>> auto = AutomatedPlaystyle()
        >>> p1 = Rogue('Alex', bq, auto)
        >>> p2 = Rogue('Bob', bq, auto)
        >>> p1.enemy = p2
        >>> p1.special_attack()
        >>> p1
        Alex (Rogue): 100/90
        >>> p2
        Bob (Rogue): 90/100
        """
        self._sp -= 10
        self.enemy.hp = max(0, self.enemy.hp - (20 - self.enemy.defense))
        self.battle_queue.add(self)
        self.battle_queue.add(self)
        self.next_sprite = 'rogue_special_0'

    def is_valid_action(self, action: str) -> bool:
        """ Return a list containing actions that are valid for a character
        to perform.

        >>> bq = BattleQueue()
        >>> from a1_playstyle import AutomatedPlaystyle
        >>> auto = AutomatedPlaystyle()
        >>> p1 = Rogue('Alex', bq, auto)
        >>> p2 = Rogue('Bob', bq, auto)
        >>> p1.enemy = p2
        >>> p1.is_valid_action('S')
        True
        """
        if action == 'A':
            return self.get_sp() >= 3
        elif action == 'S':
            return self.get_sp() >= 10
        return False

    def __repr__(self) -> str:
        """ Returns a representation of a Rogue.

        >>> bq = BattleQueue()
        >>> from a1_playstyle import AutomatedPlaystyle
        >>> auto = AutomatedPlaystyle()
        >>> p1 = Rogue('Alex', bq, auto)
        >>> p2 = Rogue('Bob', bq, auto)
        >>> p1.enemy = p2
        >>> p1
        Alex (Rogue): 100/100
        """
        return '{} (Rogue): {}/{}'.format(self.get_name(), self.get_hp(),
                                          self.get_sp())

    def get_next_sprite(self) -> str:
        """ Return the name of next sprite to be drawn to a character.

        >>> bq = BattleQueue()
        >>> from a1_playstyle import AutomatedPlaystyle
        >>> auto = AutomatedPlaystyle()
        >>> p1 = Rogue('Alex', bq, auto)
        >>> p1.get_next_sprite()
        'rogue_idle_0'
        >>> p1.get_next_sprite()
        'rogue_idle_1'
        """
        current_sprite = self.next_sprite
        if (self.next_sprite == 'rogue_idle_9' or
                self.next_sprite == 'rogue_special_9' or
                self.next_sprite == 'rogue_attack_9'):
            self.next_sprite = 'rogue_idle_0'
        elif self.next_sprite.split(sep='_')[1] == 'attack':
            self.next_sprite = 'rogue_attack_{}'.format(
                int(self.next_sprite[-1]) + 1)
        elif self.next_sprite.split(sep='_')[1] == 'special':
            self.next_sprite = 'rogue_special_{}'.format(
                int(self.next_sprite[-1]) + 1)
        elif self.next_sprite.split(sep='_')[1] == 'idle':
            self.next_sprite = 'rogue_idle_{}'.format(
                int(self.next_sprite[-1]) + 1)
        return current_sprite


if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config='a1_pyta.txt')
