# Maze

Constructs a square maze of given size via the following process:

1. Randomly generate a 2D character array where each space contains '0' or '.'

2. Parse the grid to find all pairs grid squares containing '0' that are adjacent to each other either horizonally or vertically.  

3. From the list of pairs, construct an adjacency-list graph that represents the possible steps one could take in the maze. 

4. Run a breadth-first search on the graph to find the shortest path from the top left corner of the maze to the bottom right corner. If there is no path, go back to step 1. 

This method is terribly inefficient and usually yields trivially easy mazes. The actual runtime with respect to given maze size is in the process of being calculated. 
