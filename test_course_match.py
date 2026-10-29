from app.answerer import find_course

queries = [
    "competition law",
    "Python for Policy Research",
    "advanced competition law",
    "something unrelated"
]

for query in queries:
    course = find_course(query)

    if course:
        print(f"{query} -> {course['title']}")
    else:
        print(f"{query} -> No unique match")