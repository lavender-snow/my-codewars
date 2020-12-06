class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
def push(head, data):
    n = Node(data)
    n.next = head
    return n

def build_one_two_three():
    n = push(None,3)
    n = push(n,2)
    n = push(n,1)
    return n