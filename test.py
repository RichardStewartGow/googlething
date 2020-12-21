class MazeSolution:
    prison = [0, 0]
    height = 0
    width = 0

    def handle(self, grid):
        # Keep it as row, column instead of x, y
        self.height = len(grid)
        self.width = len(grid[0])
        pod = [self.height - 1, self.width - 1]

        # No walls
        shortest_no_wall = self.bfs_shortest_path(grid, pod)

        # One wall
        walls = [[r, c] for r, row in enumerate(grid) for c, val in enumerate(row) if val == 1]
        start_to_wall = [self.bfs_shortest_path(grid, wall) for wall in walls]
        goal_to_wall = [self.bfs_shortest_path(grid, pod, wall) for wall in walls]
        total_one_wall = [sum(x) - 1 for x in zip(start_to_wall, goal_to_wall)]

        shortest_one_wall = min(total_one_wall)

        return (min(shortest_one_wall, shortest_no_wall))

    # finds shortest path between 2 nodes of a graph using BFS
    def bfs_shortest_path(self, grid, goal, modifiedStart = None):
        start = modifiedStart if modifiedStart else self.prison;

        # keep track of explored nodes
        explored = []
        # keep track of all the paths to be checked
        queue = [[start]]

        # return path if start is goal
        if start == goal:
            return 1

        # keeps looping until all possible paths have been checked
        while queue:
            # pop the first path from the queue
            path = queue.pop(0)
            # get the last node from the path
            node = path[-1]
            if node not in explored:
                r, c = node
                neighbours = [[r - 1, c], [r + 1, c], [r, c - 1], [r, c + 1]]
                neighbours = [n for n in neighbours if n[0] >= 0 and n[0] < self.height and n[1] >= 0 and n[1] < self.width]
                # go through all neighbour nodes, construct a new path and
                # push it into the queue
                for neighbour in neighbours:
                    if grid[neighbour[0]][neighbour[1]] == 0 or neighbour == goal:
                        new_path = list(path)
                        new_path.append(neighbour)
                        queue.append(new_path)
                        # return path if neighbour is goal
                        if neighbour == goal:
                            return len(new_path)

                # mark node as explored
                explored.append(node)

        # in case there's no path between the 2 nodes
        return float("inf")


solution = MazeSolution()
testgrid1 = [[0, 0, 0, 0, 1], [0, 1, 0, 1, 1], [0, 0, 1, 1, 1], [1, 1, 0, 1, 0]]

print(solution.handle(testgrid1))