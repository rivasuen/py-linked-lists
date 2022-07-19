##########################
# get value in list by index
##########################
from ListNode import init_str_node as init_node


def iterative(head, index):
    # O(n) time
    # O(1) space
    curr = head
    while curr is not None:
        if index == 0:
            return curr.val
        index -= 1
        curr = curr.next
    return None


def recursive(head, index):
    # O(n) time
    # O(n) space
    if head is None:
        return None
    if index == 0:
        return head.val
    return recursive(head.next, index - 1)


def get_demo():
    index = 5
    print("### get_demo ###")
    print("Iterative:")
    print(iterative(init_node(), index))
    print("Recursive:")
    print(recursive(init_node(), index))
    print("##########################")
