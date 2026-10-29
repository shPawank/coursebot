from app.db import load_courses

courses = load_courses()

print("Total courses:", len(courses))
print("First course:", courses[0])
print("Available columns:", list(courses[0].keys()))
