class ChatSession:
    def __init__(self):
        self.last_course = None

    def remember_course(self, course):
        self.last_course = course

    def get_last_course(self):
        return self.last_course

    def clear(self):
        self.last_course = None

    def get_follow_up_questions(self):
        if self.last_course:
            return [
                "What's the fee?",
                "How long is the course?",
                "Who can apply?",
                "When does it start?",
                "How can I apply?"
            ]

        return [
            "Show me all courses",
            "What's the cheapest course?",
            "Which courses start next year?",
            "Show me courses about Python"
        ]