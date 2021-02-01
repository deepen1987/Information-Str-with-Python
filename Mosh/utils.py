number_list = []


def list_insert(num1):
    number_list.append(num1)


def find_max():
    maximum = 0
    for itr in number_list:
        if itr > maximum:
            maximum = itr
    print('Below is the list ')
    print(number_list)
    print(f'The max number in the list is {maximum}')