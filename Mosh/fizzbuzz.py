# write a function
# if user_input/3 return Fizz
# if user_input / 5 return Buzz
# if user_input / 3 & 5 return FizzBuzz
# else return the number


def fizzbuzz(value):
    if (value % 3 == 0) and (value % 5 == 0):
        return "FizzBuzz"
    if value % 3 == 0:
        return "Fizz"
    if value % 5 == 0:
        return "Buzz"
    return value


user_input = int(input("Enter a number "))

print(fizzbuzz(user_input))


# if user_input/3 return Fizz

# if user_input / 5 return Buzz

# if user_input / 3 & 5 return FizzBuzz

# else return the number
