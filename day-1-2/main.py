#!/usr/bin/env python3


def main():
    """ Main entry point of the app """
    file_path = './input.txt'

    with open(file_path, 'r') as file:
        amount = 0
        frequencies = []
        results = {0}

        # Get all numbers in memory so we don't have to I/O every single number every single time
        for line in file:
            frequencies.append(int(line))

        print(loop_file(amount, frequencies, results))  # 61126


def loop_file(amount, frequencies, results):
    while True:
        for number in frequencies:
            amount += number
            if amount in results:
                return amount
            results.add(amount)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
