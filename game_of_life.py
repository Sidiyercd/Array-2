# Game of life
# Time Complexity: O(m*n)
# Space Complexity:  O(1)

# Count ones
# Time Complexity: O(1)
# Space Complexity: O(1)
class GameOfLife(object):

    def gameOfLife(self, board):

        m = len(board)
        if (board == None or m == 0):
            return
        n = len(board[0])

        for r in range(m):
            for c in range(n):
                countOnes = self.__countOnes(board, m, n, r, c)
                if (board[r][c] == 1 and (countOnes < 2 or countOnes > 3)):
                    board[r][c] = 2
                if (board[r][c] == 0 and countOnes == 3):
                    board[r][c] = -2

        for r in range(m):
            for c in range(n):
                if (board[r][c] == 2):
                    board[r][c] = 0
                if (board[r][c] == -2):
                    board[r][c] = 1

        return

    def __countOnes(self, board, m, n, r, c):

        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1],
                [-1, -1], [-1, 1], [1, -1], [1, 1]]
        count = 0

        for direction in dirs:
            row = r + direction[0]
            col = c + direction[1]
            if (row >= 0 and row < m and col >= 0 and col < n):
                if (board[row][col] == 1 or board[row][col] == 2):
                    count += 1

        return count
