"""
This file contains a class for arranging people into evenly divided groups.
"""
from typing import List
import random


class Arranger:
    """
    The main class for arranging people.
    """

    def __init__(self) -> None:
        """
        Initializes arranger with an empty list containing the people to
        arrange.
        """
        self._content = []
        self._num = 0
        self._divided_teams = []

    def get_people(self) -> None:
        """
        Prints all the people currently added.
        """
        for person in self._content:
            print(person)

    def get_num(self) -> int:
        """
        Returns the num of people in content.
        """
        return self._num

    def add_person(self, person: str) -> None:
        """
        Adds person into content.
        """
        self._content.append(person)
        self._num += 1

    def split_teams(self, num: int) -> None:
        """
        Split content into different teams.
        """
        for _ in range(num):
            self._divided_teams.append([])

