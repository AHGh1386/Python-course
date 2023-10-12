# fizz buzz
def fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        print("Fizz_Buzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

fizz_buzz(29)
