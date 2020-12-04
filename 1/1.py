with open('input.txt', 'r') as f:
    input_lines = [line.strip() for line in f]

def part_1(input_lines):
    print("Part 1")
    for i in range(0, len(input_lines)):
        # print(input_lines[i])
        for j in range(i, len(input_lines)):
            # print("j" + input_lines[j])
            if (int(input_lines[i]) + int(input_lines[j]) == 2020):
                print(int(input_lines[i]) * int(input_lines[j]))
                return
            else:
                pass


def part_2(input_lines):
    print("Part 2:")
    for i in range(0, len(input_lines)):
        for j in range(i, len(input_lines)):
            for k in range(j, len(input_lines)):
                if (int(input_lines[i]) + int(input_lines[j]) + int(input_lines[k]) == 2020):
                    print(int(input_lines[i]) * int(input_lines[j]) * int(input_lines[k]))
                    return
                else:
                    pass

part_1(input_lines)
part_2(input_lines)
