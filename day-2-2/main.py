#!/usr/bin/env python3

def main():
    """ Main entry point of the app """
    file_path = './input.txt'

    with open(file_path, 'r') as file:
        lines = []
        for line in file:
            lines.append(line)

        for line in lines:
            for check_line in lines:
                difference = [i for i in range(len(line)) if line[i] != check_line[i]]

                if len(difference) == 1:
                    print(check_line)  # prtkqyluiusocwvaezjmhmfngx
                    print(line)  # prtkqyluiusocwvaezjmhmfbgx



if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
