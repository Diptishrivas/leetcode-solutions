class Solution(object):
    def orangesRotting(self, grid):
        
        rows=len(grid)
        cols=len(grid[0])

        q=deque()
        fresh=0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==2:
                   q.append((i,j))
                elif grid[i][j]==1:
                    fresh+=1
        minutes=0

        while q and fresh > 0:

            for _ in range(len(q)):

                r, c = q.popleft()

                directions = [
                    (r + 1, c),
                    (r - 1, c),
                    (r, c + 1),
                    (r, c - 1)
                ]

                for nr, nc in directions:

                    if (0 <= nr < rows and
                        0 <= nc < cols and
                        grid[nr][nc] == 1):

                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr, nc))

            minutes += 1

        if fresh > 0:
            return -1

        return minutes