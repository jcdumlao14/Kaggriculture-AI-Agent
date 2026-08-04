"""
plugin_manager.py

Plugin Manager for the Kaggriculture AI Agent.

Registers and manages pluggable AI modules.

Author: Jocelyn C. Dumlao
Project: Kaggriculture-AI-Agent
"""

from __future__ import annotations


class PluginManager:
    """
    Manages pluggable AI components.
    """

    def __init__(self):
        self._plugins = {}

    # ---------------------------------------------------------

    def register(self, name: str, plugin):
        """
        Register a plugin.
        """
        self._plugins[name] = plugin

    # ---------------------------------------------------------

    def get(self, name: str):
        """
        Retrieve a plugin.
        """
        return self._plugins.get(name)

    # ---------------------------------------------------------

    def exists(self, name: str) -> bool:
        """
        Check whether a plugin exists.
        """
        return name in self._plugins

    # ---------------------------------------------------------

    def unregister(self, name: str):
        """
        Remove a plugin.
        """
        self._plugins.pop(name, None)

    # ---------------------------------------------------------

    def list_plugins(self):
        """
        Return registered plugin names.
        """
        return sorted(self._plugins.keys())

    # ---------------------------------------------------------

    def clear(self):
        """
        Remove every plugin.
        """
        self._plugins.clear()