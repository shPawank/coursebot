# TODO: search(question, top_k=3) -> list of (course, score)
# Use the BM25 index from indexer.py.
from app.db import load_courses
from app.indexer import build_index, tokenize


courses = load_courses()
bm25 = build_index(courses)


def search_courses(query, limit=3):
    tokens = tokenize(query)
    scores = bm25.get_scores(tokens)

    ranked_indices = scores.argsort()[::-1][:limit]

    results = []

    for index in ranked_indices:
        if scores[index] > 0:
            results.append(courses[index])

    return results
