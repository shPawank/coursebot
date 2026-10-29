# TODO: build_index(courses)
# 1. Turn each course into labelled text:
#    "Course: X. Price: Y. Duration: Z. ..."
# 2. Tokenise (lowercase, split into words).
# 3. Build a rank_bm25.BM25Okapi index and keep the course list beside it.
from rank_bm25 import BM25Okapi


def tokenize(text):
    return text.lower().split()


def build_index(courses):
    documents = []

    for course in courses:
        text = " ".join([
            course["title"],
            course["description"],
            course["eligibility"],
            course["not_eligible"],
            course["duration"],
            course["mode"]
        ])
        documents.append(tokenize(text))

    return BM25Okapi(documents)