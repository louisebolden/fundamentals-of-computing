"""
Clone of 2048 game.
"""

import poc_2048_gui
import poc_simpletest as simpletest
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """

    # create a list of zeros, the same length
    # as line
    result = [0] * len(line)

    # iterate through the nums in line, adding
    # any non-zeros to result and allowing each
    # num to be merged once with a previous num
    # if they are identical
    result_pos = 0
    prev_merged = False

    for num in line:
        # skip zeros in line because result already
        # contains zeros
        if num != 0:

            # if we're at the 2nd num or later, and
            # didn't do a merge on the last num, then
            # attempt a merge of this num
            if result_pos > 0 and not prev_merged:
                prev_num = result[result_pos-1]

                # can only merge identical nums...
                if num == prev_num:
                    result[result_pos-1] = num + prev_num

                    # set prev_merged flag to ensure
                    # a merge is never attempted more
                    # than once on each num
                    prev_merged = True

                else:
                    result[result_pos] = num
                    result_pos += 1

                    prev_merged = False

            else:
                result[result_pos] = num
                result_pos += 1

                prev_merged = False

    return result

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        # set initial height and width of game grid
        self._grid_height = grid_height
        self._grid_width = grid_width

        # store lists of indices for each edge of the
        # game grid, to help us later build lists of
        # values to pass into the merge function
        height_range = range(self.get_grid_height())
        width_range = range(self.get_grid_width())
        self._initial_indices = {
            UP: [(0, w) for w in width_range],
            DOWN: [(len(height_range)-1, w) for w in width_range],
            LEFT: [(h, 0) for h in height_range],
            RIGHT: [(h, len(width_range)-1) for h in height_range]
        }

        # populate the game's cells with zeros and
        # two initial random numbers
        self.reset()

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self._cells = [[0 for dummy_col in range(self.get_grid_width())] for dummy_row in range(self.get_grid_height())]
        self.new_tile()
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        result = "GRID:\n\n"
        for row in self._cells:
            for col in row:
                result += str(col) + " "
            result += "\n"
        return result

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """

        # depending on the direction, check the list of initial indices
        # and use these to create new lists of each row OR col of values
        # that begins at each initial index and ends at the other side
        # of the grid
        initial_indices = self._initial_indices[direction]
        offset = OFFSETS[direction]

        # knowing how many cells are in the row OR col that we need
        # to collect values from is pretty essential for the inner
        # loops below
        cell_range = range(self.get_grid_height() if direction == UP or direction == DOWN else self.get_grid_width())

        # we must keep track of whether or not the board has changed,
        # in order to know whether to add a new tile at the end of
        # the move
        board_changed = False

        for tile_loc in initial_indices:
            # we want to build a list of values to merge
            merge_vals = []

            # (we need a mutable location to adjust by our offset
            # during each loop through our cell_range numbers)
            temp_loc = [tile_loc[0], tile_loc[1]]

            for num in cell_range:
                merge_vals.append(self.get_tile(temp_loc[0], temp_loc[1]))

                temp_loc[0] = temp_loc[0] + offset[0]
                temp_loc[1] = temp_loc[1] + offset[1]

            # we can now get the result of merging those values
            merge_result = merge(merge_vals)

            # and update the grid to reflect the now-merged cells
            # (resetting temp_loc for use in this new loop)
            temp_loc = [tile_loc[0], tile_loc[1]]

            for num in cell_range:
                old_val = self.get_tile(temp_loc[0], temp_loc[1])
                new_val = merge_result[num]

                if old_val != new_val:
                    self.set_tile(temp_loc[0], temp_loc[1], new_val)
                    board_changed = True

                temp_loc[0] = temp_loc[0] + offset[0]
                temp_loc[1] = temp_loc[1] + offset[1]

        # add a new tile to the board if it changed during this move
        if board_changed:
            self.new_tile()

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """

        # find a random value from 1-10 and if we get
        # 1-9 (90% of the time) then our rand_val is 2
        # - otherwise, our rand_val will be 4
        rand_val = 2 if random.randrange(1, 11) <= 9 else 4

        # create ranges to represent each row and col index,
        # and then shuffle them for random cell selection
        rows = range(0, self.get_grid_height())
        cols = range(0, self.get_grid_width())
        random.shuffle(rows)
        random.shuffle(cols)

        # if we can find a cell with a value of zero,
        # then update its value with our rand_val
        for row in rows:
            for col in cols:
                cell_val = self._cells[row][col]
                if cell_val == 0:
                    self._cells[row][col] = rand_val
                    return

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._cells[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self._cells[row][col]

poc_2048_gui.run_gui(TwentyFortyEight(4, 4))


# Test suite for merge function & TwentyFortyEight class

tester = simpletest.TestSuite()

tester.run_test(merge([2, 0, 2, 4]), [4, 4, 0, 0])
tester.run_test(merge([0, 0, 2, 2]), [4, 0, 0, 0])
tester.run_test(merge([2, 2, 0, 0]), [4, 0, 0, 0])
tester.run_test(merge([2, 2, 2, 2, 2]), [4, 4, 2, 0, 0])
tester.run_test(merge([8, 16, 16, 8]), [8, 32, 8, 0])

game = TwentyFortyEight(5,7)
print game

tester.run_test(game.get_grid_height(), 5)
tester.run_test(game.get_grid_width(), 7)

tester.run_test(game._initial_indices[UP], [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6)])
tester.run_test(game._initial_indices[DOWN], [(4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6)])
tester.run_test(game._initial_indices[LEFT], [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)])
tester.run_test(game._initial_indices[RIGHT], [(0, 6), (1, 6), (2, 6), (3, 6), (4, 6)])

game.move(DOWN)
print game

tester.report_results()
