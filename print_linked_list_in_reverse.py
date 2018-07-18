"""
Print a linked-list in reverse using recursion

next and head are given

"""

def print_rev(head):
    if head is not None:
        print_rev(head.next)
        print head.next
    else:
        return None