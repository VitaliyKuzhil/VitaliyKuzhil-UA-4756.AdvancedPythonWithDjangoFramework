import json
from pathlib import Path


def path_to_folder(filename:str) -> Path:
    '''
    Function which build a path for the output files
    '''
    path = Path(r'./sprint-06/task-02_files/') / filename
    path.parent.mkdir(parents=True, exist_ok=True)
    return path


class Student:

    def __init__(self, full_name: str, avg_rank: float, courses: list):
        self.full_name = full_name
        self.avg_rank = avg_rank
        self.courses = courses

    # ---------------- Serialize ----------------

    def to_dict(self):
        """Convert object to dict."""
        return {
            "full_name": self.full_name,
            "avg_rank": self.avg_rank,
            "courses": self.courses,
        }

    def serialize_to_json(self, file_name):
        """Serialize Student object to JSON file."""
        data_to_save = self.to_dict()

        with open(path_to_folder(file_name), "w") as file:
            json.dump(data_to_save, file, indent=4)

    # ---------------- Deserialize ----------------

    @classmethod
    def from_dict(cls, data):
        """Create Student object from dict."""
        return cls(**data)

    @classmethod
    def from_json(cls, json_file):
        """Deserialize Student from JSON file."""
        with open(path_to_folder(json_file), "r") as file:
            data = json.load(file)

        return cls.from_dict(data)

    # ------------------------------------------------

    def __str__(self):
        return f"{self.full_name} ({self.avg_rank}): {self.courses}"


class Group:

    def __init__(self, title: str, students: list):
        self.title = title
        self.students = students

    # ---------------- Serialize ----------------

    def to_dict(self):
        students = [student.to_dict() for student in self.students]

        return {
            "title": self.title,
            "students": students,
        }

    @staticmethod
    def serialize_to_json(list_of_groups, file_name):
        with open(path_to_folder(file_name), "w") as file:

            data_to_save = [group.to_dict() for group in list_of_groups]

            json.dump(data_to_save, file, indent=4)

    # ---------------- Deserialize ----------------

    @classmethod
    def from_dict(cls, data):

        students = [Student.from_dict(student) for student in data["students"]]

        return cls(data["title"], students)

    @classmethod
    def create_group_from_file(cls, student_file):

        with open(path_to_folder(student_file), "r") as file:
            data = json.load(file)

        return [cls.from_dict(group) for group in data]

    # ------------------------------------------------


    def __str__(self):
        return f"{self.title}: {self.students}"


student_1 = Student("John Dow", 91, ["Python"])
student_2 = Student("Samantha Smith", 86, ["Java"])
student_3 = Student("Bob Miller", 78, ["JavaScript"])
student_4 = Student("Sofia Scrouge", 90, ["Java"])
student_5 = Student("Jane Eire", 75, ["JavaScript"])
student_6 = Student("Serena Gomez", 83, ["Python"])

group_1 = Group("Python", [student_1, student_6])
group_2 = Group("Java", [student_2, student_4])
group_3 = Group("JavaScript", [student_3, student_5])

groups = [group_1, group_2, group_3]

# Serialize
Group.serialize_to_json(groups, "groups.json")

# Deserialize
all_groups = Group.create_group_from_file("groups.json")
print(all_groups)