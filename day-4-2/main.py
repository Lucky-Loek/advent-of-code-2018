#!/usr/bin/env python3

def main():
    """ Main entry point of the app """
    file_path = './sorted_input.txt'
    with open(file_path, 'r') as file:

        minutes_per_guard = {}

        fell_asleep = ''
        guard_id = ''

        for line in file:
            split_line = line.split()
            if split_line[2] == 'Guard':
                guard_id = split_line[3][1:]
                minutes_per_guard[guard_id] = {}
                for x in range(60):
                    minutes_per_guard[guard_id][x] = 0

        file.seek(0)
        for line in file:
            split_line = line.split()
            if split_line[2] == 'Guard':
                guard_id = split_line[3][1:]
            else:
                minute = split_line[1][3:-1]
                if split_line[3] == 'asleep':
                    fell_asleep = minute
                else:
                    time_spent_asleep = int(minute) - int(fell_asleep)
                    for x in range(time_spent_asleep):
                        minutes_per_guard[guard_id][x + int(fell_asleep)] += 1
                    fell_asleep = ''

        for entry in minutes_per_guard:
            print(entry, keywithmaxval(minutes_per_guard[entry]))
            # Guard 2081 sleeps 18 times on minute 24


def keywithmaxval(d):
    v = list(d.values())
    k = list(d.keys())
    return k[v.index(max(v))], max(v)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
