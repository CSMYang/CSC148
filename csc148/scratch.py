class Student:
    """
    A class presenting students
    """
    def __init__(self, name: str, num: int) -> None:
        self.name = name
        self.student_num = num
        self.courses = []

    def enroll(self, course: str) -> None:
        if course not in self.courses:
            self.courses.append(course)

    def __str__(self) ->str:
        return '{} ({}) \n{}'.format(self.name, self.student_num,
                                     self.courses)
    def __eq__(self, other) -> bool:
        if type(other) != Student:
            return False
        return self.student_num == other.student_num
    def __repr__(self) ->str:
        return '{} - {} - {}'.format(self.name, self.student_num, self.courses)
