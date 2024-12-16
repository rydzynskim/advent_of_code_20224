import math


class Node:
    def __init__(self, row, col, dir):
        self.row = row
        self.col = col
        self.dir = dir
        self.path = math.inf
        self.children = {}
        self.previous = []

    def set_child(self, row, col, dir, edge):
        self.children[s(row, col, dir)] = edge

    def get_children(self):
        return self.children

    def set_path(self, path):
        self.path = path

    def get_path(self):
        return self.path

    def is_same(self, row, col):
        return self.row == row and self.col == col

    def reset_previous(self):
        self.previous = []

    def add_previous(self, s):
        self.previous.append(s)

    def get_previous(self):
        return self.previous


def s(row, col, dir):
    return f"{row},{col},{dir}"


def left(dir):
    if dir == 'N':
        return 'W'
    if dir == 'W':
        return 'S'
    if dir == 'S':
        return 'E'
    if dir == 'E':
        return 'N'
    raise ValueError(f"{dir}")


def right(dir):
    if dir == 'N':
        return 'E'
    if dir == 'E':
        return 'S'
    if dir == 'S':
        return 'W'
    if dir == 'W':
        return 'N'
    raise ValueError(f"{dir}")


def next(row, col, dir):
    if dir == 'N':
        return [row-1, col]
    if dir == 'E':
        return [row, col+1]
    if dir == 'S':
        return [row+1, col]
    if dir == 'W':
        return [row, col-1]
    raise ValueError(f"{dir}")


def construct_graph(maze):
    nodes = {}
    dirs = ['N', 'S', 'E', 'W']
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            if maze[row][col] == '.':
                for dir in dirs:
                    node = Node(row, col, dir)
                    n = next(row, col, dir)
                    if maze[n[0]][n[1]] == '.':
                        node.set_child(n[0], n[1], dir, 1)
                    node.set_child(row, col, left(dir), 1000)
                    node.set_child(row, col, right(dir), 1000)
                    nodes[s(row, col, dir)] = node
    return nodes


def min_path(nodes, unvisited):
    mp = math.inf
    mn = None
    for key in unvisited:
        node = nodes[key]
        if node.get_path() < mp:
            mp = node.get_path()
            mn = key
    return mn


def dijkstra(nodes, s_row, s_col, s_dir, t_row, t_col):
    # mark all the nodes as unvisited
    unvisited = set()
    for key in nodes:
        unvisited.add(key)

    # our starting node gets an initial path length of 0
    nodes[s(s_row, s_col, s_dir)].set_path(0)

    # keep going until everything is visited
    while len(unvisited) > 0:
        # our current node is the unvisited node with the shortest path
        cur_key = min_path(nodes, unvisited)
        cur_node = nodes[cur_key]
        unvisited.remove(cur_key)

        # if the current node is the target position then done
        if cur_node.is_same(t_row, t_col):
            return cur_node.get_path()

        # visit all the neighbors of the current node, updating shortest paths if necessary
        for child_key, edge in cur_node.get_children().items():
            child_node = nodes[child_key]
            alt = cur_node.get_path() + edge
            if alt == child_node.get_path():
                child_node.add_previous(cur_key)
            elif alt < child_node.get_path():
                child_node.reset_previous()
                child_node.add_previous(cur_key)
                child_node.set_path(alt)

    raise RuntimeError('Never saw target position')


raw_lines = []
with open('./inputs/16.txt') as file:
    raw_lines = file.readlines()

maze = []
for row in range(len(raw_lines)):
    maze_row = []
    stripped = raw_lines[row].strip()
    for col in range(len(stripped)):
        if stripped[col] != "#":
            maze_row.append(".")
        else:
            maze_row.append(stripped[col])
    maze.append(maze_row)

nodes = construct_graph(maze)
dijkstra(nodes, len(maze)-2, 1, 'E', 1, len(maze[0])-2)

points = set()
cur = [s(1, len(maze[0])-2, 'N'), s(1, len(maze[0])-2, 'S'),
       s(1, len(maze[0])-2, 'E'), s(1, len(maze[0])-2, 'W')]
while len(cur) > 0:
    next = []
    for c_key in cur:
        p = c_key.split(',')
        points.add(f"{p[0]},{p[1]}")
        c_node = nodes[c_key]
        for prev in c_node.get_previous():
            next.append(prev)
    cur = next


print(len(points))
