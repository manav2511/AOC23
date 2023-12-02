import re

# Read input
with open("input.txt", "r") as inp:
   calib_values = inp.read().split("\n")

# Part 1
def add_calib_values(data):
    sum = 0
    for s in data:
        left = -1
        right = -1

        for i in range(len(s)):
            if s[i].isdigit():
                if left == -1:
                    left = i
                right = i
        
        print(s)
        print(s[left]+s[right])
        sum += int(s[left]+s[right])

    print(sum)

# Part 2

new_data = []
for s in calib_values:
    s = s.replace("one", "one1one") \
    .replace("two", "two2two") \
    .replace("three", "three3three") \
    .replace("four", "four4four") \
    .replace("five", "five5five") \
    .replace("six", "six6six") \
    .replace("seven", "seven7seven") \
    .replace("eight", "eight8eight") \
    .replace("nine", "nine9nine")

    new_data.append(s)


add_calib_values(new_data)
    