# final project for 2022 Spring Randomness and Computation
# Joanne Lee & Matt Ma

import numpy as np

class Number_Slide_Puzzle():

    # Joanne Lee
    # 0 is the blank spot, must end up in bottom right when board is solved
    def __init__(self):
        self.board = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,0]]
        self.empty_spot = (3,3)
        self.solved_board = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,0]]

    def is_solved(self):
        return self.board == self.solved_board

    # Matt Ma
    # slides the tile into empty position
    # variable tile is pair (coordinates)
    def slide(self, tile):
        if tile[1] != 0:
            left = (tile[0],tile[1]-1)
            if self.board[left[0]][left[1]] == 0:
                self.board[left[0]][left[1]] = self.board[tile[0]][tile[1]]
                self.board[tile[0]][tile[1]] = 0
                self.empty_spot = tile
        if tile[0] != 0:
            up = (tile[0]-1,tile[1])
            if self.board[up[0]][up[1]] == 0:
                self.board[up[0]][up[1]] = self.board[tile[0]][tile[1]]
                self.board[tile[0]][tile[1]] = 0
                self.empty_spot = tile
        if tile[0] != 3:
            down = (tile[0]+1, tile[1])
            if self.board[down[0]][down[1]] == 0:
                self.board[down[0]][down[1]] = self.board[tile[0]][tile[1]]
                self.board[tile[0]][tile[1]] = 0
                self.empty_spot = tile
        if tile[1] != 3:
            right = (tile[0], tile[1]+1)
            if self.board[right[0]][right[1]] == 0:
                self.board[right[0]][right[1]] = self.board[tile[0]][tile[1]]
                self.board[tile[0]][tile[1]] = 0
                self.empty_spot = tile
        return

    # Matt Ma
    # scrambling board
    def scramble(self, num_scrambles):
        count = 0
        tiles = []
        while count < num_scrambles:
            (empty_row, empty_col) = self.empty_spot
            tiles = []
            # not in top row
            if empty_row != 0:
                tiles.append((empty_row - 1, empty_col))
            # not in bottom row
            if empty_row != 3:
                tiles.append((empty_row + 1, empty_col))
            # not in left column
            if empty_col != 0:
                tiles.append((empty_row, empty_col - 1))
            # not in right column
            if empty_col != 3:
                tiles.append((empty_row, empty_col + 1))
            tile = tiles[np.random.randint(len(tiles))]
            self.slide(tile)
            count += 1

    # Joanne Lee
    # printing on terminal to test
    def print_board(self):
        print("")
        for i in range(4):
            nums = [""] * 4
            for j in range(4):
                number = self.board[i][j]
                num_spaces = 1 - (number // 10)
                spaces = " " * num_spaces
                nums[j] = f"{number}{spaces}"
            print(nums)
            print("")
