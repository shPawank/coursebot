# TODO: load_courses() -> list[dict]
# While developing, read data/courses.csv with pandas.
# Later, read from the real database with a READ-ONLY user.


import csv

def load_courses(path="data/courses.csv"):
    with open(path, "r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)
        courses = list(reader)

    return courses
