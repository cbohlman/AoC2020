ROWS = 128
COLUMNS = 8

def get_row(code, low, high, step, size):
    if code[step] == 'F':
        low = low
        high = high - int(size/2)
        # print(low, high)
        if low == high:
            return low
        return get_row(code, low, high, step + 1, int(size/2))
    elif code[step] == 'B':
        low = low + int(size/2)
        high = high
        # print(low, high)
        if low == high: 
            return high
        return get_row(code, low, high, step + 1, int(size/2))

def get_column(code, low, high, step, size):
    if code[step] == 'L':
        low = low 
        high = high -int(size/2)
        # print(low, high)
        if low == high:
            return low
        return get_column(code, low, high, step + 1, int(size/2))
    elif code[step] == 'R':
        low = low + int(size/2)
        high = high
        # print(low, high)
        if low == high:
            return high
        return get_column(code, low, high, step + 1, int(size/2))

class Ticket:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.id = self.row * 8 + self.column

id_list = []
with open('5.txt', 'r') as f:
    input_lines = [line.strip() for line in f]
    max_id = 0
    for line in input_lines:
        row_code = line[0:7]
        column_code = line[7:10]
        row = get_row(row_code, 0, ROWS - 1, 0, ROWS)
        column = get_column(column_code, 0, COLUMNS - 1, 0, COLUMNS)
        ticket_id = row * 8 + column
        id_list.append(ticket_id)
        if ticket_id > max_id:
            max_id = ticket_id
id_list.sort()
print('Part 1:')
print(max_id)
print('Part 2:')
for i in id_list:
    if id_list[i+1] != id_list[i] + 1:
        print(id_list[i] + 1)
        break
