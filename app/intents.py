# TODO: detect_field(question) -> field name or None
# Check "not eligible" / "cannot apply" BEFORE "eligible" / "can apply".
def detect_intent(query):
    query = query.lower().strip()

    # Price
    if any(word in query for word in ["price", "fee", "cost", "cheapest", "expensive"]):
        if "cheapest" in query:
            return "cheapest"
        return "price"

    # Duration
    if any(word in query for word in ["duration", "long", "weeks", "months", "how long"]):
        return "duration"

    # Eligibility
    eligibility_phrases = [
        "eligible", "eligibility", "qualify", "qualification",
        "who can apply", "can apply", "who is eligible",
        "requirements"
    ]

    if any(phrase in query for phrase in eligibility_phrases):
        return "eligibility"

       # Courses by year
    if any(phrase in query for phrase in [
        "which courses start",
        "what courses start",
        "courses starting",
        "courses launching",
        "courses in 2027",
        "courses in 2028",
        "next year"
    ]):
        return "courses_by_year"

    # Launch date for a specific course
    launch_phrases = [
        "start", "starts", "starting", "launch", "launches",
        "upcoming", "when does", "when will", "begin", "begins"
    ]

    if any(phrase in query for phrase in launch_phrases):
        return "launch_date"

    if any(phrase in query for phrase in launch_phrases):
        return "launch_date"

    # List courses
    if any(word in query for word in ["all courses", "available courses", "list courses"]):
        return "list_courses"

    # General course search
    if any(word in query for word in [
        "course", "learn", "teach", "training", "about",
        "interested in", "looking for", "related to",
        "find", "show me"
    ]):
        return "course_search"



    # Greetings
    if query in ["hi", "hello", "hey", "good morning", "good afternoon", "good evening"]:
        return "greeting"
    return "course_search"