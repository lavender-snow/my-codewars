def list_to_array(node):
    l = []
    while True:
        l.append(node.value)
        if node.next is None:
            break
        else:
            node = node.next
    return l