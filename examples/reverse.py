##########################
# reverse the list
##########################
from ListNode import init_str_node as init_node
from examples.show import iterative as show_node


def iterative(head):
    # O(n) time
    # O(1) space
    prev = None
    curr = head
    while curr is not None:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev


def recursive(head, prev=None):
    # O(n) time
    # O(n) space
    if head is None:
        return prev
    temp = head.next
    head.next = prev
    return recursive(temp, head)


def reverse_demo():
    print("### reverse_demo ###")
    print("Input:")
    m = 3
    show_node(init_node(m))
    print("Iterative:")
    my_iterative_node = iterative(init_node(m))
    show_node(my_iterative_node)
    print("Recursive:")
    my_recursive_node = recursive(init_node(m))
    show_node(my_recursive_node)
    print("##########################")
