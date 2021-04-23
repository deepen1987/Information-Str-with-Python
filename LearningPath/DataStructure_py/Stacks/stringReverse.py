def string_reverse(str1):
    s = ""
    my_stack = list(str1)
    for i in range(len(my_stack)):
        s += my_stack.pop()
    return s


in_str = "abcde"
print(string_reverse(in_str))
