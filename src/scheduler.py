"""
scheduler.py

Task scheduler for Kaggriculture AI.

Responsible for ordering all pending jobs
by importance.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations

from dataclasses import dataclass


# ==========================================================
# Task
# ==========================================================

@dataclass
class Task:
    """
    Represents one scheduled task.
    """

    priority: int
    action: str
    target: tuple | None = None
    crop: str | None = None
    product: str | None = None
    amount: int | None = None


# ==========================================================
# Scheduler
# ==========================================================

class Scheduler:
    """
    Stores pending tasks and always returns the
    highest-priority task first.

    Lower priority values indicate higher importance.
    """

    def __init__(self):
        self.tasks: list[Task] = []

    # ------------------------------------------------------
    # Add Task
    # ------------------------------------------------------

    def add(
        self,
        priority,
        action,
        target=None,
        crop=None,
        product=None,
        amount=None,
    ):
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
    # Sort Tasks
    # ------------------------------------------------------

    def sort(self):
        """
        Sort tasks by priority.
        Lower number = higher priority.
        """

        self.tasks.sort(key=lambda task: task.priority)

    # ------------------------------------------------------
    # Backward Compatibility
    # ------------------------------------------------------

    def next(self):
        """
        Alias for next_task().

        Maintained for backward compatibility with
        existing tests and modules.
        """

        return self.next_task()

    # ------------------------------------------------------
    # Get Next Task
    # ------------------------------------------------------

    def next_task(self):
        """
        Return and remove the highest-priority task.
        """

        if self.empty():
            return None

        self.sort()

        return self.tasks.pop(0)

    # ------------------------------------------------------
    # Clear
    # ------------------------------------------------------

    def clear(self):
        """
        Remove all scheduled tasks.
        """

        self.tasks.clear()

    # ------------------------------------------------------
    # Empty
    # ------------------------------------------------------

    def empty(self):
        """
        Return True if no tasks exist.
        """

        return len(self.tasks) == 0

    # ------------------------------------------------------
    # Length
    # ------------------------------------------------------

    def __len__(self):
        return len(self.tasks)

    # ------------------------------------------------------
    # Iterator
    # ------------------------------------------------------

    def __iter__(self):
        self.sort()
        return iter(self.tasks)

    # ------------------------------------------------------
    # Summary
    # ------------------------------------------------------

    def summary(self):
        """
        Return all scheduled tasks as dictionaries.
        """

        return [
            {
                "priority": task.priority,
                "action": task.action,
                "target": task.target,
                "crop": task.crop,
                "product": task.product,
                "amount": task.amount,
            }
            for task in sorted(
                self.tasks,
                key=lambda t: t.priority,
            )
        ]