#
# Difficulty Level: MEDIUM
#
# You start at the cell (rStart, cStart) of an rows x cols grid facing east.
# The northwest corner is at the first row and column in the grid,
# and the southeast corner is at the last row and column.
#
# You will walk in a clockwise spiral shape to visit every position in this grid.
# Whenever you move outside the grid's boundary, we continue our walk outside
# the grid (but may return to the grid boundary later.).
# Eventually, we reach all rows * cols spaces of the grid.
#
# Return an array of coordinates representing the positions of the grid in the order you visited them.
#

class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        ans = [[rStart, cStart]]
        count = (rows * cols) - 1
        
        row, col = rStart, cStart
        steps = 1

        while count > 0:
            movements = [(0, 1), (1, 0), (0, -1), (-1, 0)]

            for move in movements:
                for i in range(steps):
                    row += move[0]
                    col += move[1]

                    if 0 <= row < rows and 0 <= col < cols:
                        ans.append([row, col])
                        count -= 1

                if move == (1, 0) or move == (-1, 0):
                    steps += 1

        return ans