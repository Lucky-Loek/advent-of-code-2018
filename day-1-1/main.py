#!/usr/bin/env python3


def main():
    """ Main entry point of the app """
    file_path = './input.txt'

    with open(file_path, 'r') as file:
        amount = 0
        for line in file:
            delta = int(line)
            amount += delta

        print(amount)  # 423


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
