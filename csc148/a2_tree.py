"""
This class represents state of each step in game.
"""


class State:
    """
    A class represents each State for iterative minimax to use
    """
    def __init__(self, bq: 'BattleQueue', prev_action=None,
                 children: list = None, score: int = None) -> None:
        """
        Initializes a state for iterative minimax to use.
        """
        self.bq = bq
        self.children = children[:] if children else []
        self.score = score
        self.prev_action = prev_action
        self.best_action = None


if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config='a2_pyta.txt')
