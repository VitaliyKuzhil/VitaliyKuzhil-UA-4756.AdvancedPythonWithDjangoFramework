
class Testpaper:

    def __init__(self, subject, markscheme, pass_mark):
        self.subject = subject
        self.markscheme = markscheme
        self.pass_mark = pass_mark



class Student:

    def __init__(self, tests_taken='No tests taken'):
        self.tests_taken = tests_taken


    def take_test(self, testpaper, answers):

        all_tests = len(testpaper.markscheme)

        correct_answers = len(set(testpaper.markscheme) & set(answers))

        result = int(round((correct_answers / all_tests) * 100))

        if isinstance(self.tests_taken,str):
            self.tests_taken = dict()

        self.tests_taken[testpaper.subject] = f"Passed! ({result}%)" if result >= int(testpaper.pass_mark[:-1]) else f"Failed! ({result}%)"



paper1 = Testpaper("Maths", ["1A", "2C", "3D", "4A", "5A"], "60%")
paper2 = Testpaper("Chemistry", ["1C", "2C", "3D", "4A"], "75%")
paper3 = Testpaper("Computing", ["1D", "2C", "3C", "4B", "5D", "6C", "7A"], "75%")

student1 = Student()
student2 = Student()

print(student1.tests_taken) # ➞ "No tests taken"
student1.take_test(paper1, ["1A", "2D", "3D", "4A", "5A"])
print(student1.tests_taken) # ➞ {"Maths" : "Passed! (80%)"}

student2.take_test(paper2, ["1C", "2D", "3A", "4C"])
student2.take_test(paper3, ["1A", "2C", "3A", "4C", "5D", "6C", "7B"])
print(student2.tests_taken) # ➞ {"Chemistry" : "Failed! (25%)", "Computing" : "Failed! (43%)"}