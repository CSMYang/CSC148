"""
The SkillDecisionTree class for A2.

You are to implement the pick_skill() method in SkillDecisionTree, as well as
implement create_default_tree() such that it returns the example tree used in
a2.pdf.

This tree will be used during the gameplay of a2_game, but we may test your
SkillDecisionTree with other examples.
"""
from typing import Callable, List
from a2_skills import MageAttack, MageSpecial, RogueAttack, RogueSpecial


class SkillDecisionTree:
    """
    A class representing the SkillDecisionTree used by Sorcerer's in A2.

    value - the skill that this SkillDecisionTree contains.
    condition - the function that this SkillDecisionTree will check.
    priority - the priority number of this SkillDecisionTree.
               You may assume priority numbers are unique (i.e. no two
               SkillDecisionTrees will have the same number.)
    children - the subtrees of this SkillDecisionTree.
    """
    value: 'Skill'
    condition: Callable[['Character', 'Character'], bool]
    priority: int
    children: List['SkillDecisionTree']

    def __init__(self, value: 'Skill',
                 condition: Callable[['Character', 'Character'], bool],
                 priority: int,
                 children: List['SkillDecisionTree'] = None):
        """
        Initialize this SkillDecisionTree with the value value, condition
        function condition, priority number priority, and the children in
        children, if provided.

        >>> from a2_skills import MageAttack
        >>> def f(caster, _):
        ...     return caster.hp > 50
        >>> t = SkillDecisionTree(MageAttack(), f, 1)
        >>> t.priority
        1
        >>> type(t.value) == MageAttack
        True
        """
        self.value = value
        self.condition = condition
        self.priority = priority
        self.children = children[:] if children else []

    # Implement a method called pick_skill which takes in a caster and target
    # and returns a skill.
    def pick_all(self, caster: 'Character', target: 'Character') -> list:
        """
        Helper function for pick skill. Return a list of all skills that satisfy
        the condition of caster to use on target.
        """
        if not self.condition(caster, target) or not self.children:
            return [self]
        return sum([child.pick_all(caster, target) for child in self.children],
                   [])

    def pick_skill(self, caster: 'Character', target: 'Character') -> 'Skill':
        """
        Pick one skill from the tree that has the highest priority under passed
        conditions for caster to use on target.
        """
        list_of_skills = self.pick_all(caster, target)
        skill_to_return = list_of_skills[0]
        for skill in list_of_skills:
            if skill.priority < skill_to_return.priority:
                skill_to_return = skill
        return skill_to_return.value


def create_default_tree() -> SkillDecisionTree:
    """
    Return a SkillDecisionTree that matches the one described in a2.pdf.

    >>> s = create_default_tree()
    >>> s.value
    MageAttack()
    >>> s.priority
    5
    """
    a = SkillDecisionTree(RogueAttack(), f6, 6)
    b = SkillDecisionTree(RogueAttack(), f6, 8)
    c = SkillDecisionTree(RogueSpecial(), f6, 7)
    d = SkillDecisionTree(RogueSpecial(), f5, 4, [a])
    e = SkillDecisionTree(MageSpecial(), f3, 2, [b])
    f = SkillDecisionTree(RogueAttack(), f4, 1, [c])
    g = SkillDecisionTree(MageAttack(), f2, 3, [d])
    return SkillDecisionTree(MageAttack(), f1, 5, [g, e, f])


def f1(caster, _) -> bool:
    """
    Returns True if caster's hp is greater than 50.
    """
    return caster.get_hp() > 50


def f2(caster, _) -> bool:
    """
    Returns True if caster's sp is greater than 20.
    """
    return caster.get_sp() > 20


def f3(_, target) -> bool:
    """
    Returns True if target's sp is greater than 40.
    """
    return target.get_sp() > 40


def f4(caster, _) -> bool:
    """
    Returns True if caster's hp is greater than 90.
    """
    return caster.get_hp() > 90


def f5(_, target) -> bool:
    """
    Returns True if target's hp is greater than 30.
    """
    return target.get_hp() < 30


def f6(_, __) -> bool:
    """
    A function for conditon of leaves in skill decision tree.
    Always return False.
    """
    return False


if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config='a2_pyta.txt')
