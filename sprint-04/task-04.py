
class Employee:

    def __init__(self, firstname, lastname, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = int(salary)


    @staticmethod
    def from_string(string):
        firstname, lastname, salary = string.split('-')

        return Employee(firstname, lastname, salary)



# emp1 = Employee("Mary", "Sue", 60000)
emp2 = Employee.from_string("John-Smith-55000")

# print(emp1.firstname) # ➞ "Mary"
# print(emp1.salary) # ➞ 60000

print(emp2.firstname) # ➞ "John"