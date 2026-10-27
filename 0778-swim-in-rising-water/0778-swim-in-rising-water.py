class Solution(object):
    def swimInWater(self, grid):
        import heapq

        n = len(grid)
        heap = [(grid[0][0], 0, 0)]
        heapq.heapify(heap)

        visited = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while heap:
            water, r, c = heapq.heappop(heap)

            if (r, c) in visited:
                continue

            visited.add((r, c))

            if r == n - 1 and c == n - 1:
                return water

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < n and 0 <= nc < n:
                    if (nr, nc) not in visited:
                        new_water = max(water, grid[nr][nc])
                        heapq.heappush(heap, (new_water, nr, nc))

        return -1
