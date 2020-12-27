def is_flush(cards):
    for card in cards[1:]:
        if cards[0][-1] != card[-1]:
            return False
    return True