
class Employee:

    def __init__(self, full_name, **kwargs):
        self.name, self.lastname = full_name.split(' ')

        for key, value in kwargs.items():
            setattr(self, key, value)


john = Employee("John Doe")
print(john.name) # ➞ "John"

mary = Employee("Mary Major", salary=120000)
print(mary.lastname) # ➞ "Major"

richard = Employee("Richard Roe", salary=110000, height=178)
print(richard.height) # ➞ 178

giancarlo = Employee("Giancarlo Rossi", salary=115000, height=182, nationality="Italian")
print(giancarlo.nationality) # ➞ "Italian"
