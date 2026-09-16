# Fill in the body of each function below (look for the TODO comments).
#
# The function names and their arguments are already written for you - do NOT
# rename them or change their arguments, because the automated tests call them by
# name. Just replace each `pass` with your code, using `return` to send the answer
# back (not `print`).


import numbers


def seconds_to_hms(total_seconds):
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        return f"{hours}:{minutes:02}:{seconds:02}"



def admission_price(age):
    # TODO (Part 2): return the ticket price (a number) for someone of this age
    if age < 5:
        return 0.0
    elif age <= 12:
        return 8.0
    elif age <= 64:
        return 15.0
    else:
        return 10.0

def sum_multiples(limit):
    total = 0
    for i in range(limit):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total


def total_of_positives(numbers):
    total = 0
    for number in numbers:
        if number > 0:
            total += number
    return total
pass


def main():
    # Optional scratch space - use this to try your functions with sample values.
    # Uncomment a line and run `python lab02.py` to see the result.
    # print(seconds_to_hms(3661))            # 1:01:01
    # print(admission_price(10))             # 8
    # print(sum_multiples(10))               # 23
    # print(total_of_positives([1, -2, 3]))  # 4
    pass


if __name__ == "__main__":
    main()
