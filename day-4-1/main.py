#!/usr/bin/env python3

def main():
    """ Main entry point of the app """
    find_most_slept_guards()
    find_most_slept_minutes()

    print('#3187 * 45 = ' + str(3187*45))


def find_most_slept_minutes():
    file_path = './guard_3187.txt'
    with open(file_path, 'r') as file:
        minutes = {}

        for x in range(60):
            minutes[x] = 0

        fell_asleep = ''

        for line in file:
            split_line = line.split()
            minute = split_line[1][3:-1]
            if split_line[3] == 'asleep':
                fell_asleep = minute
            else:
                time_spent_asleep = int(minute) - int(fell_asleep)
                for x in range(time_spent_asleep):
                    minutes[x + int(fell_asleep)] += 1
                fell_asleep = ''

        for entry in minutes:
            print(entry, minutes.get(entry))


def find_most_slept_guards():
    file_path = './sorted_input.txt'
    with open(file_path, 'r') as file:

        time_table = {}
        guard_id = ''
        fell_asleep = ''

        for line in file:
            split_line = line.split()
            if split_line[2] == 'Guard':
                guard_id = split_line[3][1:]
                time_table[guard_id] = 0

        file.seek(0)
        guard_id = ''
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
                    time_table[guard_id] = time_table.get(guard_id) + time_spent_asleep
                    fell_asleep = ''

        for entry in time_table:
            print(entry, time_table.get(entry))
            # Guard 3187 spent 517 minutes asleep
            # Guard 1217 spent 512 minutes asleep


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
