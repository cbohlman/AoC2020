with open('input.txt','r') as f:
    input_lines = [line.strip() for line in f]
    # [print(line.split(" ")) for line in input_lines]

def is_valid_part1(low, high, letter, password):
    count = password.count(letter)
    if (count >= low and count <= high):
        return True
    else:
        return False

def is_valid_part2(low, high, letter, password):
    if ((password[low - 1] == letter and password[high-1] != letter) or (password[low-1] != letter and password[high - 1] == letter)):
        return True
    else:
        return False


count1 = 0
count2 = 0

for line in input_lines:
    split = line.split(" ")
    low = int(split[0].split("-")[0])
    high = int(split[0].split("-")[1])
    letter = split[1][0]
    password = split[2]
    if (is_valid_part1(low, high, letter, password)):
        count1 += 1
    if (is_valid_part2(low, high, letter, password)):
        count2 += 1

print("Part 1:")
print(count1)
print("Part 2:")
print(count2)

