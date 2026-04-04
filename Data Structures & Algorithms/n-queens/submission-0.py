class Solution:
    def solveNQueens(self, n):
        result = []

        def is_valid(row, col, current):
            # check col
            for i in range(n):
                if current[i][col] == 'Q': return False
            # check 4 diagonals
            for x,y in [(1,1),(1,-1),(-1,-1),(-1,1)]:
                newx, newy = row, col
                while 0<=newx+x<n and 0<=newy+y<n:
                    newx+=x; newy+=y
                    if current[newx][newy]=='Q': return False
            return True

        def backtrack(row, current):
            if row == n:                                      # all rows filled
                result.append(["".join(r) for r in current]) # snapshot
                return
            for col in range(n):                             # try every column
                if is_valid(row, col, current):
                    current[row][col] = 'Q'                  # PUT ON
                    backtrack(row+1, current)                 # GO DEEP
                    current[row][col] = '.'                  # TAKE OFF

        current = [['.']*n for _ in range(n)]
        backtrack(0, current)
        return result