#   write a program that calculates average
def average():
    summery, counter = 0, 0
    while True:
        number = int(input("Enter your Number to Calculate New Average :"))
        if number != 0:
            summery += number
            counter += 1
            print(f"The Current Average is: {summery//counter}")
        else:
            print(f"The Last Average is: {summery//counter}")
            break
