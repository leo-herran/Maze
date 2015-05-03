# Maze

Constructs a square maze of given size via the following process:

1. Randomly generate a 2D character array where each space contains '0' or '.'

2. Parse the grid to find all pairs of tuples (i, j) and (m, n) such that:

- 0 <= i, j, m, n < gridSize

- grid[i][j] and grid[m][n] both contain '0'.

- either (i+1, j), (i-1, j), (i, j+1), or (i, j-1) is equal to (m, n)

3. From the list of pairs, construct an adjacency-list graph that represents the possible steps one could take in the maze. 

4. Run a breadth-first search on the graph to find the shortest path from the top left corner of the maze to the bottom right corner. If there is no path, go back to step 1. 
