#!/usr/bin/env python3

#Author: Ricardo Jimenez
#Date: 15-06-2025
# This script simulates the vtdft command functionality using argparse.
# It allows users to specify a logging level and a section to display.

import argparse
import logging


def main():
    parser = argparse.ArgumentParser(
        description="Simulate the vtdft command"
    )

    parser.add_argument(
        "-l", "--log",
        type=int,
        default=0,
        help="Logging level (3 = enabled)/n\
                0 = No logging/n \
                1 = Error logging/n \
                2 = Warning logging/n \
                3 = Info logging (default)/n \
                4 = Debug logging/n"
    )

    parser.add_argument(
        "--section",
        required=True,
        help="Section to display /n \
        Available sections: 1.1, 1.2, 2.1, 2.2, 3.1, 3.2/n \
        Section 1.1: Checks memory usage of the server/n\
        Section 1.2: Checks CPU usage of the server/n \
        Section 2.1: Checks disk usage of the server/n" \
    )

    args = parser.parse_args()

    if args.log == 3:
        print("Logging is activated.")

    if args.section == "1.1":
        print("Function in section 1.1: my_function()")
    else:
        print(f"No implementation for section {args.section}")

if __name__ == "__main__":
    main()