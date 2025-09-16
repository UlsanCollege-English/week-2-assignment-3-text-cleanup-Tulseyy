from typing import List
from collections import Counter


def unique_words_preserve_order(words: List[str]) -> List[str]:
    """Return first occurrences only (case-sensitive)."""
    seen = set()
    result = []
    for word in words:
        if word not in seen:
            seen.add(word)
            result.append(word)
    return result


def top_k_frequent_first_tie(words: List[str], k: int) -> List[str]:
    """Return up to k words ordered by frequency (high to low).

    For ties, earlier first-appearance wins.
    If k <= 0, raise ValueError.
    """
    if k <= 0:
        raise ValueError("k must be greater than 0")

    freq = Counter(words)
    first_seen = {}
    for i, word in enumerate(words):
        if word not in first_seen:
            first_seen[word] = i

    # Sort by frequency desc, then by first appearance asc
    sorted_words = sorted(freq.items(), key=lambda item: (-item[1], first_seen[item[0]]))
    return [word for word, _ in sorted_words[:k]]


def redact_words(words: List[str], banned: List[str]) -> List[str]:
    """Return a new list where every word in `banned` is replaced by "***".

    Exact matches only; case-sensitive.
    """
    banned_set = set(banned)
    return ["***" if word in banned_set else word for word in words]
