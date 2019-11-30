from ex4 import *
import unittest


class ExerciseTests(unittest.TestCase):
    def test_client_code(self):
        """
        Tests the client code to make sure the exercise passes it.
        """
        lnk = LinkedList()
        lnk.prepend(3)
        lnk.prepend(2)
        lnk.prepend(1)

        front_id = id(lnk.front)
        back_id = id(lnk.back)
        lnk.swap_front_back()

        self.assertEqual(str(lnk), "3 -> 2 -> 1 -> |")
        self.assertEqual(front_id, id(lnk.back))
        self.assertEqual(back_id, id(lnk.front))

        lnk2 = LinkedList()
        lnk2.prepend(2)
        lnk2.prepend(1)

        front_id2 = id(lnk2.front)
        back_id2 = id(lnk2.back)
        lnk2.swap_front_back()

        self.assertEqual(str(lnk2), "2 -> 1 -> |")
        self.assertEqual(front_id2, id(lnk2.back))
        self.assertEqual(back_id2, id(lnk2.front))

    def test_hidden(self):
        """
        The hidden test for students.
        """
        # Swap with a linkedlist with 5 items
        lnk = LinkedList()
        lnk.prepend(5)
        lnk.prepend(4)
        lnk.prepend(3)
        lnk.prepend(2)
        lnk.prepend(1)

        front_id = id(lnk.front)
        back_id = id(lnk.back)
        lnk.swap_front_back()

        self.assertEqual(str(lnk), "5 -> 2 -> 3 -> 4 -> 1 -> |")
        self.assertEqual(front_id, id(lnk.back))
        self.assertEqual(back_id, id(lnk.front))

        # Swap with an empty linkedlist
        lnk2 = LinkedList()
        lnk2.swap_front_back()

        self.assertEqual(str(lnk2), "|")

        # Swap with a linkedlist with duplicate elements in it
        lnk3 = LinkedList()
        lnk3.prepend(3)
        lnk3.prepend(4)
        lnk3.prepend(3)
        lnk3.prepend(2)
        lnk3.prepend(1)

        front_id3 = id(lnk3.front)
        back_id3 = id(lnk3.back)
        lnk3.swap_front_back()

        self.assertEqual(str(lnk3), "3 -> 2 -> 3 -> 4 -> 1 -> |")
        self.assertEqual(front_id3, id(lnk3.back))
        self.assertEqual(back_id3, id(lnk3.front))


if __name__ == "__main__":
    unittest.main(exit=False)
