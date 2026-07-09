import re

pattern = r'\"([^\"]+):\s([^,]+),\s(\d+)\"'


def pretty_message(data):
    return ((book, author, year) for match in re.finditer(pattern, data) for book, author, year in [match.groups()])


# data = '"Head First. Python: PROSystem, 2021"# and "Coding for Kids Python & Blockchain Programming: Elliot Davis, 2022"'

data = '"Design Patterns in Java: Gang of Four, 1994", "Introduction to Algorithms: Thomas H. Cormen, 2009" - "Clean Code: Robert C. Martin, 2008"; "The Pragmatic Programmer: Andrew Hunt, 1999" and "Artificial Intelligence: A Modern Approach: Stuart Russell, 2003"'


for item in pretty_message(data):
    print(item)