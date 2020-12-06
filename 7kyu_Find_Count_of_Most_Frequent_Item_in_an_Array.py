def most_frequent_item_count(collection):
    return max([collection.count(n) for n in set(collection)]) if len(collection) > 0 else 0