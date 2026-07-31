"""
movement.py

Movement and navigation utilities.

Responsible for computing distances, neighboring tiles,
and determining the next movement action.

Future versions can replace this with A* pathfinding without
changing the planner.
"""

from __future__ import annotations

from collections import deque

from src.constants import (
    NORTH,
    SOUTH,
    EAST,
    WEST,
)

# -----------------------------------------
# Movement vectors
# -----------------------------------------

MOVE_VECTOR = {
    NORTH: (0, -1),
    SOUTH: (0, 1),
    EAST: (1, 0),
    WEST: (-1, 0),
}

REVERSE = {
    NORTH: SOUTH,
    SOUTH: NORTH,
    EAST: WEST,
    WEST: EAST,
}


class Movement:

    def __init__(self, board):

        self.board = board
        self.size = len(board)

    # -----------------------------------------
    # Valid position
    # -----------------------------------------

    def valid(self, x, y):

        if x < 0:
            return False

        if y < 0:
            return False

        if x >= self.size:
            return False

        if y >= self.size:
            return False

        if self.board[y][x] == "LOCKED":
            return False

        return True

    # -----------------------------------------
    # Manhattan distance
    # -----------------------------------------

    @staticmethod
    def distance(a, b):

        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    # -----------------------------------------
    # Neighbor tiles
    # -----------------------------------------

    def neighbors(self, position):

        x, y = position

        results = []

        for action, (dx, dy) in MOVE_VECTOR.items():

            nx = x + dx
            ny = y + dy

            if self.valid(nx, ny):
                results.append((action, (nx, ny)))

        return results

    # -----------------------------------------
    # Breadth First Search
    # -----------------------------------------

    def shortest_path(self, start, goal):

        if start == goal:
            return []

        queue = deque()

        queue.append(start)

        came_from = {}

        visited = {start}

        while queue:

            current = queue.popleft()

            if current == goal:
                break

            for action, nxt in self.neighbors(current):

                if nxt in visited:
                    continue

                visited.add(nxt)

                came_from[nxt] = (current, action)

                queue.append(nxt)

        if goal not in came_from:
            return []

        actions = []

        node = goal

        while node != start:

            previous, action = came_from[node]

            actions.append(action)

            node = previous

        actions.reverse()

        return actions

    # -----------------------------------------
    # Next Action
    # -----------------------------------------

    def next_action(self, start, goal):

        path = self.shortest_path(start, goal)

        if len(path) == 0:
            return None

        return path[0]