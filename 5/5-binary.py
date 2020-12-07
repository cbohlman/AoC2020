with open('5.txt', 'r') as f:
    input_lines = [line.strip() for line in f]
    tickets = []
    for line in input_lines:
        line = line.replace('F','0')
        line = line.replace('B','1')
        line = line.replace('L','0')
        line = line.replace('R','1')
        ticket_id = int(line, 2)
        tickets.append(ticket_id)
    print('Part 1:')
    print(max(tickets))

    tickets.sort()
    for i in range(len(tickets)):
        if tickets[i] + 1 != tickets[i+1]:
            print(tickets[i] + 1)
            break