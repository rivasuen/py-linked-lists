##########################
# sum all value stored in list
##########################
from ListNode import init_num_node as init_node


def iterative(head):
    # O(n) time
    # O(1) space
    total = 0
    curr = head
    while curr is not None:
        total += curr.val
        curr = curr.next
    return total


def recursive(head):
    # O(n) time
    # O(n) space
    if head is None:
        return 0
    return head.val + recursive(head.next)


def sum_demo():
    print("### sum_demo ###")
    print("Iterative:")
    print(iterative(init_node()))
    print("Recursive:")
    print(recursive(init_node()))
    print("##########################")
