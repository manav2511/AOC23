import re

# Read input
with open("input.txt", "r") as inp:
   games = inp.read().strip().split("\n")

def solve_1(data):
    color_dict = { 
        "red": 12,
        "green": 13,
        "blue": 14
    }

    possible_count = 0
    for i in range(len(data)):
        s = data[i]

        # Find all the numbers followed by color names in the string
        matches = re.findall(r'(\d+) (red|green|blue)', s)

        # For each match, print the count and the color
        possible = True
        for count, color in matches:
            if int(count) > color_dict[color]:
                possible = False
                break

        if possible: possible_count += i+1

    return possible_count

def solve_2(data):
    power_sum = 0
    for i in range(len(data)):
        color_dict = { 
            "red": 0,
            "green": 0,
            "blue": 0
        }

        s = data[i]

        # Find all the numbers followed by color names in the string
        matches = re.findall(r'(\d+) (red|green|blue)', s)

        # For each match, print the count and the color
        for count, color in matches:
            color_dict[color] = max(color_dict[color], int(count))


        power = 1
        for count in color_dict.values():
            power *= count

        power_sum += power
            

    return power_sum

print(solve_1(games))
print(solve_2(games))

