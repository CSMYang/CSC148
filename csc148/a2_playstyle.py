"""
The Playstyle classes for A2.
Docstring examples are not required for Playstyles.

You are responsible for implementing the get_state_score function, as well as
creating classes for both Iterative Minimax and Recursive Minimax.
"""
from typing import Any
import random
from a2_tree import State


class Playstyle:
    """
    The Playstyle superclass.

    is_manual - Whether the class is a manual Playstyle or not.
    battle_queue - The BattleQueue corresponding to the game this Playstyle is
                   being used in.
    """
    is_manual: bool
    battle_queue: 'BattleQueue'

    def __init__(self, battle_queue: 'BattleQueue') -> None:
        """
        Initialize this Playstyle with BattleQueue as its battle queue.
        """
        self.battle_queue = battle_queue
        self.is_manual = True

    def select_attack(self, parameter: Any = None) -> str:
        """
        Return the attack for the next character in this Playstyle's
        battle_queue to perform.

        Return 'X' if a valid move cannot be found.
        """
        raise NotImplementedError

    def copy(self, new_battle_queue: 'BattleQueue') -> 'Playstyle':
        """
        Return a copy of this Playstyle which uses the BattleQueue
        new_battle_queue.
        """
        raise NotImplementedError


class ManualPlaystyle(Playstyle):
    """
    The ManualPlaystyle. Inherits from Playstyle.
    """

    def select_attack(self, parameter: Any = None) -> str:
        """
        Return the attack for the next character in this Playstyle's
        battle_queue to perform.

        parameter represents a key pressed by a player.

        Return 'X' if a valid move cannot be found.
        """
        if parameter in ['A', 'S']:
            return parameter

        return 'X'

    def copy(self, new_battle_queue: 'BattleQueue') -> 'Playstyle':
        """
        Return a copy of this ManualPlaystyle which uses the
        BattleQueue new_battle_queue.
        """
        return ManualPlaystyle(new_battle_queue)


class RandomPlaystyle(Playstyle):
    """
    The Random playstyle. Inherits from Playstyle.
    """

    def __init__(self, battle_queue: 'BattleQueue') -> None:
        """
        Initialize this RandomPlaystyle with BattleQueue as its battle queue.
        """
        super().__init__(battle_queue)
        self.is_manual = False

    def select_attack(self, parameter: Any = None) -> str:
        """
        Return the attack for the next character in this Playstyle's
        battle_queue to perform.

        Return 'X' if a valid move cannot be found.
        """
        actions = self.battle_queue.peek().get_available_actions()

        if not actions:
            return 'X'

        return random.choice(actions)

    def copy(self, new_battle_queue: 'BattleQueue') -> 'Playstyle':
        """
        Return a copy of this RandomPlaystyle which uses the
        BattleQueue new_battle_queue.
        """
        return RandomPlaystyle(new_battle_queue)


def get_state_score(battle_queue: 'BattleQueue') -> int:
    """
    Return an int corresponding to the highest score that the next player in
    battle_queue can guarantee.

    For a state that's over, the score is the HP of the character who still has
    HP if the next player who was supposed to act is the winner. If the next
    player who was supposed to act is the loser, then the score is -1 * the
    HP of the character who still has HP. If there is no winner (i.e. there's
    a tie) then the score is 0.

    >>> from a2_battle_queue import BattleQueue
    >>> from a2_characters import Rogue, Mage
    >>> bq = BattleQueue()
    >>> r = Rogue("r", bq, ManualPlaystyle(bq))
    >>> m = Mage("m", bq, ManualPlaystyle(bq))
    >>> r.enemy = m
    >>> m.enemy = r
    >>> bq.add(r)
    >>> bq.add(m)
    >>> m.set_hp(3)
    >>> get_state_score(bq)
    100
    >>> r.set_hp(40)
    >>> get_state_score(bq)
    40
    >>> bq.remove()
    r (Rogue): 40/100
    >>> bq.add(r)
    >>> get_state_score(bq)
    -10
    """
    if battle_queue.is_over():
        if battle_queue.get_winner() is None:
            return 0
        if type(battle_queue.get_winner()) == type(battle_queue.peek()):
            return battle_queue.get_winner().get_hp()
        return battle_queue.get_winner().get_hp() * -1
    action = battle_queue.peek().get_available_actions()
    scores = []
    for skill in action:
        new_battlequeue = battle_queue.copy()
        current_player = new_battlequeue.peek()
        if skill == 'A':
            new_battlequeue.peek().attack()
        else:
            new_battlequeue.peek().special_attack()
        if new_battlequeue.peek().get_available_actions() != []:
            new_battlequeue.remove()
        if type(current_player) == type(new_battlequeue.peek()):
            scores.append(get_state_score(new_battlequeue))
        else:
            scores.append(get_state_score(new_battlequeue) * -1)
    return max(scores)


