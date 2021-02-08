
# find pedometer reading palindrome

def compare_string(search):

    return search == search[::-1]


def search_str():

    x = 100000

    while x < 1000000:
        if compare_string((str(x))[2:]):
            if compare_string((str(x + 1)[1:])):
                if compare_string((str(x + 2))[1:5]):
                    if compare_string((str(x + 3))):
                        return x

        x += 1


print(f" No. are  {search_str()}")

