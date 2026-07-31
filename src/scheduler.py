"""
scheduler.py

Task scheduler for Kaggriculture AI.

Responsible for ordering all pending jobs
by importance.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class Task:
    priority: int
    action: str
    target: Any


class Scheduler:

    def __init__(self):

        self.tasks = []

    # --------------------------------------------------------

    def clear(self):

        self.tasks.clear()

    # --------------------------------------------------------

    def add(self, priority, action, target=None):

        self.tasks.append(

            Task(
                priority=priority,
                action=action,
                target=target,
            )

        )

    # --------------------------------------------------------

    def sort(self):

        self.tasks.sort(
            key=lambda task: task.priority
        )

    # --------------------------------------------------------

    def next(self):

        if not self.tasks:
            return None

        self.sort()

        return self.tasks.pop(0)

    # --------------------------------------------------------

    def empty(self):

        return len(self.tasks) == 0

    # --------------------------------------------------------

    def __len__(self):

        return len(self.tasks)

    # --------------------------------------------------------

    def __iter__(self):

        self.sort()

        return iter(self.tasks)

    # --------------------------------------------------------

    def summary(self):

        return [

            {

                "priority": task.priority,
                "action": task.action,
                "target": task.target,

            }

            for task in sorted(
                self.tasks,
                key=lambda t: t.priority,
            )

        ]