# Grid

# Import libraries
import matplotlib.pyplot as plt
import math

MAX = 50

# Point
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f'({self.x}, {self.y})'
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False
    def to_tuple(self):
        return self.x, self.y
    def __hash__(self):
        return hash((self.x, self.y))
    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
        #return abs(self.x - other.x) + abs(self.y - other.y)

# Draws background plot
def draw_board():
    fig = plt.figure(figsize=[8,8])
    ax = fig.add_subplot(111)
    ax.set_axis_off()
    return fig, ax

# Draws grid lines
def draw_grids(ax):
    for x in range(MAX):
        ax.plot([x, x], [0,MAX-1], color = '0.75', linestyle='dotted')
    for y in range(MAX):
        ax.plot([0, MAX-1], [y,y], color = '0.75', linestyle='dotted')
    ax.set_position([0,0.02,1,1])

# Draws point
def draw_point(ax, x, y):
    ax.plot(x,y,'o',markersize=4,
        markeredgecolor=(0,0,0),
        markerfacecolor='k',
        markeredgewidth=1)

# Draws source point
def draw_source(ax, x, y):
    ax.plot(x,y,'o',markersize=4,
        markeredgecolor='b',
        markerfacecolor='b',
        markeredgewidth=1)

# Draws destination point
def draw_dest(ax, x, y):
    ax.plot(x,y,'o',markersize=4,
        markeredgecolor='r',
        markerfacecolor='r',
        markeredgewidth=1)

# Draws red point
def draw_red_point(ax, x, y):
    ax.plot(x,y,'o',markersize=4,
        markeredgecolor='r',
        markerfacecolor='r',
        markeredgewidth=1)

# Draws green point
def draw_green_point(ax, x, y):
    ax.plot(x,y,'o',markersize=4,
        markeredgecolor='g',
        markerfacecolor='g',
        markeredgewidth=1)

# Draws line
def draw_line(ax, xs, ys):
    ax.plot(xs, ys, color='k')

# Draws red line
def draw_result_line(ax, xs, ys):
    ax.plot(xs, ys, color='r')

# Draws green line
def draw_green_line(ax, xs, ys):
    ax.plot(xs, ys, color='g')

# Fills in polygon
def fill_polygon(ax, polygon, color):
    xs = [p.x for p in polygon]
    ys = [p.y for p in polygon]
    ax.fill(xs, ys, color=color, alpha=0.5)
