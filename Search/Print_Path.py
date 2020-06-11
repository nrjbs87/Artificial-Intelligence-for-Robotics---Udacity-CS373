 # ----------
# User Instructions:
# 
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space


grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

def search(grid,init,goal,cost):

    closed = [[0] * len(grid[0]) for i in range(len(grid))]
    closed[init[0]][init[1]] = 1

    actions = [[99] * len(grid[0]) for i in range(len(grid))]

    x = init[0]
    y = init[1]
    g = 0

    counter = 0

    open = [[g, x, y]]

    cantMove = False
    solFound = False

    while cantMove == False and solFound == False:
        if len(open) == 0:
            cantMove = True
        else:
            open.sort()
            next = open.pop(0)
            g = next[0]
            x = next[1]
            y = next[2]

            if (x == goal[0] and y == goal[1]):
                solFound = True
            else:
                for i in range(len(delta)):
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]
                    if x2 < len(grid) and x2 >= 0 and y2 < len(grid[0]) and y2 >= 0:
                        if closed[x2][y2] != 1 and grid[x2][y2] != 1:
                            g2 = g + 1
                            open.append([g2, x2, y2])
                            closed[x2][y2] = 1
                            counter += 1
                            actions[x2][y2] = i


    path = [[' '] * len(grid[0]) for i in range(len(grid))]
    path[goal[0]][goal[1]] = '*'
    x = goal[0]
    y = goal[1]    
    while x != init[0] or y != init[1]:
        x2 = x - delta[actions[x][y]][0]
        y2 = y - delta[actions[x][y]][1]
        path[x2][y2] = delta_name[actions[x][y]]
        x = x2
        y = y2
    
    for i in range(len(path)):
        print(path[i])




    return path

search(grid,init,goal,cost)
