# Greedy Best First Search

# Import libraries
from utils import PriorityQueue
from grid import Point 
from collisions import is_valid_move, get_action_cost

def greedy_best_first_search(start, goal, enclosures, turfs):
    
    # Use priority queue for frontier
    frontier = PriorityQueue()
    frontier.push((start.x, start.y, start), start.distance(goal))

    # Keep track of visited nodes
    visited = set()
    visited.add(start)

    nodes_expanded = 0  
    came_from = {start: None} 

    # While there are nodes to explore
    while not frontier.isEmpty():
        (x, y, current) = frontier.pop()
        nodes_expanded += 1

        # Goal check
        if current == goal:
            # Reconstruct path
            path = []
            while current is not None:
                path.append(current)
                current = came_from[current]
            path.reverse()

            # Compute the path cost
            total_cost = sum(get_action_cost(p, turfs) for p in path)
            return path

        # Expansion
        for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:  # Up, Right, Down, Left
            neighbor = Point(current.x + dx, current.y + dy)

            # Valid move check
            if 0 <= neighbor.x < 50 and 0 <= neighbor.y < 50:
                if is_valid_move(neighbor, enclosures) and neighbor not in visited:
                    frontier.push((neighbor.x, neighbor.y, neighbor), neighbor.distance(goal))
                    came_from[neighbor] = current
                    visited.add(neighbor)

    # Return failure if goal not reached
    return []
