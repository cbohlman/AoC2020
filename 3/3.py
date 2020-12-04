with open('input.txt', 'r') as f:
    input_lines = [line.strip() for line in f]

width = len(input_lines[0])

def count_trees(input_lines, x_slope, y_slope):
    tree_count = 0
    for i in range(0, len(input_lines), y_slope):
        # print("x: ", int(i*x_slope/y_slope) % width, "y: ", i)
        if (input_lines[i][int(i*x_slope/y_slope)% width] == '#'):
            tree_count += 1
    return tree_count


# count_trees(input_lines, 1, 2)

# Part 1
print("Part 1:")
print(count_trees(input_lines, 3, 1))

# Part 2
x_slopes = [1,3,5,7,1]
y_slopes = [1,1,1,1,2]
out = 1

print("Part 2:")
for i in range(len(x_slopes)):
    out *= count_trees(input_lines, x_slopes[i], y_slopes[i])
    print(count_trees(input_lines, x_slopes[i], y_slopes[i]))
print(out)
