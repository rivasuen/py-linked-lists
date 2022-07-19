##########################
# find if target exist in list, return True/False
##########################
from ListNode import init_str_node as init_node


def iterative(head, target):
    # O(n) time
    # O(1) space
    curr = head
    while curr is not None:
        if curr.val == target:
            return True
        curr = curr.next
    return False


def recursive(head, target):
    # O(n) time
    # O(n) space
    if head is None:
        return False
    if head.val == target:
        return True
    return recursive(head.next, target)


def find_demo():
    target = "G"
    print("### find_demo ###")
    print("Iterative:")
    print(iterative(init_node(), target))
    print("Recursive:")
    print(recursive(init_node(), target))
    print("##########################")
