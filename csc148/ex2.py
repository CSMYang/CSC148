""" Define your class up here. """
from typing import List


class Person:
    """A class representing a person."""

    def __init__(self, name: str) -> None:
        """ Initialize a person named name. A person initially has an empty list
        of eaten food.

        >>> p = Person('Alina')
        >>> p.get_name()
        'Alina'
        """
        self._name = name
        self._eaten_food = []

    def eat(self, food_name: str) -> None:
        """ This function is called when someone eats a food, and the food will
        be appended to his list of eaten food.

        >>> p = Person('Alina')
        >>> p.get_eaten_food()
        []
        >>> p.eat('Bobo')
        >>> p.get_eaten_food()
        ['Bobo']
        """
        self._eaten_food.append(food_name)

    def get_name(self) -> str:
        """ Return the name of a person.

        >>> p = Person('Alina')
        >>> p.get_name()
        'Alina'
        """
        return self._name

    def get_eaten_food(self) -> List:
        """ Return the list of food a person ate.

        >>> p = Person('Alina')
        >>> p.eat('Bobo')
        ['Bobo']
        """
        return self._eaten_food

    def __eq__(self, other) -> bool:
        """ Return True iff an object has the same name and eaten food as this
        person.

        >>> p = Person('Alina')
        >>> s = Student('Lisa')
        >>> p == s
        False
        >>> s.change_name('Alina')
        >>> p == s
        True
        >>> p.eat('Apple')
        >>> p == s
        False
        >>> s.eat('Apple')
        >>> p == s
        True
        """
        if type(other) == Person or type(other) == Student:
            return self.get_name() == other.get_name() and \
                   self.get_eaten_food() == other.get_eaten_food()
        return False

    def change_name(self, new_name) -> None:
        """ Changes a person's name to new_name.

        >>> p = Person('Alina')
        >>> p.get_name()
        'Alina'
        >>> p.change_name('whatever')
        >>> p.get_name()
        'whatever'
        """
        self._name = new_name

    def __str__(self) -> str:
        """ Return the string representation of a person.

        >>> p = Person('Alina')
        >>> p.eat('Apple')
        >>> str(p)
        'Alina is a Person who has eaten 1 thing(s).'
        """
        return self.get_name() + ' is a Person who has eaten {} thing(s).'. \
            format(len(self.get_eaten_food()))


class Student(Person):
    """ A class representing students."""

    def __init__(self, name: str) -> None:
        """ Initialize a student with name name.

        >>> s = Student('Alina')
        >>> s.get_courses()
        []
        >>> s.get_name()
        'Alina'
        >>> s.get_eaten_food()
        []
        """
        super().__init__(name)
        self.enrolled_courses = []

    def get_courses(self) -> List:
        """ Return a list of courses that the student enrolled.

        >>> s = Student('Alina')
        >>> c = Course('CSC148')
        >>> c.add_student(s)
        >>> s.get_courses()
        ['CSC148']
        """
        return self.enrolled_courses

    def __str__(self) -> str:
        """ Return a string representation of a student.
        >>> s = Student('Alina')
        >>> str(s)
        'Alina is a Student who has eaten 0 thing(s).'
        """
        return self._name + ' is a Student who has eaten {} thing(s).'.format(
            len(super().get_eaten_food()))


class Course:
    """ A class representing Course."""

    def __init__(self, course_name: str) -> None:
        """ Initialize a course with its course_name."""
        self._course_name = course_name
        self._enrolled_students = []

    def add_student(self, student: Student) -> None:
        """ Add a student to the given course."""
        self._enrolled_students.append(student)
        student.enrolled_courses.append(self._course_name)

    def __str__(self) -> str:
        """ Return the string representation of a course."""
        the_str = self._course_name + ' Student log:'
        for student in self._enrolled_students:
            the_str = the_str + '\n' + str(student)
        return the_str


# ---- Everything below this is client code. Do NOT modify anything! ----
if __name__ == '__main__':
    s = Student("Sophia")
    p = Person("Jen")

    # A Student should be a Person, but a Person should not be a Student
    assert isinstance(s, Person), "A Student should also be a Person"
    assert not isinstance(p, Student), "A Person should not be a Student"

    s.eat("Cupcake")
    s.eat("Apple")

    # get_eaten_food() should return a list of foods in the order they were
    # eaten
    expected = ("s.get_eaten_food() returned {} instead " +
                "of ['Cupcake, 'Apple']").format(s.get_eaten_food())
    assert s.get_eaten_food() == ['Cupcake', 'Apple'], expected

    p.eat("Cupcake")
    p.eat("Apple")

    expected = ("p.get_eaten_food() returned {} instead " +
                "of ['Cupcake, 'Apple']").format(s.get_eaten_food())
    assert p.get_eaten_food() == ['Cupcake', 'Apple'], expected

    assert p != s, ("A Person should only be equal to another object if they" +
                    " have the same name and eaten foods.")

    p.change_name("Sophia")

    assert p == s, ("A Person should be equal to another object if they" +
                    " have the same name and eaten foods.")
    assert s == p, ("A Student should be equal to another object if they" +
                    " have the same name and eaten foods.")

    error = ("str(p) was expected to return\nSophia is a Person who has " +
             "eaten 2 thing(s).\nBut got\n{}\ninstead.").format(str(p))

    assert str(p) == "Sophia is a Person who has eaten 2 thing(s).", error

    error = ("str(s) was expected to return\nSophia is a Student who has " +
             "eaten 2 thing(s).\nBut got\n{}\ninstead.").format(str(s))
    assert str(s) == "Sophia is a Student who has eaten 2 thing(s).", error

    c = Course("CSC148")
    c.add_student(s)

    # Assume that get_courses() returns a list in the order that the
    # courses were added
    expected = ("After adding a Student to a Course, that Student should " +
                "have that course in the list returned by get_courses but " +
                "got {} instead.").format(s.get_courses())
    assert s.get_courses() == ["CSC148"], expected

    assert s == p, ("After adding a course to a Student, that Student should " +
                    "be equal to a Person with the same foods eaten and name.")
    assert p == s, ("After adding a course to a Student, that Person should " +
                    "be equal to a Student with the same foods eaten and name.")

    assert not getattr(p, 'get_courses', None), ("Person should not have a " +
                                                 "get_courses() method.")

    expected = ("When printing a Course, the string\n" +
                "CSC148 Student log:\nSophia is a Student " +
                "who has eaten 2 thing(s).\nWas expected" +
                ", but we got\n{}\ninstead").format(str(c))
    assert str(c) == ("CSC148 Student log:\nSophia is a Student " +
                      "who has eaten 2 thing(s)."), expected

    s2 = Student("Jacqueline")
    c.add_student(s2)

    expected = ("When printing a Course, the string\n" +
                "CSC148 Student log:\nSophia is a Student " +
                "who has eaten 2 thing(s).\nJacqueline " +
                "is a Student who has eaten 0 thing(s).\nWas expected" +
                ", but we got\n{}\ninstead").format(str(c))
    assert str(c) == ("CSC148 Student log:\nSophia is a Student " +
                      "who has eaten 2 thing(s).\nJacqueline is a Student " +
                      "who has eaten 0 thing(s)."), expected

    # Below is how python_ta (PythonTA/pyTA/etc.) is called.
    # When run, your code should produce no errors from python_ta.
    # You must have python_ta installed for this to work (see Lab 1 and
    # the Software Installation page).
    import python_ta

    python_ta.check_all(config="ex2_pyta.txt")
