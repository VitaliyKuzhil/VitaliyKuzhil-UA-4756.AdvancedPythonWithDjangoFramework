import json
import os
from json import JSONEncoder


class UniversityEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, (Student, Group)):
            return o.__dict__
        return super().default(o)


class Student:

    def __init__(self, full_name: str, avg_rank: float, courses: list):
        self.full_name = full_name
        self.avg_rank = avg_rank
        self.courses = courses
    
    # ______________ To serialize _______________
    def to_dict(self):
        '''From object to dict'''
        return {
            'full_name': f'{self.full_name}',
            'avg_rank': self.avg_rank,
            'courses': self.courses
        }

    def serialize_to_json(self, file_name):
        '''Serialize dict to json'''
        data_to_save = self.to_dict()
        with open(file_name, 'w') as file:
            json.dump(data_to_save, file)
    # ____________________________________________

    # _______________ To deserialize _____________
    @classmethod
    def from_dict(cls, data):
        ''' From dict to object '''
        return cls(**data)

    @classmethod
    def from_json(cls, json_file):
        ''' Deserialize from dict to object'''
        with open(json_file, 'r') as file:
            data = json.load(file)
            return cls.from_dict(data)
    # ___________________________________________

    def __str__(self):
        return f'{self.full_name} ({self.avg_rank}): {self.courses}'

    def __repr__(self):
        return f'"{self}"'


class Group:

    def __init__(self, title: str, students: list):
        self.title = title
        self.students = students

    # _______________ Serialize ________________________
    def to_dict(self):
        students = [student.to_dict() if isinstance(student, Student) else student for student in self.students]
        return {
            'title': self.title,
            'students': students
        }

    @staticmethod
    def serialize_to_json(list_of_groups, file_name):
        with open(file_name, 'w') as file:
            json.dump(list_of_groups, file, cls=UniversityEncoder)
    # _______________________________________________________

    # __________________ Deserialize ________________________
    @classmethod
    def from_dict(cls, data):
        students = [Student.from_dict(student) for student in data['students']]
        return cls(data['title'], students)
    
    @classmethod
    def create_group_from_file(cls, student_file):
        title = os.path.splitext(os.path.basename(student_file))[0]

        with open(student_file, 'r') as file:
            data = json.load(file)
        
        # 1. Якщо у файлі список студентів
        if isinstance(data, list):
            students = [Student.from_dict(student) for student in data]
            return cls(title, students)
        
        # 2. Якщо у файлі словник
        elif isinstance(data, dict):
            # Якщо це вже готова серіалізована група
            if 'students' in data:
                return cls.from_dict(data)
            # Якщо це один студент
            else:
                return cls(title, [Student.from_dict(data)])
    # ________________________________________________________

    def __str__(self):
        return f'{self.title}: {self.students}'

    def __repr__(self):
        return self.__str__()