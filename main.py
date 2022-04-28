import random


def random_state(height, width):
    """This function will take in 2 arguments
    your boards width and its height.
    ALIVE = 1; DEAD = 0
    :return
    """
    # Build the board using your previous work
    state = dead_state(width, height)

    # randomize each element of `state`  to either 0 or 1
    for i in range(len(state)):
        for j in range(len(state[i])):
            random_number = random.random()
            if random_number >= 0.39:
                state[i][j] = 0
            else:
                state[i][j] = 1

    return state


def dead_state(height, width):
    dead_state_grid = [[0 for x in range(height)] for x in range(width)]
    return dead_state_grid


def render(random_state):
    for i in range(len(random_state)):
        for j in range(len(random_state[i])):
            if random_state[i][j] == 1:
                random_state[i][j] = '#'
            elif random_state[i][j] == 0:
                random_state[i][j] = ' '
    for i in range(len(random_state)):
        random_state[i].append('|')
        random_state[i].insert(0, '|')
    print('- ' * (len(random_state) + 2))
    print('\n'.join([' '.join([str(cell) for cell in row]) for row in random_state]))
    print('- ' * (len(random_state) + 2))


# def next_board_state(initial_state):
#    for x in range(0, len(initial_state)):
#       for y in range(0, len(initial_state[0])):

# https://codereview.stackexchange.com/questions/62160/checking-for-neighbours-more-elegantly-in-conways-game-of-life
def count_neighbors(x, y, grid):
    """

    """
    # TODO: calculate the number of live
    # neighbors...

    alive = 0
    for row in range(3):
        for column in range(3):
            if x - 1 < 0 or x + 1 > len(grid) or y - 1 < 0 or y + 1 > len(grid):
                continue
            else:
                if grid[x, y] == 1:
                    alive += 1
    return alive


# render(random_state(5, 5))
print(count_neighbors(0, 0, random_state(3, 3)))
