#!/usr/bin/env python3

# created by: Ryan Walsh
# created on: January 2021
# this program accepts marks from user and calculates the average of the marks
# after "-1" is entered


def averaging_marks(marks):
    # averaging marks

    sum = 0
    for counter in marks:
        sum += counter
    if len(marks) is 0:
        average = 0
    else:
        average = sum / len(marks)

    average = int(average)
    return average


def main():
    # this program accepts marks from user and calculates the average of the
    # marks after "-1" is entered

    marks = []
    mark_from_user = 0
    print("Please enter 1 mark at a time. Enter -1 at the end.")
    print("\n", end="")
    print("Make sure all marks you enter are between 0 to 100.")
    # input
    while True:
        try:
            while mark_from_user != -1:
                mark_from_user = input("Enter a mark(0-100):")
                mark_from_user = int(mark_from_user)
                if mark_from_user < -1 or mark_from_user > 100:
                    print("The mark must be between 0 and 100")
                    print("\n", end="")
                else:
                    marks.append(mark_from_user)
            marks.pop()
            print("\n", end="")
            break
        except Exception:
            print("Please enter a valid number.")
            print("\n", end="")

    averaged_mark = averaging_marks(marks)
    print("Your entered marks:")
    print("\n", end="")
    fmt = "[%s"
    for counter in marks:
        print(fmt % counter, end="")
        fmt = ", %s"
    print("]")
    print("\n", end="")

    print("\n", end="")
    print("The average mark is {0}%".format(averaged_mark))


if __name__ == "__main__":
    main()
