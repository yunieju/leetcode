class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        if not rooms:
            return
        rows, cols = len(rooms), len(rooms[0])
        q = []
        for i in range(rows):
            for j in range(cols):
                if rooms[i][j] == 0:
                    q.append((i,j))
        for row, col in q:
            d = rooms[row][col] + 1
            for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
                r = row + dx
                c = col + dy
                if 0 <= r < rows and 0 <= c < cols and rooms[r][c] == 2147483647:
                    rooms[r][c] = d
                    q.append((r,c))

        
