# Maze

maze.py constructs a square maze of given size via the following process:

1. Randomly generate a 2D integer array where each space contains 0 or 1. 

2. Parse the grid to find all pairs grid squares containing 0 that are adjacent to each other either horizonally or vertically.  

3. From the list of pairs, construct an adjacency-list graph that represents the possible steps one could take in the maze. 

4. Run a breadth-first search on the graph to find the shortest path from the top left corner of the maze to the bottom right corner. If there is no path, go back to step 1. 

This method is terribly inefficient and usually yields trivially easy mazes, as generating them in this way often causes chunks of the maze to be unreachable. The actual runtime with respect to given maze size is in the process of being calculated. 

Some examples are given below. 

![alt text](http://i.imgur.com/ONW7g38.png "Maze of size four.")

![alt text](http://i.imgur.com/wVQiApT.png "Maze of size eight")

![alt text](http://i.imgur.com/ChSEtRY.png "Maze of size ten.")

betterMaze.py takes advantage of the fact that one can generate much better mazes with the same int[][] representation. If one sees a 0 in a grid square, this means there is no wall directly above it, but there is a wall to the left of it. The opposite holds for 1s. The only exception is that the top left square must have no walls to the south and east, every square on the top row must not have a wall to the west, and every square on the left column must not have a wall to the north. 

Examples are given below. 

![alt text](http://i.imgur.com/opyFy6S.png "Better maze of size four.")

![alt text](http://i.imgur.com/lbB5rX4.png "Better maze of size eight.")

![alt text](http://i.imgur.com/Z265I6f.png "Better maze of size ten.")

One nice thing about this implementation is that as long as the maze representation follows the aforementioned rules, there will always be a path from the top left corner to the bottom right corner. This is because the graph representation of the maze can be interpreted as a random binary tree where the root is the top left corner, the left child of a node is the square to the south, and the right child is the square to the east. It's clear that since the end of the maze is a leaf node in the binary tree, there is always a path to the root. 
