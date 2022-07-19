class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def init_num_node(length=5):
    node = None
    while length > 0:
        node = ListNode(length, node)
        length -= 1
    return node


def init_str_node(length=5):
    node = None
    letter_ord = ord("A")
    while length > 0:
        node = ListNode(chr(letter_ord), node)
        letter_ord += 1
        length -= 1
    return node
