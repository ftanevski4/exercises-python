#!/usr/bin/python3


def countingValleys(steps, path):
    # Write your code here
    valleys = 0
    level = 0
    for val in path:
        if val == 'U':
            level += 1
            if(level == 0):
                valleys += 1
        elif val == "D":
            level -= 1

    return valleys


print(countingValleys(8, "UDDDUDUU"))
