#!/usr/bin/env python3

def main():
    """ Main entry point of the app """
    file_path = './input.txt'

    with open(file_path, 'r') as file:
        w, h = 1000, 1000
        matrix = [[0 for x in range(w)] for y in range(h)]

        for line in file:
            elements = line.split()
            coordinates = elements[2].split(',')
            xCoord = int(coordinates[0])
            yCoord = int(coordinates[1][:-1])
            surface = elements[3].split('x')
            xSurf = int(surface[0])
            ySurf = int(surface[1])

            for y in range(ySurf):
                for x in range(xSurf):
                    matrix[xCoord + x][yCoord + y] += 1

        overlaps = 0

        for x in range(len(matrix)):
            for y in range(len(matrix)):
                if matrix[x][y] > 1:
                    overlaps += 1

        print(overlaps)  # 109785



if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
