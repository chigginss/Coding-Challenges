# """Balanced Paranthesis"""

# class Stack(object):

#     def 

from python.basics.stack import Stack

def is_balanced(paran_str):

    new_stack = Stack()
    balanced = True

    for char in paran_str:
        if char == "(":
            new_stack.push(char)
        else:
            if new_stack.isEmpty():
                balanced = False
            else:
                new_stack.pop()


    if balanced and new_stack.isEmpty():
        return False
    else:
        return True

is_balanced("())((")
is_balanced("()()()")
is_balanced("())")