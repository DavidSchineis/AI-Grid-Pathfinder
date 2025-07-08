# Main

# Import libraries
import matplotlib.pyplot as plt
from utils import *
from grid import *
from collisions import *
from bfs import breadth_first_search
from dfs import depth_first_search
from gbfs import greedy_best_first_search
from astar import astar

# Generates polygons from file
def gen_polygons(worldfilepath):
    polygons = []
    with open(worldfilepath, "r") as f:
        lines = [line.strip() for line in f.readlines()]
        for line in lines:
            polygon = []
            pts = line.split(';')
            for pt in pts:
                xy = pt.split(',')
                polygon.append(Point(int(xy[0]), int(xy[1])))
            polygons.append(polygon)
    return polygons

# Flag to control early exit
exit_requested = False

# Close matplot window on 'q' or 'ESC'
def on_key(event):
    global exit_requested
    if event.key in ['q', 'escape']: 
        exit_requested = True
        plt.close()  

# Draws algorithm path
def draw_path(fig, ax, res_path, algo_name):
    print(f"Running {algo_name}...")
    for i in range(len(res_path)-1):
        draw_result_line(ax, [res_path[i].x, res_path[i+1].x], [res_path[i].y, res_path[i+1].y])
        plt.pause(0.01)
    plt.show()

# Draws entire figure, grid, and pathfinding algorithm  
def draw_algorithm(choice, source, dest, epolygons, tpolygons):
    algorithms = {
        "BFS": breadth_first_search,
        "DFS": depth_first_search,
        "GBFS": greedy_best_first_search,
        "A*": astar
    }
    
    # Input check
    if choice not in algorithms:
        print("Invalid choice. Please select BFS, DFS, GBFS, or A*.")
        return
    
    # Draw grid and points
    fig, ax = plt.subplots(figsize=(8, 8))
    draw_grids(ax)
    draw_source(ax, source.x, source.y)
    draw_dest(ax, dest.x, dest.y)
    
    # Draw enclosure polygons
    for polygon in epolygons:
        fill_polygon(ax, polygon, color="black")
        for p in polygon:
            draw_point(ax, p.x, p.y)
        for i in range(len(polygon)):
            draw_line(ax, [polygon[i].x, polygon[(i+1)%len(polygon)].x], [polygon[i].y, polygon[(i+1)%len(polygon)].y])
    
    # Draw turf polygons
    for polygon in tpolygons:
        fill_polygon(ax, polygon, color="green")
        for p in polygon:
            draw_green_point(ax, p.x, p.y)
        for i in range(len(polygon)):
            draw_green_line(ax, [polygon[i].x, polygon[(i+1)%len(polygon)].x], [polygon[i].y, polygon[(i+1)%len(polygon)].y])
    
    # Draw algorithm
    algo = algorithms[choice]
    path = algo(source, dest, epolygons, tpolygons)
    draw_path(fig, ax, path, choice)

# Main loop
if __name__ == "__main__":
    epolygons = gen_polygons('TestingGrid/world2_enclosures.txt')
    tpolygons = gen_polygons('TestingGrid/world2_turfs.txt')

    source = Point(8,10)
    dest = Point(43,45)
    
    print("Select a search algorithm: BFS, DFS, GBFS, A*")
    user_choice = input("Enter your choice: ").strip().upper()
    draw_algorithm(user_choice, source, dest, epolygons, tpolygons)
