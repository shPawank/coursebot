from app.intents import detect_intent

questions = [
    "Which courses start in 2027?",
    "What courses start next year?",
    "Courses launching in 2028",
    "When does Python for Policy Research start?",
    "Does Competition Law Basics start?",
    "Hello"
]

for question in questions:
    print(question, "->", detect_intent(question))