# ----------
# User Instructions:
# 
# Implement the function optimum_policy2D below.
#
# You are given a car in grid with initial state
# init. Your task is to compute and return the car's 
# optimal path to the position specified in goal; 
# the costs for each motion are as defined in cost.
#
# There are four motion directions: up, left, down, and right.
# Increasing the index in this array corresponds to making a
# a left turn, and decreasing the index corresponds to making a 
# right turn.

forward = [[-1,  0], # go up
           [ 0, -1], # go left
           [ 1,  0], # go down
           [ 0,  1]] # go right
forward_name = ['up', 'left', 'down', 'right']

# action has 3 values: right turn, no turn, left turn
action = [-1, 0, 1]
action_name = ['R', '#', 'L']

# EXAMPLE INPUTS:
# grid format:
#     0 = navigable space
#     1 = unnavigable space 
grid = [[1, 1, 1, 0, 0, 0],
        [1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1]]

init = [4, 3, 0] # given in the form [row,col,direction]
                 # direction = 0: up
                 #             1: left
                 #             2: down
                 #             3: right
                
goal = [2, 0] # given in the form [row,col]

cost = [2, 1, 1] # cost has 3 values, corresponding to making 
                  # a right turn, no turn, and a left turn

# EXAMPLE OUTPUT:
# calling optimum_policy2D with the given parameters should return 
# [[' ', ' ', ' ', 'R', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', '#'],
#  ['*', '#', '#', '#', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', ' '],
#  [' ', ' ', ' ', '#', ' ', ' ']]
# ----------

# ----------------------------------------
# modify code below
# ----------------------------------------

def optimum_policy2D(grid,init,goal,cost):

    value = [[[999 for facing in range(len(forward))]\
    for col in range(len(grid[0]))]\
    for row in range(len(grid))]
    policy = [[[' ' for facing in range(len(forward))]\
    for col in range(len(grid[0]))]\
    for row in range(len(grid))]
    policy2D = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]
  
    change = True

    while change:
        change = False
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                for o in range(len(forward)):
                    if x == goal[0] and y == goal[1]:
                        if value[x][y][o] > 0:
                            value[x][y][o] = 0
                            policy[x][y][o] = '*'
                            change = True

                    elif grid[x][y] == 0:
                        for f2 in range(len(action)):
                            o2 = (o + action[f2]) % 4
                            x2 = x + forward[o2][0]
                            y2 = y + forward[o2][1]
                            

                            if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]) and grid[x2][y2] == 0:
                                v2 = value[x2][y2][o2] + cost[f2]
                                if v2 < value[x][y][o]:
                                    value[x][y][o] = v2
                                    policy[x][y][o] = action_name[f2]
                                    change = True
        

    x = init[0]
    y = init[1]
    o = init[2]
    policy2D[x][y] = policy[x][y][o]

    while policy[x][y][o] != '*':
        if policy[x][y][o] == '#':
            o2 = o
        elif policy[x][y][o] == 'R':
            o2 = (o-1) % 4
        elif policy[x][y][o] == 'L':
            o2 = (o+1) % 4
        x = x + forward[o2][0]
        y = y + forward[o2][1]

        o = o2
        policy2D[x][y] = policy[x][y][o]

    for i in range(len(policy2D)):
        print(policy2D[i])

optimum_policy2D(grid,init,goal,cost)