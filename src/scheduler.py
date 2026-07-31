"""
scheduler.py

Task scheduler for Kaggriculture AI.

Responsible for ordering all pending jobs
by importance.
"""

from __future__ import annotations

from dataclasses import dataclass


# ==========================================================
# Task
# ==========================================================

@dataclass
class Task:
    priority: int
    action: str
    target: tuple | None = None
    crop: str | None = None


# ==========================================================
# Scheduler
# ==========================================================

class Scheduler:
    """
    Stores all pending tasks and always returns
    the highest-priority one.
    """

    def __init__(self):
        self.tasks = []

    # ------------------------------------------------------

    def clear(self):
        """Remove all scheduled tasks."""
        self.tasks.clear()

    # ------------------------------------------------------

    def add(self, priority, action, target=None, crop=None, product=None, amount=None,):
        """
        Add a new task to the scheduler.
        """

        task = Task(
            priority=priority,
            action=action,
            target=target,
            crop=crop,
            product=product,
            amount=amount,
        )

        self.tasks.append(task)

    # ------------------------------------------------------

    def sort(self):
        """Sort tasks by priority (lower number = higher priority)."""

        self.tasks.sort(key=lambda task: task.priority)

    # ------------------------------------------------------

    def next(self):
        """
        Return the highest-priority task.
        """

        if not self.tasks:
            return None

        self.sort()

        return self.tasks.pop(0)

    # ------------------------------------------------------

    def empty(self):
        """Return True if there are no tasks."""

        return len(self.tasks) == 0

    # ------------------------------------------------------

    def __len__(self):
        return len(self.tasks)

    # ------------------------------------------------------

    def __iter__(self):
        self.sort()
        return iter(self.tasks)

    # ------------------------------------------------------

    def summary(self):
        """
        Return a readable list of pending tasks.
        """

        return [
            {
                "priority": task.priority,
                "action": task.action,
                "target": task.target,
                "crop": task.crop,
            }
            for task in sorted(
                self.tasks,
                key=lambda t: t.priority,
            )
        ]