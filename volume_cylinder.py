#!/usr/bin/env python3

# Created by Jenoe Balote
# Created on May 2021
# This program calculates the volume of a cylinder

import constant


def calculate_volume(radius_from_user, height_from_user):
    # calculate area
    area = constant.PI * radius_from_user ** 2 * height_from_user

    return area


def main():
    # this function calls other functions
    # input

    print("Let's calculate the volume of a cylinder!")
    print("")
    string_radius = str(input("Enter radius (cm): "))
    string_height = str(input("Enter height (cm): "))

    # call function and output
    try:
        radius_from_user = int(string_radius)
        height_from_user = int(string_height)
        cylinder_volume = calculate_volume(radius_from_user, height_from_user)
        print("\nThe volume is: {} cm³.".format(cylinder_volume))
    except Exception:
        print("\nInvalid.")
    finally:
        print("\nThanks for participating!")


if __name__ == "__main__":
    main()
