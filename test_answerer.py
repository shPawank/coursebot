from app.answerer import chat_response
from app.session import ChatSession

session = ChatSession()

print(chat_response("Hello", session))
print(chat_response("Tell me about Python for Policy Research", session))
print(chat_response("What's the fee?", session))