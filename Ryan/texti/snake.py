# Python3 program to find minimum number
# of dice throws required to reach last
# cell from first cell of a given
# snake and ladder board

# An entry in queue used in BFS
class Cell(object):
    def __init__(self, cell_num=0, dist=0):
        self.cell_num = cell_num
        self.dist = dist


'''This function returns minimum number of 
dice throws required to. Reach last cell 
from 0'th cell in a snake and ladder game. 
move[] is an array of size N where N is 
no. of cells on board. If there is no 
snake or ladder from cell i, then move[i] 
is -1. Otherwise move[i] contains cell to 
which snake or ladder at i takes to.'''


def getMinDiceThrows(boardSize, snakes, ladders):
    # orgnize the shortcuts; combin snakes and ladders
    temp = snakes + ladders
    shortcuts = {}
    for i in temp:
        index = i[0]
        value = i[1]
        shortcuts[index] = value

    # for shortest path, use BFS
    # create a queue
    queue = list()

    # init cell 1
    cell_1 = Cell(0, 0)
    queue.append(cell_1)

    # check board visit status, -1 for unvisited, 1 for visited
    cell_visited = [-1] * boardSize
    cell_visited[0] = 1

    res = Cell()
    while queue:
        res = queue.pop(0)
        cur_cell_num = res.cell_num
        # break when cur_cell is a cell away from destination
        if boardSize - cur_cell_num < 2:
            break

        # start to look for cells within a dice range
        next_cell = cur_cell_num + 1
        while boardSize - next_cell > 1 and next_cell - cur_cell_num <= 6:

            if cell_visited[next_cell] == -1:

                new_cell = Cell()
                new_cell.dist = res.dist + 1
                cell_visited[next_cell] = 1

                # check for shortcuts
                if next_cell in shortcuts.keys():
                    new_cell.cell_num = shortcuts[next_cell]
                else:
                    new_cell.cell_num = next_cell

                queue.append(new_cell)

            next_cell += 1

    return res.dist


def change(snakes, ladders):
    temp = snakes + ladders
    shortcuts = {}
    for i in temp:
        index = i[0]
        value = i[1]
        shortcuts[index] = value
    return shortcuts


N = 30
snakes = [[27, 1],
          [21, 9],
          [17, 4],
          [19, 7]]
ladders = [[11, 26],
           [3, 22],
           [5, 8],
           [20, 29]]

m = change(snakes, ladders)
print(getMinDiceThrows(N, snakes, ladders))
# driver code
N = 30
moves = [-1] * N

# Ladders
moves[2] = 21
moves[4] = 7
moves[10] = 25
moves[19] = 28

# Snakes
moves[26] = 0
moves[20] = 8
moves[16] = 3
moves[18] = 6

print(moves)
# print("Min Dice throws required is {0}".
#       format(getMinDiceThrows(moves, N)))

# This code is contributed by Ajitesh Pathak
