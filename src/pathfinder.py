"""
pathfinder.py

Simple grid path planner for the Kaggriculture AI Agent.

Uses Breadth-First Search (BFS) to compute the shortest path
between two tiles on the farm.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations

from collections import deque

from src.constants import Direction


class Pathfinder:
    """
    Breadth-First Search (BFS) path planner.

    Computes the shortest path between two positions
    on the farm grid.
    """

    def __init__(self, world):
        """
        Parameters
        ----------
        world : World
            Current world representation.
        """
        self.world = world

    # ---------------------------------------------------------
    # Neighbor Search
    # ---------------------------------------------------------

    def neighbors(self, position):
        """
        Return all valid neighboring tiles.

        Parameters
        ----------
        position : tuple[int, int]

        Returns
        -------
        list[tuple[int, int]]
        """

        x, y = position

        candidates = [
            (x, y - 1),  # North
            (x, y + 1),  # South
            (x - 1, y),  # West
            (x + 1, y),  # East
        ]

        valid = []

        for nx, ny in candidates:

             if self.world.is_walkable(nx, ny):
                valid.append((nx, ny))

        return valid

    # ---------------------------------------------------------
    # Breadth-First Search
    # ---------------------------------------------------------

    def find_path(self, start, goal):
        """
        Compute the shortest path using BFS.

        Parameters
        ----------
        start : tuple[int, int]
        goal : tuple[int, int]

        Returns
        -------
        list[tuple[int, int]]
            Path including start and goal.
        """

        if start == goal:
            return [start]

        queue = deque([[start]])

        visited = {start}

        while queue:

            path = queue.popleft()

            current = path[-1]

            if current == goal:
                return path

            for neighbor in self.neighbors(current):

                if neighbor not in visited:

                    visited.add(neighbor)

                    queue.append(path + [neighbor])

        # No path found
        return []

    # ---------------------------------------------------------
    # Path → Directions
    # ---------------------------------------------------------

    def directions(self, path):
        """
        Convert a path into movement commands.

        Parameters
        ----------
        path : list[tuple[int, int]]

        Returns
        -------
        list[str]
            Example:
            ["EAST", "EAST", "SOUTH"]
        """

        moves = []

        for i in range(len(path) - 1):

            x1, y1 = path[i]
            x2, y2 = path[i + 1]

            if x2 > x1:
                moves.append(Direction.EAST.value)

            elif x2 < x1:
                moves.append(Direction.WEST.value)

            elif y2 > y1:
                moves.append(Direction.SOUTH.value)

            elif y2 < y1:
                moves.append(Direction.NORTH.value)

        return moves