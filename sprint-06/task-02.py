import json
from json import JSONEncoder


class UniversityEncoder(JSONEncoder):
    def default(self, o):

        if isinstance(o, (Student, Group)):
            return o.__dict__

        return super().default(o)


class Student:

    def __init__(self, full_name:str, avg_rank:float, courses:list):
        self.full_name = full_name
        self.avg_rank = avg_rank
        self.courses = courses
    
    # ______________ To serialize _______________
    def to_dict(self):
        '''From object to dict'''
        # print(type(self))
        return {
            'full_name': f'{self.full_name}',
            'avg_rank': self.avg_rank,
            'courses': self.courses}


    def serialize_to_json(self, file_name):
        '''Serialize dict to json'''
        
        data_to_save = self.to_dict() # object to dict
        # print(type(data_to_save))
        
        with open(file_name, 'w') as file: # get instance and prepare it to use by calling to file
            json.dump(data_to_save, file) # write dict to file
    # ____________________________________________

    # _______________ To deserialize _____________
    @classmethod
    def from_dict(cls, data):
        ''' From dict to object
        Create instance from dict by calling class constructor
        '''
        return cls(**data) # unpack data


    @classmethod
    def from_json(cls, json_file):
        ''' Deserialize from dict to object'''
        with open(json_file, 'r') as file: # get instance and prepare it to use by calling to file
            data = json.load(file) # get dict
            # print(type(data))
            return cls.from_dict(data) # create instance from received data
    # ___________________________________________

    def __str__(self):
        return f'{self.full_name} ({self.avg_rank}): {self.courses}'
    
    # def __repr__(self):
    #     return self.__str__()

class Group:

    def __init__(self, title:str, students:list):
        self.title = title
        self.students = students

    # _______________ Serialize ________________________
    def to_dict(self):
        # print(type(self))
        students = [Student.to_dict(student) for student in self.students]

        return {
            'title': self.title,
            'students': students
            }


    # def serialize_to_json(list_of_groups, file_name):
    #     with open(file_name, 'w') as file:
    #         data_to_save = [Group.to_dict(group) for group in list_of_groups]
    #         # print(type(data_to_save))
    #         json.dump(data_to_save, file, indent=4)


    # def serialize_to_json(self, file_name):
    #     # for one group
    #     with open(file_name, 'w') as file:

    #         data_to_save = self.to_dict()
    #         print(type(data_to_save))

    #         json.dump(data_to_save, file)

    @staticmethod
    def serialize_to_json(list_of_groups, file_name):
        with open(file_name, 'w') as file:
            json.dump(list_of_groups, file, cls=UniversityEncoder, indent=4)
    # _______________________________________________________

    # __________________ Deserialize ________________________
    @classmethod
    def from_dict(cls, data):
        students = [Student.from_dict(student) for student in data['students']]

        return cls(data['title'], students)
    

    @classmethod
    def create_group_from_file(cls, student_file):
        with open(student_file, 'r') as file:
            data = json.load(file)
            # print(type(data))
        
        # return [cls.from_dict(group) for group in data] # for groups
        return cls.from_dict(data) # for one group
        


    # @classmethod
    # def create_group_from_file(cls, student_file):
    #     with open(student_file, 'r') as file:
    #         data = json.load(file)
    #         # print(type(data))

    #     return [Group.from_dict(group) for group in data]
        # return [cls.from_dict(group) for group in data]
        # return cls(student_file, [Group.from_dict(group) for group in data])

    # ________________________________________________________

    def __str__(self):
        return f'{self.title}: {self.students}'
    
    # def __repr__(self):
    #     return self.__str__()


student_1 = Student('John Dow', 91, ['Python'])
student_2 = Student('Samantha Smith', 86, ['Java'])
student_3 = Student('Bob Miller', 78, ['JavaScrip'])
student_4 = Student('Sofia Scrouge', 90,['Java'])
student_5 = Student('Jane Eire', 75, ['JavaScrip'])
student_6 = Student('Serena Gomez', 83, ['Python'])



group_1 = Group('Python', [student_1, student_6])
group_2 = Group.create_group_from_file('group_1.json')
group_2.serialize_to_json('group_2.json')
group_3 = Group('JavaScript', [student_2, student_4])


groups = [group_1, group_2, group_3]

# # serialize
Group.serialize_to_json(groups, 'groups.json')


# deserialize
all_groups= Group.create_group_from_file('groups.json')
print(all_groups) 