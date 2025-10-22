#!/usr/bin/env python3
# Created By: Abdul
# Date: 10/22/2025
# Program to ask the user to guess a number between 0 and 9


def main():
    # Get integer from user
    user_integer = int(input("Please enter an integer: "))

    # Determine if the integer is positive, negative, or zero
    if user_integer > 0:
        print("You entered a positive integer: ", user_integer)
    elif user_integer < 0:
        print("You entered a negative integer: ", user_integer)
    else:
        print("You entered zero.")


if __name__ == "__main__":
    main()
