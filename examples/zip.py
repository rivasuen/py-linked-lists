##########################
# zipper 2 lists together
# L1: A B C D
# L2: X Y
# New list: A X B Y C D
##########################
from ListNode import init_str_node as init_node
from examples.show import iterative as show_node


def iterative(head1, head2):
    # O(min(n,m)) time
    # O(1) space
    tail = head1
    curr1 = head1.next
    curr2 = head2
    count = 0
    while curr1 is not None and curr2 is not None:
        if count % 2 == 0:
            tail.next = curr2
            curr2 = curr2.next
        else:
            tail.next = curr1
            curr1 = curr1.next

        tail = tail.next
        count += 1
    if curr1 is not None:
        tail.next = curr1
    if curr2 is not None:
        tail.next = curr2

    return head1


def recursive(head1, head2):
    # O(min(n, m))
    # O(min(n, m))
    if head1 is None and head2 is None:
        return None
    if head1 is None:
        return head2
    if head2 is None:
        return head1

    next1 = head1.next
    next2 = head2.next
    head1.next = head2
    head2.next = recursive(next1, next2)
    return head1


def zip_demo():
    print("### zip_demo ###")
    print("Input:")
    m = 5
    n = 2
    show_node(init_node(m))
    show_node(init_node(n))
    print("Iterative:")
    my_iterative_node = iterative(init_node(m), init_node(n))
    show_node(my_iterative_node)
    print("Recursive:")
    my_recursive_node = recursive(init_node(m), init_node(n))
    show_node(my_recursive_node)
    print("##########################")
