# AI Grid Pathfinder
>A 2D grid pathfinding agent that uses AI search algorithms to navigate from point A to point B while avoiding obstacles and considering terrain costs.

## Features
This project uses a path finding agent that implements different search algorithms to go from a starting point to a end point.
The grid world is defined by the txt files in TestingGrid folder.
This project consists of the following files:
    search.py: Main script to run the program
    grid.py: Defines the grid and visualizaton
    utils.py: Contains data structures for use
    collisions.py: Defines how obstables are handled
    bfs.py: Implements breadth first search for pathfinding
    dfs.py: Implements depth first search for pathfinding
    gbfs.py: Implements greedy best firsth search for pathfinding
    astar.py: Implements A* search for pathfinding

This project uses the following python libraries:
    math
    matplotlib
    heapq
    
## Breadth First Search (BFS)

## Depth First Search (DFS)

## Greedy Best First Search (GBFS)

## A-star Search (A*)



## How to Run
Clone this repository
```bash
git clone https://github.com/DavidSchineis/AI-Grid-Pathfinder.git
```

Ensure Python 3.11+ is installed and install required libraries:
```bash
pip install -r assets/requirements.txt
```

Run the simulation:
```bash
python3 main.py
```
