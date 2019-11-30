class Employee:
    """ Represent an Employee’s information
    name - name
    phone - phone number
    email - email
    """
    name: str
    phone: int
    email: str

    def __init__(self, name: str, phone: int, email: str) -> None:
        """ Initialize a new emplyee
        """
        self.name, self.phone, self.email = name, phone, email

    def __str__(self) -> str:
        """ Return a string representation of the employee information.
        """
        return ("Name: {}\nPhone:{}\nEmail:{}\nMonthly Pay:{}"
        .format(self.name, self.phone, self.email,
        self.get_monthly_payment()))
    def get_monthly_payment(self) -> int:
        """ Return the monthly payment (in cents) of the employee.
        """
        raise NotImplementedError

class SalariedEmployee(Employee):
    """ A class representing salaried employees."""

    def __init__(self, name: str, phone: int, email: str, salary: int) -> None:
        """ Initialize a new salaried employee

        Extends the init method of superclass.
        """
        super().__init__(name, phone, email)
        self.annual_salary = salary

    def get_monthly_payment(self) -> int:
        return self.annual_salary // 12

class HourlyEmployee(Employee):
    """ A class representing hourly paid employees."""

    def __init__(self, name: str, phone: int, email: str) -> None:
        """ Initialize a new emplyee
        """
        self.name, self.phone, self.email = name, phone, email
