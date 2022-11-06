"""Chapter 2 - Containers"""


def mark_coordinate(grid, coord):
    if 0 <= coord.x < grid.width and 0 <= coord.y < grid.height:
        grid[coord] = 1

    if coord in grid:
        grid[coord] = 1


class Boundaries:
    def __init__(self, width, height):
        self.width = width
        self.height = heigh

    # 'value' in boundaries
    def __contains__(self, coord): #bool
        x, y = coord
        return 0 <= x < self.width and 0 <= y < self.height


class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.limits = Boundaries(width, height)

    # 'value' in boundaries
    def __contains__(self, coord):
        return coord in self.limits