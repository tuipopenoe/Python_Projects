# Tui Popenoe
# Adjacent Grid

def getAdjacentWrapCount(grid, x, y, X, Y, char):
    """Get the adjacent grid spaces for a grid space located at grid[x][y] in a
    grid of size X by Y. char represents a marked grid space """
    count = 0
    # X, % Y gets spaces that are wrapped around the grid 
    # Get x coordinates for adjacent grid spaces
    for i in [(x-1) % X, x, (x+1) % X]:
        # Get y coordinates for adjacent grid 
        for j in [(y-1) % Y, y, (y+1) % Y]:
            # if the grid space is present and not the center of the grid spaces
            if (i, j) != (x, y) and grid[i][j] == char:
                count += 1
    return count

def getAdjacentCount(grid, x, y, X, Y, char):
    """ Gets the adjacent grid spaces for a grid space located at grid[x][y] in a grid of size X by Y. char represents a marked grid space."""
    count = 0
    try{
        if x == 0:

        if y == 0:

        if x == X-1:

        if y == Y-1:
    }
