# AI Grid Pathfinder
>A 2D grid pathfinding agent that uses AI search algorithms to navigate from point A to point B while avoiding obstacles and considering terrain costs.

## Features
* Modular implementations of BFS, DFS, GBFS, and A* algorithms for pathfinding.
* Real-time visualization using Matplotlib, with path rendering and keyboard exit controls (q, ESC).
* Polygon-based spatial detection for enclosures and turfs, with polygon, edge, and corner checks.
* Weighted movement costs applied per step, with extra cost when crossing turf.
* Grid world is defined by txt files supporting custom enclosure and turf geometry.

## Breadth First Search (BFS)
<p align="center">
  <img src="assets/BFS2.png" alt="BFS Example" width="300">
</p>

## Depth First Search (DFS)
<p align="center">
  <img src="assets/DFS2.png" alt="BFS Example" width="300">
</p>

## Greedy Best First Search (GBFS)
<p align="center">
  <img src="assets/GBFS2.png" alt="BFS Example" width="300">
</p>

## A-star Search (A*)
<p align="center">
  <img src="assets/A*2.png" alt="BFS Example" width="300">
</p>

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
