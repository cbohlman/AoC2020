import re
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

def count_bags(graph, color):
    count = 0
    inner = graph[color]
    for num, contained in inner:
        print(num, contained)
        # increment no. bags themselves
        count += num
        # increment no. of bags * contents of bags
        count += num * count_bags(graph, contained)
    return count


if (sys.argv[1] == 'test'):
    file_name = './7/7t.txt'
else:
    file_name = './7/7.txt'
with open(file_name,'r') as f:
    input_lines = [line.strip() for line in f]
    graph = build_graph(input_lines)
    # pp = pprint.PrettyPrinter(indent=4)
    # pp.pprint(graph)
    print(graph['shiny gold'])
    print(count_bags(graph, 'shiny gold'))