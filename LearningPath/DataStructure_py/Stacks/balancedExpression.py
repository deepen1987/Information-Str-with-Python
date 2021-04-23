def balanced_expression(exp):
    my_stack = []

    for i in exp:
        if left_bracket(i):
            my_stack.append(i)

        if right_bracket(i):
            if len(my_stack) == 0:
                return False
            current = my_stack.pop()
            if bracket_matching(i, current):
                return False

    if len(my_stack) == 0:
        return True
    else:
        return False


def left_bracket(i):
    return i == "(" or i == "<" or i == "{" or i == "["


def right_bracket(i):
    return i == ")" or i == ">" or i == "}" or i == "]"


def bracket_matching(left, right):
    return (left == ")" and right != "(") or (left == ">" and right != "<") or (left == "}" and right != "{") or (
            left == "]" and right != "[")


s = input("")
print(balanced_expression(s))
