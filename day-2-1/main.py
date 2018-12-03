#!/usr/bin/env python3

def main():
    """ Main entry point of the app """
    file_path = './input.txt'

    with open(file_path, 'r') as file:
        twos = 0
        threes = 0

        for line in file:
            two = False
            three = False

            if line.count('a') == 2 \
                    or line.count('b') == 2\
                    or line.count('c') == 2\
                    or line.count('d') == 2\
                    or line.count('e') == 2\
                    or line.count('f') == 2\
                    or line.count('g') == 2\
                    or line.count('h') == 2\
                    or line.count('i') == 2\
                    or line.count('j') == 2\
                    or line.count('k') == 2\
                    or line.count('l') == 2\
                    or line.count('m') == 2\
                    or line.count('n') == 2\
                    or line.count('o') == 2\
                    or line.count('p') == 2\
                    or line.count('q') == 2\
                    or line.count('r') == 2\
                    or line.count('s') == 2\
                    or line.count('t') == 2\
                    or line.count('u') == 2\
                    or line.count('v') == 2\
                    or line.count('w') == 2\
                    or line.count('x') == 2\
                    or line.count('y') == 2\
                    or line.count('z') == 2:
                two = True

            if line.count('a') == 3 \
                    or line.count('b') == 3\
                    or line.count('d') == 3\
                    or line.count('c') == 3\
                    or line.count('e') == 3\
                    or line.count('f') == 3\
                    or line.count('g') == 3\
                    or line.count('h') == 3\
                    or line.count('i') == 3\
                    or line.count('j') == 3\
                    or line.count('k') == 3\
                    or line.count('l') == 3\
                    or line.count('m') == 3\
                    or line.count('n') == 3\
                    or line.count('o') == 3\
                    or line.count('p') == 3\
                    or line.count('q') == 3\
                    or line.count('r') == 3\
                    or line.count('s') == 3\
                    or line.count('t') == 3\
                    or line.count('u') == 3\
                    or line.count('v') == 3\
                    or line.count('w') == 3\
                    or line.count('x') == 3\
                    or line.count('y') == 3\
                    or line.count('z') == 3:
                three = True

            if two:
                twos += 1
            if three:
                threes += 1

        print(twos * threes)  # 6723



if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
