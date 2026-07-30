import json
from enum import Enum

class NonUniqueException(Exception):
    pass

class Role(Enum):
    Mentor = 1
    Trainee = 2
    Student = 3
    Teacher = 4

    def __str__(self):
        return f"Role.{self.name}"

class Score(str, Enum):
    A = "A"
    B = "B"
    C = "C"
    D = "D"
    F = "F"

    @classmethod
    def _missing_(cls, value):
        obj = str.__new__(cls, str(value))
        obj._value_ = value
        return obj

class Subject:
    def __init__(self, title, id=None):
        self.id = id
        self.title = title

class User:
    def __init__(self, username, password, role, id=None):
        self.id = id
        self.username = username
        self.password = password
        self.role = role
        self.grades = {}

    @classmethod
    def create_user(cls, username, password, role):
        return cls(username, password, role)

    def add_score_for_subject(self, subject: Subject, score: Score):
        if subject.title not in self.grades:
            self.grades[subject.title] = []
        self.grades[subject.title].append(score)

    def __str__(self):
        grades_list = []
        for subj, scores in self.grades.items():
            for s in scores:
                val = s.value if hasattr(s, 'value') else s
                grades_list.append({subj: val})
        return f"{self.username} with role {self.role}: {grades_list}"

class AppEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, User):
            d = {
                "username": obj.username, 
                "password": obj.password, 
                "role": obj.role.value if hasattr(obj.role, 'value') else obj.role
            }
            if obj.id is not None:
                d["id"] = obj.id
            return d
        if isinstance(obj, Subject):
            d = {"title": obj.title}
            if obj.id is not None:
                d["id"] = obj.id
            return d
        if isinstance(obj, Enum):
            return obj.value
        return super().default(obj)

def get_subjects_from_json(subjects_json) -> list:
    with open(subjects_json, 'r') as f:
        data = json.load(f)
    subjects = []
    for item in data:
        title = item.get('title')
        id_val = item.get('id')
        if title:
            subjects.append(Subject(title, id=id_val))
    return subjects

def get_users_with_grades(users_json, subjects_json, grades_json) -> list:
    with open(users_json, 'r') as f:
        users_data = json.load(f)
        
    users_dict = {}
    id_to_user = {}
    for u in users_data:
        uname = u.get('username')
        uid = u.get('id')
        pwd = u.get('password')
        role_val = u.get('role')
        if isinstance(role_val, int):
            try:
                role_val = Role(role_val)
            except ValueError:
                pass
        elif isinstance(role_val, str) and hasattr(Role, role_val):
            role_val = getattr(Role, role_val)
        if uname:
            user_obj = User(uname, pwd, role_val, id=uid)
            users_dict[uname] = user_obj
            if uid is not None:
                id_to_user[uid] = user_obj
    
    subjects = get_subjects_from_json(subjects_json)
    subjects_dict = {sub.title: sub for sub in subjects}
    id_to_subject = {sub.id: sub for sub in subjects if sub.id is not None}
    
    with open(grades_json, 'r') as f:
        grades_data = json.load(f)
        
    for record in grades_data:
        u_key = record.get('username', record.get('user', record.get('user_id')))
        user_obj = users_dict.get(u_key) or id_to_user.get(u_key)
        
        s_key = record.get('subject', record.get('subject_id', record.get('title')))
        subj_obj = subjects_dict.get(s_key) or id_to_subject.get(s_key)
        
        score_val = record.get('score')
        
        if user_obj and subj_obj and score_val is not None:
            try:
                score_obj = Score(score_val)
            except ValueError:
                score_obj = score_val
            user_obj.add_score_for_subject(subj_obj, score_obj)
            
    return list(users_dict.values())

def add_user(user, users):
    if any(u.username == user.username for u in users):
        raise NonUniqueException(f"User with name {user.username} already exists")
    users.append(user)

def add_subject(subject, subjects):
    if any(s.title == subject.title for s in subjects):
        raise NonUniqueException(f"Subject with title {subject.title} already exists")
    subjects.append(subject)

def check_if_user_present(username, password, users):
    for u in users:
        if u.username == username and u.password == password:
            return True
    return False

def get_grades_for_user(username: str, user: User, users: list):
    if user.username == username or user.role == Role.Mentor:
        target_user = next((u for u in users if u.username == username), None)
        if target_user:
            result = []
            for subj, scores in target_user.grades.items():
                for s in scores:
                    val = s.value if hasattr(s, 'value') else s
                    result.append({subj: val})
            return result
    return None

def users_to_json(users, json_file):
    with open(json_file, 'w') as f:
        json.dump(users, f, cls=AppEncoder, indent=4)

def subjects_to_json(subjects, json_file):
    with open(json_file, 'w') as f:
        json.dump(subjects, f, cls=AppEncoder, indent=4)

def grades_to_json(users, subjects, json_file):
    data = []
    valid_subjects = {s.title for s in subjects}
    
    for u in users:
        for subj_title, scores in u.grades.items():
            if subj_title in valid_subjects:
                for s in scores:
                    data.append({
                        "username": u.username, 
                        "subject": subj_title, 
                        "score": s.value if hasattr(s, 'value') else s
                    })
                    
    with open(json_file, 'w') as f:
        json.dump(data, f, indent=4)