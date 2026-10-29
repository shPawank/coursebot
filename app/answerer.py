# TODO: build_answer(course, field) -> str
# Use templates, e.g. "The fee for {title} is {price}."
# If the field is empty, say the information is not available.
# Later you can swap this file for an LLM-based version.
from app.db import load_courses
from app.retriever import search_courses
from app.session import ChatSession

def find_course(query):
    courses = load_courses()
    query = query.lower().strip()

    # 1. Exact course title match
    for course in courses:
        if course["title"].lower() in query:
            return course

    # 2. Find courses containing all the user's keywords
    query_words = set(query.split())
    matches = []

    for course in courses:
        title_words = set(course["title"].lower().split())

        if query_words and query_words.issubset(title_words):
            matches.append(course)

    # Return a course only if the match is unambiguous
    if len(matches) == 1:
        return matches[0]

    return None


def search_and_answer(query):
    results = search_courses(query, limit=3)

    if not results:
        return "I couldn't find a relevant course. Try another topic."

    response = "Here are some courses you might like:\n"

    for course in results:
        response += (
            f"\n- {course['title']}"
            f"\n  Fee: ₹{course['price']}"
            f"\n  Duration: {course['duration']}\n"
        )

    return response

def get_course_price(query):
    courses = load_courses()
    query = query.lower()

    for course in courses:
        title = course["title"].lower()

        if title in query:
            if course["price"].strip():
                return f"The fee for {course['title']} is ₹{course['price']}."

            return f"Pricing information for {course['title']} is unavailable."

    return "Which course would you like to know the fee for?"

def get_cheapest_course():
    courses = load_courses()

    priced_courses = [
        course for course in courses
        if course["price"].strip().isdigit()
    ]

    if not priced_courses:
        return "Course pricing information is unavailable."

    cheapest = min(priced_courses, key=lambda course: int(course["price"]))

    return (
        f"The cheapest course is {cheapest['title']}, "
        f"priced at ₹{cheapest['price']}."
    )


def get_course_duration(query):
    courses = load_courses()
    query = query.lower()

    for course in courses:
        title = course["title"].lower()

        if title in query:
            if course["duration"].strip():
                return (
                    f"{course['title']} takes "
                    f"{course['duration']} to complete."
                )

            return f"Duration information for {course['title']} is unavailable."

    return "Which course would you like to know the duration of?"

def check_eligibility(query):
    courses = load_courses()
    query = query.lower()

    for course in courses:
        title = course["title"].lower()

        if title in query:
            eligible = course["eligibility"]
            not_eligible = course["not_eligible"]

            return (
                f"Eligibility for {course['title']}:\n"
                f"Who can apply: {eligible}\n"
                f"Who cannot apply: {not_eligible}"
            )

    return "Which course would you like to check eligibility for?"

def get_course_launch_date(query):
    courses = load_courses()
    query = query.lower()

    for course in courses:
        title = course["title"].lower()

        if title in query:
            launch_date = course["launch_date"].strip()

            if launch_date:
                return (
                    f"{course['title']} is scheduled to start on "
                    f"{launch_date}."
                )

            return f"The start date for {course['title']} is not available."

    return "Which course would you like to know the start date for?"

from datetime import datetime


def get_courses_by_year(year):
    courses = load_courses()

    matching_courses = [
        course for course in courses
        if course["launch_date"].strip()
        and course["launch_date"].startswith(str(year))
    ]

    if not matching_courses:
        return f"No courses are scheduled to start in {year}."

    response = f"Courses starting in {year}:\n"

    for course in matching_courses:
        response += (
            f"\n- {course['title']} — "
            f"{course['launch_date']}"
        )

    return response

def answer_courses_by_year(query):
    from datetime import date

    query = query.lower()

    if "next year" in query:
        year = date.today().year + 1
    else:
        import re

        match = re.search(r"\b20\d{2}\b", query)

        if not match:
            return "Which year would you like to search for?"

        year = int(match.group())

    return get_courses_by_year(year)

from app.intents import detect_intent

def list_all_courses():
    courses = load_courses()

    if not courses:
        return "No courses are currently available."

    response = "Here are all available courses:\n"

    for course in courses:
        response += (
            f"\n- {course['title']}"
            f"\n  Fee: ₹{course['price'] or 'Not available'}"
            f"\n  Duration: {course['duration'] or 'Not available'}\n"
        )

    return response

def answer_question(query, session=None):
    if session is None:
        session = ChatSession()

    intent = detect_intent(query)

    courses = load_courses()
    query_lower = query.lower().strip()

    # Recognize complete course titles
    matched_course = None

    for course in courses:
        if course["title"].lower() in query_lower:
            matched_course = course
            break

    if matched_course:
        session.remember_course(matched_course["title"])

    # Use remembered course for follow-up questions
    last_course = session.get_last_course()

    if intent == "price":
        if last_course and not any(
            course["title"].lower() in query_lower
            for course in courses
        ):
            query = f"What is the fee for {last_course}?"

        return get_course_price(query)

    elif intent == "duration":
        if last_course and not any(
            course["title"].lower() in query_lower
            for course in courses
        ):
            query = f"What is the duration of {last_course}?"

        return get_course_duration(query)

    elif intent == "cheapest":
        return get_cheapest_course()

    elif intent == "eligibility":
        if last_course and not any(
            course["title"].lower() in query_lower
            for course in courses
        ):
            query = f"Who is eligible for {last_course}?"

        return check_eligibility(query)

    elif intent == "launch_date":
        if last_course and not any(
            course["title"].lower() in query_lower
            for course in courses
        ):
            query = f"When does {last_course} start?"

        return get_course_launch_date(query)

    elif intent == "courses_by_year":
        return answer_courses_by_year(query)
    
    elif intent == "list_courses":
        return list_all_courses()

    elif intent == "course_search":
        return search_and_answer(query)

    elif intent == "greeting":
        return (
            "Hello! I can help you explore courses, fees, "
            "durations, eligibility, and start dates."
        )

    return "Sorry, I didn't understand. Could you rephrase your question?"

def chat_response(query, session=None):
    if session is None:
        session = ChatSession()

    answer = answer_question(query, session)

    return {
        "answer": answer,
        "suggestions": session.get_follow_up_questions()
    }