# tarting in the top left corner of a 2×2 grid, and only being able to move to the right and
# down, there are exactly 6 routes to the bottom right corner.


# How many such routes are there through a 20×20 grid?


class OutOfBoundsError(Exception):
    """Exception raised when going to far in the array"""
    pass


class LatticePaths:
    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.y_position = 0
        self.x_position = 0

    def move_down(self):
        if self.y_position <= self.grid_size:
            self.y_position = self.y_position + 1
        else:
            raise OutOfBoundsError("You went out of the grid !")

    def move_right(self):
        if self.x_position <= self.grid_size:
            self.x_position = self.x_position + 1
        else:
            raise OutOfBoundsError("You went out of the grid !")

# At this moment I realized there was a way to get this with a simple
# combination math calculus 20 among 40 -> 137846528820