class RecursiveMinimax(Playstyle):
    """
    A class representing Minimax writen recursively.
    """

    def __init__(self, battlequeue: 'BattleQueue') -> None:
        """
        Initializes the minimax with battlequeue battlequeue.
        """
        super().__init__(battlequeue)
        self.is_manual = False

    def select_attack(self, parameter: Any = None) -> str:
        """
        Return the attack for the next character in this Playstyle's
        battle_queue to perform.

        Return 'X' if a valid move cannot be found.
        """
        current_player = self.battle_queue.peek()
        actions = current_player.get_available_actions()
        scores = []
        if not actions:
            return 'X'
        for skill in actions:
            new_battlequeue = self.battle_queue.copy()
            if skill == 'A':
                new_battlequeue.peek().attack()
            else:
                new_battlequeue.peek().special_attack()
            if new_battlequeue.peek().get_available_actions() != []:
                new_battlequeue.remove()
            if type(self.battle_queue.peek()) == type(new_battlequeue.peek()):
                scores.append(get_state_score(new_battlequeue))
            else:
                scores.append(get_state_score(new_battlequeue) * -1)
        return actions[scores.index(max(scores))]

    def copy(self, new_battle_queue: 'BattleQueue') -> 'Playstyle':
        """
        Return a copy of this RandomPlaystyle which uses the
        BattleQueue new_battle_queue.
        """
        return RecursiveMinimax(new_battle_queue)


class IterativeMinimax(Playstyle):
    """
    A class representing Minimax writen iteratively.
    """

    def __init__(self, battlequeue: 'BattleQueue') -> None:
        """
        Initializes the iterative minimax playstyle with battlequeue battlequeue
        """
        super().__init__(battlequeue)
        self.is_manual = False

    def copy(self, new_battle_queue: 'BattleQueue') -> 'Playstyle':
        """
        Return a copy of this RandomPlaystyle which uses the
        BattleQueue new_battle_queue.
        """
        return IterativeMinimax(new_battle_queue)

    def select_attack(self, parameter: Any = None) -> str:
        """
        Return the attack for the next character in this Playstyle's
        battle_queue to perform.

        Return 'X' if a valid move cannot be found.
        """
        new_bq = self.battle_queue.copy()
        stack = []
        state1 = State(new_bq)
        stack.append(state1)
        list_of_states = []
        if not state1.bq.peek().get_available_actions():
            return 'X'
        while stack:
            current_state = stack.pop()
            if current_state.bq.is_over():
                if not current_state.bq.get_winner():
                    current_state.score = 0
                elif type(current_state.bq.get_winner()) == \
                        type(current_state.bq.peek()):
                    current_state.score = current_state.bq.get_winner().get_hp()
                else:
                    current_state.score = \
                        current_state.bq.get_winner().get_hp() * -1
                current_state.best_action = current_state.prev_action
                list_of_states.append(current_state.best_action)
            else:
                if current_state.children:
                    c1, c2 = None, None
                    temp_bq = current_state.bq.copy()
                    if type(temp_bq.peek()) == \
                            type(current_state.children[0].bq.peek()):
                        c1 = current_state.children[0].score
                    else:
                        c1 = current_state.children[0].score * -1
                    if len(current_state.children) == 2:
                        if type(temp_bq.peek()) == \
                                type(current_state.children[1].bq.peek()):
                            c2 = current_state.children[1].score
                        else:
                            c2 = current_state.children[1].score * -1
                    if c2 is None or c1 >= c2:
                        current_state.score = c1
                        current_state.best_action = \
                            current_state.children[0].prev_action
                    else:
                        current_state.score = c2
                        current_state.best_action = \
                            current_state.children[1].prev_action
                    list_of_states.append(current_state.best_action)
                else:
                    action = current_state.bq.peek().get_available_actions()
                    for skill in action:
                        my_bq = current_state.bq.copy()
                        if skill == 'A':
                            my_bq.peek().attack()
                        else:
                            my_bq.peek().special_attack()
                        if my_bq.peek().get_available_actions() != []:
                            my_bq.remove()
                        new_state = State(my_bq, skill)
                        current_state.children.append(new_state)
                    stack.append(current_state)
                    for child in current_state.children:
                        stack.append(child)
        return list_of_states[-1]


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config='a2_pyta.txt')
