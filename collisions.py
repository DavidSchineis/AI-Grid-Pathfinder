# Collisions

# Returns True if the move is valid
def is_valid_move(point, enclosures):
    if is_on_polygon_corner(point, enclosures):
        return False
    for polygon in enclosures:
        if is_inside_polygon(point, polygon) or is_on_polygon_edge(point, polygon):
            return False 
    return True

# Returns True if the point is on an edge of a polygon
def is_on_polygon_edge(point, polygon, epsilon = 1e-9):
    x, y = point.to_tuple()
    
    for i in range(len(polygon)):
        p1x, p1y = polygon[i].to_tuple()
        p2x, p2y = polygon[(i + 1) % len(polygon)].to_tuple()
        
        # Check if point (x, y) lies on the line segment (p1, p2)
        if min(p1x, p2x) <= x <= max(p1x, p2x) and min(p1y, p2y) <= y <= max(p1y, p2y):
            if abs((p2x - p1x) * (y - p1y) - (x - p1x) * (p2y - p1y)) < epsilon:
                return True
    return False

# Returns True if the point is a polygon corner
def is_on_polygon_corner(point, polygons):
    adjacent_edges = 0
    for polygon in polygons:
        if is_on_polygon_edge(point, polygon):
            adjacent_edges += 1
        if adjacent_edges >= 2: 
            return True
    return False

# Returns True if the point is inside a polygon
def is_inside_polygon(point, polygon):
    x, y = point.to_tuple()
    n = len(polygon)
    inside = False
    p1x, p1y = polygon[0].to_tuple()
    for i in range(n + 1):
        p2x, p2y = polygon[i % n].to_tuple()
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        num = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or x <= num:
                        inside = not inside
        p1x, p1y = p2x, p2y
    return inside

# Returns turf/no turf multiplier 
def get_action_cost(point, turfs):
    if is_on_polygon_corner(point, turfs):
        return 15.0
    for turf in turfs:
        if is_inside_polygon(point, turf) or is_on_polygon_edge(point, turf):
            return 1.5
    return 1.0
