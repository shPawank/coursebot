from app.retriever import search_courses

while True:
    query = input("\nAsk about courses (or type 'exit'): ")

    if query.lower() == "exit":
        break

    results = search_courses(query)

    for course in results:
        print(f"- {course['title']} | ₹{course['price']} | {course['duration']}")