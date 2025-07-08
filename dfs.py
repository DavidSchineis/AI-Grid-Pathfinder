# Depth First Search

# Import libraries
from utils import Stack
from grid import Point
from collisions import is_valid_move, get_action_cost

def depth_first_search(start, goal, enclosures, turfs):
   
    # Use a stack for frontier
    frontier = Stack()
    frontier.push([start])
    
    # Keep track of visited nodes
    visited = set()
    visited.add(start.to_tuple())
    
    nodes_expanded = 0

    # While there are nodes to explore
    while not frontier.isEmpty():
        
        # Pop frontier node
        path = frontier.pop()
        current = path[-1]
        nodes_expanded += 1
        
        # Goal check
        if current == goal:
            
            # Compute the path cost
            total_cost = sum(get_action_cost(p, turfs) for p in path)
            return path
        
        # Expansion
        for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:  # Up, Right, Down, Left
            neighbor = Point(current.x + dx, current.y + dy)
            
            # Valid move check
            if 0 <= neighbor.x < 50 and 0 <= neighbor.y < 50:
                if is_valid_move(neighbor, enclosures) and neighbor.to_tuple() not in visited:
                    visited.add(neighbor.to_tuple())
                    frontier.push(path + [neighbor])
    
    # Return failure if goal not reached
    return [] 
