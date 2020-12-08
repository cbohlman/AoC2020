import sys
import pprint

def build_graph(input_lines):
    g = dict()
    for line in input_lines:
        s = line.split(' bags contain ')
        parent = s[0]
        right = s[1].split(', ')
        colors = []
        for rule in right:
            if 'no other bags' not in rule:
                num = int(rule[0])
                color = rule[2:].split(' bag')[0]
                colors.append((num,color)) 
        g[parent] = colors
    return g

def contains_bag(graph, colors, alls):
    direct = set()
    if len(colors) == 0:
        return
    else:
        for color in colors:
            for g in graph:
                if color in [x[1] for x in graph[g]]:
                    direct.add(g)
                    alls.add(g)
    return contains_bag(graph, direct, alls)

def count_bags(graph, color):
    count = 0
    inner = graph[color]
    for num, contained in inner:
        # increment no. bags themselves
        count += num
        # increment no. of bags * contents of bags
        count += num * count_bags(graph, contained)
    return count

def print_bags(graph, color, level):
    inner = graph[color]
    for _, contained in inner:
        print(level * '--', contained)
        print_bags(graph, contained, level + 1)
    return


if (sys.argv[1] == 'test'):
    file_name = './7/7t.txt'
else:
    file_name = './7/7.txt'
with open(file_name,'r') as f:
    input_lines = [line.strip() for line in f]
    graph = build_graph(input_lines)
    
    # Part 1
    root = set(['shiny gold'])
    alls = set()
    contains_bag(graph, root, alls)
    print('Part 1:')
    print(len(alls))

    print('Part 2:')
    print(count_bags(graph, 'shiny gold'))
    # Optional function to print bag topography
    # print_bags(graph, 'shiny gold', 0)