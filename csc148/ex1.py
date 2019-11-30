""" Define your class up here. """
from typing import List


class Course:
    """
    A class representing a course.
    """
    enrolled_students: List[str]
    waitlist: List[str]
    course_name: str
    course_capacity: int

    def __init__(self, course_name: str) -> None:
        """ Initialize a course with the course name course_name. The course
        will initially has an empty list of enrolled students enrolled_students,
        course capacity of 0 and an empty list of students in waitlist waitlist.

        >>> c = Course('CSC148')
        >>> c.course_name
        'CSC148'
        >>> c.course_capacity
        0
        >>> c.enrolled_students
        []
        >>> c.waitlist
        []
        """
        self.course_name = course_name
        self.enrolled_students = []
        self.course_capacity = 0
        self.waitlist = []

    def set_course_capacity(self, capacity: int) -> None:
        """ Change the course capacity of a given course to new capacity
        capacity

        >>> c = Course('csc148')
        >>> c.course_capacity
        0
        >>> c.set_course_capacity(2)
        >>> c.course_capacity
        2
        >>> c.set_course_capacity(5)
        >>> c.course_capacity
        5
        """
        self.course_capacity = capacity

    def add_student(self, student_name: str) -> None:
        """ Add a student with student_name to the list of enrolled students
        enrolled_students of a course in a sorted way. If the number of enrolled
        students of that course is equal to the course capacity, add the student
        to waitlist instead. If the student is already enrolled or in waitlist,
        'This student is already in this course.' will be prompted.

        >>> c = Course('csc148')
        >>> c.set_course_capacity(2)
        >>> c.add_student('John')
        >>> c.enrolled_students
        ['John']
        >>> c.add_student('Alan')
        >>> c.enrolled_students
        ['Alan', 'John']
        >>> c.add_student('Bob')
        >>> c.enrolled_students
        ['Alan', 'John']
        >>> c.waitlist
        ['Bob']
        """
        if len(self.enrolled_students) < self.course_capacity and student_name \
                not in self.enrolled_students:
            self.enrolled_students.append(student_name)
            self.enrolled_students.sort()
        elif len(self.enrolled_students) >= self.course_capacity and \
                student_name not in self.waitlist:
            self.waitlist.append(student_name)
        else:
            print('This student is already in this course')

    def get_enrolled_students(self) -> List[str]:
        """ Return a list of enrolled students of a course. Names of enrolled
        students will be sorted in order.

        >>> c = Course('CSC148')
        >>> c.set_course_capacity(2)
        >>> c.add_student('Lisa')
        >>> c.get_enrolled_students()
        ['Lisa']
        >>> c.add_student('Alex')
        >>> c.get_enrolled_students()
        ['Alex', 'Lisa']
        """
        return self.enrolled_students

    def get_waitlist(self) -> List[str]:
        """ Return a list of students in waitlist of a course. Names of students
        in waitlist will be in the order they were added

        >>> c = Course('csc148')
        >>> c.set_course_capacity(1)
        >>> c.add_student('Alan')
        >>> c.add_student('Bob')
        >>> c.add_student('Alex')
        >>> c.get_waitlist()
        ['Bob', 'Alex']
        """
        return self.waitlist

    def remove_student(self, student_name) -> None:
        """ Remove a student with student_name from enrolled_students, and add
        the first student in waitlist to enrolled_students. If the
        student is in waitlist but not in enrolled_students, remove it from
        waitlist. If the student_name provided does not exixt in waitlist and
        enrolled_students, 'Student name is invalid' will be shown.

        >>> c = Course('CSC148')
        >>> c.set_course_capacity(1)
        >>> c.add_student('Alan')
        >>> c.add_student('Alex')
        >>> c.add_student('Bob')
        >>> c.add_student('John')
        >>> c.get_waitlist()
        ['Alex', 'Bob', 'John']
        >>> c.get_enrolled_students()
        ['Alan']
        >>> c.remove_student('Alan')
        >>> c.get_enrolled_students()
        ['Alex']
        >>> c.get_waitlist()
        ['Bob', 'John']
        """
        if student_name in self.enrolled_students:
            self.enrolled_students.remove(student_name)
            self.add_student(self.waitlist[0])
            self.waitlist.remove(self.waitlist[0])
        elif student_name in self.waitlist:
            self.waitlist.remove(student_name)
        else:
            print('Student name is invalid')

    def __eq__(self, other) -> bool:
        """ Return True iff self and other have the same students enrolled.

        >>> c = Course('CSC148')
        >>> c.set_course_capacity(1)
        >>> c.add_student('Alan')
        >>> c2 = Course('CSC165')
        >>> c2.set_course_capacity(1)
        >>> c2.add_student('Alan')
        >>> c == c2
        True
        """
        return self.enrolled_students == other.enrolled_students and \
               self.waitlist == other.waitlist and type(self) == type(other)

    def __str__(self) -> str:
        """ Return the string representation of a course.

        >>> c = Course('CSC148')
        >>> print(c)
        The course CSC148 has 0 student(s) enrolled with 0 student(s) on the
        waitlist.
        """
        first_part = 'The course {} has {} student(s) enrolled with'.format(
            self.course_name, len(self.enrolled_students))
        second_part = ' {} student(s) on the waitlist.'.format(
            len(self.waitlist))
        return first_part + second_part


# ---- Everything below this is client code. Do NOT modify anything! ----
if __name__ == '__main__':
    c = Course("CSC148")
    c.set_course_capacity(2)  # You may assume this number will always be a
    # positive integer and that set_course_capacity()
    # will be called before adding students and
    # never after adding students.

    c.add_student("Sophia")
    c.add_student("Danny")
    c.add_student("Jacqueline")

    assert str(c) == ("The course CSC148 has 2 student(s) enrolled with" +
                      " 1 student(s) on the waitlist.")

    # get_enrolled_students() should return the enrolled students in sorted
    # order.
    assert c.get_enrolled_students() == ['Danny', 'Sophia']

    # get_waitlist() should return the students on the waitlist in the order
    # that they were added.
    assert c.get_waitlist() == ['Jacqueline']

    c.add_student("David")
    assert c.get_waitlist() == ['Jacqueline', 'David']

    # if remove_student() removes an enrolled student, add in the first
    # waitlisted student to enrolled students.
    # HINT: The list method .pop() might be useful here.
    #       See help(list.pop) for details.
    c.remove_student("Danny")
    assert c.get_enrolled_students() == ['Jacqueline', 'Sophia']
    assert c.get_waitlist() == ['David']

    c.remove_student("David")
    assert c.get_waitlist() == []

    # When comparing 2 courses, they are the same if the enrolled students
    # are the same (regardless of order), the waitlist is the same
    # (and in the same order), and the course code and capacity are the same.
    c2 = Course("CSC148")
    c2.set_course_capacity(2)
    c2.add_student("Jacqueline")
    c2.add_student("Sophia")
    assert c == c2

    c2.add_student("David")
    assert c != c2

    # Below is how python_ta (PythonTA/pyTA/etc.) is called.
    # When run, your code should produce no errors from python_ta.
    # You must have python_ta installed for this to work (see Lab 1 and
    # the Software Installation page).
    import python_ta

    python_ta.check_all(config="ex1_pyta.txt")
