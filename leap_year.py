#!/usr/bin/env python3

# Created by: Jonathan Pasco-Arnone
# Created on: December 2020
# This program determines whether it is a leap year or not


def main():
    # This function determines whether it is a leap year or not

    print("")
    print("This program determines whether it is a leap year or not.")
    print("")
    year = int(input("Please input the year: "))

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                if year == str(year):
                    print("Invalid Input")

                else:
                    print("It is a leap year")

            else:
                print("It is a common year")

        else:
            print("It is a leap year")

    else:
        print("It is a common year")


if __name__ == "__main__":
    main()
