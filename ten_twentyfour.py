from random import randint, random
import copy
game_board = [[None for cell in range(4)] for row in range(4)]
GAME_SCORE = 0
GAME_OVER = False


def spawn_number():
    # pick a random spot on the board
    random_row = randint(0, 3)
    random_col = randint(0, 3)
    # determine if it's available for spawning
    if not game_board[random_row][random_col]:
        if random() > 0.9:
            new_tile = 4
        else:
            new_tile = 2
        game_board[random_row][random_col] = new_tile
        return True
    else:
        return False


def move_right():
    """ Move all tiles to the right and process scoring """
    global GAME_SCORE
    for row in game_board:
        # Sort the row with None as 0 and all tiles as 1
        # Sort is stable and so tiles stay in order
        row.sort(key=lambda x: 0 if x is None else 1)
        # Iterate backwards over list to find identical tiles and combine
        # Insert blank tiles at beginning of list
        for cell_index in range(3, 0, -1):
            if row[cell_index] and row[cell_index] == row[cell_index-1]:
                # if the cell is not None and equal in value to the cell to its left
                # combine the values
                row[cell_index] *= 2
                # add the combined value to the total score
                GAME_SCORE += row[cell_index]
                # remove the combined cell
                row.pop(cell_index-1)
                # insert a blank cell at the beginning of the row
                row.insert(0, None)


def move_left():
    """ Move all tiles to the left and process scoring """
    global GAME_SCORE
    for row in game_board:
        # Sort the row with None as 0 and all tiles as 1, reversed
        # Sort is stable and so tiles stay in order
        row.sort(key=lambda x: 0 if x is None else 1, reverse=True)
        # Iterate over list to find identical tiles and combine
        # Insert blank tiles at beginning of list
        for cell_index in range(3):
            if row[cell_index] and row[cell_index] == row[cell_index+1]:
                # if the cell is not None and equal in value to the cell to its right
                # combine the values
                row[cell_index] *= 2
                # add the combined value to the total score
                GAME_SCORE += row[cell_index]
                # remove the combined cell
                row.pop(cell_index + 1)
                # insert a blank cell at the end of the row
                row.append(None)


def move_down():
    """ Move all tiles down and process scoring """
    global GAME_SCORE
    for col_index in range(4):
        vertical_row = []
        for row_index in range(4):
            # We convert each column to a list for ease of processing
            vertical_row.append(game_board[row_index][col_index])
        # Sort the row with None as 0 and all tiles as 1
        # Sort is stable and so tiles stay in order
        vertical_row.sort(key=lambda x: 0 if x is None else 1)
        # Iterate backwards over list to find identical tiles and combine
        # Insert blank tiles at beginning of list
        for cell_index in range(3, 0, -1):
            if vertical_row[cell_index] and vertical_row[cell_index] == vertical_row[cell_index - 1]:
                # if the cell is not None and equal in value to the cell above it
                # combine the values
                vertical_row[cell_index] *= 2
                # add the combined value to the total score
                GAME_SCORE += vertical_row[cell_index]
                # remove the combined cell
                vertical_row.pop(cell_index - 1)
                # insert a blank cell at the beginning of the row
                vertical_row.insert(0, None)
        for row_index in range(4):
            # We convert each processed list back into the column
            game_board[row_index][col_index] = vertical_row[row_index]


def move_up():
    """ Move all tiles up and process scoring """
    global GAME_SCORE
    for col_index in range(4):
        vertical_row = []
        for row_index in range(4):
            # We convert each column to a list for ease of processing
            vertical_row.append(game_board[row_index][col_index])
        # Sort the row with None as 0 and populated tiles as 1, reversed
        # Sort is stable and so tiles stay in order
        vertical_row.sort(key=lambda x: 0 if x is None else 1, reverse=True)
        # Iterate over list to find identical tiles and combine
        # Insert blank tiles at beginning of list
        for cell_index in range(3):
            if vertical_row[cell_index] and vertical_row[cell_index] == vertical_row[cell_index + 1]:
                # if the cell is not None and equal in value to the cell below it
                # combine the values
                vertical_row[cell_index] *= 2
                # add the combined value to the total score
                GAME_SCORE += vertical_row[cell_index]
                # remove the combined cell
                vertical_row.pop(cell_index + 1)
                # insert a blank cell at the end of the row
                vertical_row.append(None)
        for row_index in range(4):
            # We convert each processed list back into the column
            game_board[row_index][col_index] = vertical_row[row_index]


def is_game_over():
    """ Determines whether the game is over by first checking
        if the board is full, then checking whether any moves
        remain """
    if not is_board_full():
        # If there are empty cells, the game can continue
        return False
    # The game board is full and we must evaluate if there are moves
    for row_index in range(4):
        for col_index in range(4):
            # Create list of all adjacent values
            adjacents = []
            if row_index-1 > 0:
                adjacents.append(game_board[row_index-1][col_index])
            if row_index+1 < 4:
                adjacents.append(game_board[row_index+1][col_index])
            if col_index-1 > 0:
                adjacents.append(game_board[row_index][col_index-1])
            if col_index+1 < 4:
                adjacents.append(game_board[row_index][col_index+1])
            # Test if tile value is in an adjacent cell, meaning play can continue
            if game_board[row_index][col_index] in adjacents:
                return False
    return True


def is_board_full():
    """ Checks each row for empty cells """
    for row in game_board:
        if None in row:
            return False
    return True


def play_game(move):
    global GAME_OVER
    state_change = True
    prev_game_board = copy.deepcopy(game_board)
    if move == 'up':
        move_up()
    elif move == 'right':
        move_right()
    elif move == 'down':
        move_down()
    elif move == 'left':
        move_left()
    if prev_game_board == game_board:
        state_change = False
    if state_change and not is_board_full():
        # As long a space is available and the board has changed, we want to add a piece
        while not spawn_number():
            pass
    if is_game_over():
        GAME_OVER = True

def main():
    pass

def game_board_setup():
    global game_board
    global GAME_SCORE
    global GAME_OVER
    game_board = [[None for cell in range(4)] for row in range(4)]
    GAME_SCORE = 0
    GAME_OVER = False
    spawn_number()
    spawn_number()

if __name__ == "__main__":
    # execute only if run as a script
    main()