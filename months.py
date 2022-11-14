#!/usr/bin/env python3

# Created by: Johanna Liu
# Created on: Oct 2022
# This program adds two numbers

import random


def main():
    # this is a number guessing game

    # input
    print("This program identifies the days in a month.")
    str_month = input("Enter month number: ")
    str_year = input("Enter year: ")

    # process
    try:
        int_year = int(str_year)
        int_month = int(str_month)
        if int_year < 0:
                print("Invalid year")
        else:
            if int_year % 4 == 0 or int_year % 400 == 0:
                if int_year % 100 == 0 and int_year % 400 != 0:
                    if int_month < 0 and int_month >= 13:
                        print("Invalid Month")
                    else:
                        if int_month == 2:
                            print("This month has 28 days.")
                        elif int_month % 2 == 0:
                            print("This month has 30 days.")
                        else:
                            print("This month has 31 days.")
                else:
                    print("This is a leap year.")
                    if int_month == 2:
                        print("There are 29 days.")
                    elif int_month % 2 == 0:
                        print("This month has 30 days.")
                    else:
                        print("This month has 31 days.")
            else:
                if int_month < 0 and int_month >= 13:
                    print("Invalid Month")
                else:
                    if int_month == 2:
                        print("This month has 28 days.")
                    elif int_month % 2 == 0:
                        print("This month has 30 days.")
                    else:
                        print("This month has 31 days.")
    except ValueError:
        print("Invalid integer")
    # output

    print("\nDone.")


if __name__ == "__main__":
    main()
