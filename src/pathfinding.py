"""
pathfinding.py

Shortest-path navigation for the Kaggriculture AI Agent.

Uses Breadth-First Search (BFS) to find the shortest
path between two locations on the farm.

Author: Jocelyn Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations

from collections import deque

from src.constants import (
    Direction,
    DIRECTION_VECTOR,
    TileKind,
)


class PathFinder:
    """
    Breadth-First Search pathfinder.
    """

    def __init__(self, parser):

        self.parser = parser
        self.tiles = parser.tiles

        self.height = len(self.tiles)
        self.width = len(self.tiles[0])

    # ---------------------------------------------------------
    # Helpers
    # ---------------------------------------------------------

    def inside(self, x, y):
        """Return True if coordinates are inside the map."""
        return (
            0 <= x < self.width
            and
            0 <= y < self.height
        )

    def walkable(self, x, y):
        """
        Return True if the tile can be walked on.
        """

        tile = self.tiles[y][x]

        if tile == TileKind.LOCKED.value:
            return False

        return True

    # ---------------------------------------------------------
    # BFS
    # ---------------------------------------------------------

    def shortest_path(self, start, goal):
        """
        Compute the shortest path from start to goal.

        Parameters
        ----------
        start : tuple
        goal : tuple

        Returns
        -------
        list
            Sequence of coordinates.
        """

        if start == goal:
            return [start]

        queue = deque([start])

        parent = {
            start: None
        }

        while queue:

            current = queue.popleft()

            if current == goal:
                break

            x, y = current

            for direction in Direction:

                dx, dy = DIRECTION_VECTOR[direction]

                nx = x + dx
                ny = y + dy

                if not self.inside(nx, ny):
                    continue

                if not self.walkable(nx, ny):
                    continue

                nxt = (nx, ny)

                if nxt in parent:
                    continue

                parent[nxt] = current
                queue.append(nxt)

        if goal not in parent:
            return []

        path = []

        node = goal

        while node is not None:

            path.append(node)
            node = parent[node]

        path.reverse()

        return path

    # ---------------------------------------------------------
    # Directions
    # ---------------------------------------------------------

    def path_to_actions(self, path):
        """
        Convert coordinates into movement actions.
        """

        actions = []

        for i in range(1, len(path)):

            x1, y1 = path[i - 1]
            x2, y2 = path[i]

            dx = x2 - x1
            dy = y2 - y1

            if dx == 1:
                actions.append(Direction.EAST.value)

            elif dx == -1:
                actions.append(Direction.WEST.value)

            elif dy == 1:
                actions.append(Direction.SOUTH.value)

            elif dy == -1:
                actions.append(Direction.NORTH.value)

        return actions

    # ---------------------------------------------------------

    def next_move(self, start, goal):
        """
        Return the first movement action needed
        to reach the goal.

        Returns
        -------
        str | None
        """

        path = self.shortest_path(start, goal)

        if len(path) <= 1:
            return None

        actions = self.path_to_actions(path)

        if not actions:
            return None

        return actions[0]