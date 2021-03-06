#!/usr/bin/env python3

def main():
    """ Main entry point of the app """
    file_path = './input.txt'
    with open(file_path, 'r') as file:
        file_contents = file.read()

        while True:
            done, file_contents = remove_double_characters(file_contents)
            if done:
                print(file_contents)
                print(len(file_contents))  # 11118
                break


def remove_double_characters(string):
    done = True

    for x in range(len(string)):
        if x == 0:
            continue

        try:
            string[x]
        except IndexError:
            break

        if string[x - 1].lower() == string[x].lower() and ((string[x - 1].islower() and string[x].isupper()) or (string[x - 1].isupper() and string[x].islower())):
            string = string[:x - 1] + string[x + 1:]
            done = False

    return done, string


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
