"""
event_bus.py

Lightweight publish/subscribe event bus for the
Kaggriculture AI Agent.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations


class EventBus:
    """
    Simple publish/subscribe event system.
    """

    def __init__(self):
        self._listeners = {}

    # ---------------------------------------------------------

    def subscribe(self, event: str, callback):
        """
        Register a callback for an event.
        """
        self._listeners.setdefault(event, []).append(callback)

    # ---------------------------------------------------------

    def unsubscribe(self, event: str, callback):
        """
        Remove a callback.
        """
        listeners = self._listeners.get(event)

        if listeners and callback in listeners:
            listeners.remove(callback)

    # ---------------------------------------------------------

    def publish(self, event: str, data=None):
        """
        Publish an event.
        """
        for callback in self._listeners.get(event, []):
            callback(data)

    # ---------------------------------------------------------

    def listener_count(self, event: str) -> int:
        """
        Return number of listeners.
        """
        return len(self._listeners.get(event, []))

    # ---------------------------------------------------------

    def clear(self):
        """
        Remove every listener.
        """
        self._listeners.clear()