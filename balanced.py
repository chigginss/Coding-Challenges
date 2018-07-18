# """Balanced Paranthesis"""

# class Stack(object):

#     def 

def is_balanced(paran_str):

    new_stack = []

    for char in paran_str:
        if char == "(":
            new_stack.append(char)
        elif char == ")" and len(new_stack) != 0:
            new_stack.pop(char)

    if len(new_stack) != 0:
        print False
    else:
        print True

is_balanced("())((")
is_balanced("()()()")
is_balanced("())")