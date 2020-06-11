# ----------
# User Instructions:
# 
# Create a function compute_value which returns
# a grid of values. The value of a cell is the minimum
# number of moves required to get from the cell to the goal. 
#
# If a cell is a wall or it is impossible to reach the goal from a cell,
# assign that cell a value of 99.
# ----------

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1 # the cost associated with moving from a cell to an adjacent one

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

def compute_value(grid,goal,cost):
    value = [[99] * len(grid[0]) for i in range(len(grid))]
    value[goal[0]][goal[1]] = 0

    x = goal[0]
    y = goal[1]
    v = 0
    cost = 1

    open = [[v, x, y]]

    while len(open) != 0:
        open.sort()
        next = open.pop(0)
        for i in range(len(delta)):
            x2 = next[1] - delta[i][1]
            y2 = next[2] - delta[i][0]
            if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]):
                if grid[x2][y2] == 0 and value[x2][y2] == 99:
                    open.append([next[0]+cost, x2, y2])
                    value[x2][y2] = next[0] + cost
        
    for i in range(len(value)):
        print(value[i])


    return value

compute_value(grid,goal,cost)