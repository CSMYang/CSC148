# Import the student solution
from ex1 import *
import unittest


class ExerciseTests(unittest.TestCase):
    def test_client_code(self):
        """
        Tests the client code to make sure the exercise passes it.
        """
        c = Course("CSC148")
        c.set_course_capacity(2)  # You may assume this number will always be a
        # positive integer and that set_course_capacity()
        # will be called before adding students and
        # never after adding students.

        c.add_student("Sophia")
        c.add_student("Danny")
        c.add_student("Jacqueline")

        self.assertEqual(str(c),
                         ("The course CSC148 has 2 student(s) enrolled with" +
                          " 1 student(s) on the waitlist."))

        # get_enrolled_students() should return the enrolled students in sorted
        # order.
        self.assertEqual(c.get_enrolled_students(), ['Danny', 'Sophia'])

        # get_waitlist() should return the students on the waitlist in the order
        # that they were added.
        self.assertEqual(c.get_waitlist(), ['Jacqueline'])

        c.add_student("David")
        self.assertEqual(c.get_waitlist(), ['Jacqueline', 'David'])

        # if remove_student() removes an enrolled student, add in the first
        # waitlisted student to enrolled students.
        # HINT: The list method .pop() might be useful here.
        #       See help(list.pop) for details.
        c.remove_student("Danny")
        self.assertEqual(c.get_enrolled_students(), ['Jacqueline', 'Sophia'])
        self.assertEqual(c.get_waitlist(), ['David'])

        c.remove_student("David")
        self.assertEqual(c.get_waitlist(), [])

        # When comparing 2 courses, they are the same if the enrolled students
        # are the same (regardless of order), the waitlist is the same
        # (and in the same order), and the course code and capacity are the same.
        c2 = Course("CSC148")
        c2.set_course_capacity(2)
        c2.add_student("Jacqueline")
        c2.add_student("Sophia")
        self.assertEqual(c, c2)

        c2.add_student("David")
        self.assertNotEqual(c, c2)

    def test_hidden(self):
        """
        The hidden test for students.
        """
        c = Course("CSC108")
        c.set_course_capacity(3)

        c.add_student("Sophia")
        expected = ['Sophia']
        self.assertEqual(c.get_enrolled_students(), expected)
        self.assertEqual(str(c),
                         ("The course CSC108 has 1 student(s) enrolled with" +
                          " 0 student(s) on the waitlist."))

        c.add_student("Jen")
        expected = ['Jen', 'Sophia']
        self.assertEqual(c.get_enrolled_students(), expected)
        self.assertEqual(str(c),
                         ("The course CSC108 has 2 student(s) enrolled with" +
                          " 0 student(s) on the waitlist."))

        c.add_student("Tom")
        expected = ['Jen', 'Sophia', 'Tom']
        self.assertEqual(c.get_enrolled_students(), expected)
        self.assertEqual(str(c),
                         ("The course CSC108 has 3 student(s) enrolled with" +
                          " 0 student(s) on the waitlist."))

        c.add_student("Diane")
        expected = ['Jen', 'Sophia', 'Tom']
        self.assertEqual(c.get_enrolled_students(), expected)
        self.assertEqual(str(c),
                         ("The course CSC108 has 3 student(s) enrolled with" +
                          " 1 student(s) on the waitlist."))

        expected = ['Diane']
        self.assertEqual(c.get_waitlist(), expected)

        c.add_student("Alan")
        expected = ['Diane', 'Alan']
        self.assertEqual(c.get_waitlist(), expected)
        self.assertEqual(str(c),
                         ("The course CSC108 has 3 student(s) enrolled with" +
                          " 2 student(s) on the waitlist."))

        c.remove_student("Tom")
        expected = ['Diane', 'Jen', 'Sophia']
        self.assertEqual(c.get_enrolled_students(), expected)

        expected = ['Alan']
        self.assertEqual(c.get_waitlist(), expected)
        self.assertEqual(str(c),
                         ("The course CSC108 has 3 student(s) enrolled with" +
                          " 1 student(s) on the waitlist."))

        c1 = Course("CSC108")
        c2 = Course("CSC108")
        c1.set_course_capacity(2)
        c2.set_course_capacity(3)
        self.assertNotEqual(c1, c2)

        c3 = Course("CSC108")
        c3.set_course_capacity(2)
        self.assertEqual(c1, c3)

        c1.add_student("Banana")
        c1.add_student("Apple")

        c3.add_student("Banana")
        c3.add_student("Apple")
        self.assertEqual(c1, c3)

        c1.add_student("Cat")
        c3.add_student("Cat")
        self.assertEqual(c1, c3)

        c1.add_student("Box")
        c1.add_student("Dog")
        c3.add_student("Dog")
        c3.add_student("Box")
        self.assertNotEqual(c1, c3)


if __name__ == "__main__":
    unittest.main(exit=False)
