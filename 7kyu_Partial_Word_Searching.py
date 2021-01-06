def word_search(query, seq):
    l = [s for s in seq if query.lower() in s.lower()]
    return l if len(l) > 0 else ['None']