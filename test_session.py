from app.session import ChatSession

session = ChatSession()

print("Before selecting a course:")
print(session.get_follow_up_questions())

session.remember_course("Python for Policy Research")

print("\nAfter selecting a course:")
print(session.get_follow_up_questions())