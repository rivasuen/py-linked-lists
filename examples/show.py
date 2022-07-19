##########################
# show all value stored in list
##########################

from ListNode import init_num_node as init_node


def iterative(head):
    # O(n) time
    # O(n) space
    curr = head
    while curr is not None:
        print(curr.val)
        curr = curr.next


def recursive(head):
    # O(n) time
    # O(n) space
    if head is None:
        return
    print(head.val)
    return recursive(head.next)


def show_demo():
    print("### show_demo ###")
    print("Iterative:")
    iterative(init_node())
    print("Recursive:")
    recursive(init_node())
    print("##########################")
