
class SchemaValidationError(Exception):
    def __init__(self, value):
      self.value = value

    def __str__(self):
      return str(self.value)
    
class IncorrectTypeOfSchema(SchemaValidationError):
    def __init__(self, value):
       super().__init__(value)


class MissedAttribute(SchemaValidationError):
    def __init__(self, value):
       super().__init__(value)


class BadTypeOfAttribute(SchemaValidationError):
    def __init__(self, value):
       super().__init__(value)


class MissedRequiredAttribute(MissedAttribute):
    def __init__(self, value):
       super().__init__(value)

    def __str__(self):
        return f"Missing required field: '{self.value}'"


def validate_json(data: dict, schema: dict) -> bool:
    # Виправляємо перевірку: якщо ключа 'type' взагалі немає або він не "object"
    if schema.get('type') != "object":
        raise IncorrectTypeOfSchema("Only 'object' type schemas are supported.")
    
    if not isinstance(data, dict):
        raise IncorrectTypeOfSchema("Data must be an object")

    type_mapping = {
        "string": str,
        "integer": int,
        "boolean": bool,
        "array": list,
        "object": dict
    }

    required_attributes = schema.get("required", [])
    for attribute in required_attributes:
        if attribute not in data:
            raise MissedRequiredAttribute(attribute)

    properties = schema.get("properties", {})
    for attribute, expected_schema in properties.items():
        if attribute in data:
            val = data[attribute]
            expected_type_str = expected_schema.get("type")
            expected_type = type_mapping.get(expected_type_str)

            if expected_type is dict:
                if not isinstance(val, dict):
                    raise BadTypeOfAttribute(attribute)
                validate_json(val, expected_schema)
            elif expected_type is int:
                if type(val) is not int:
                    raise BadTypeOfAttribute(attribute)
            elif expected_type is bool:
                if type(val) is not bool:
                    raise BadTypeOfAttribute(attribute)
            else:
                if not isinstance(val, expected_type):
                    raise BadTypeOfAttribute(attribute)

    return True





student_schema = {
    "type": "object",
    "properties": {
        "full_name": {"type": "string"},
        "avg_rank": {"type": "number"},
        "is_active": {"type": "boolean"},
        "courses": {
            "type": "array",
            "items": {"type": "string"}
        }
    },
    "required": ["full_name", "is_active"]
}


# Правильні дані
good_student_1 = {"full_name": "John Dow",
                "avg_rank": 91,
                "is_active": True,
                "courses": ["Python", "JavaScript"]
                }


# Правильні дані
good_student_2 = {
                "full_name": "Serena Gomez",
                "avg_rank": 83.4,
                "is_active": False,
                "courses": ["Python", "Go"]
                }


# Неправильні дані (avg_rank — рядок замість числа)
bad_student_1 = {
                "full_name": "Jane Eire",
                "avg_rank": "Seventy five",
                "is_active": False,
                "courses": ["JavaScript", "Java"]
                }


bad_student_2 = {
                "full_name": "Sofia Scrouge",
                "avg_rank": 90.2,
                "courses": ["Java"]
                }


validate_json(good_student_1, student_schema)