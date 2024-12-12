"""
Styles and theme management for MetDat.
"""
from enum import Enum
import darkdetect

class Mode(str, Enum):
    """Theme mode enumeration."""
    LIGHT = "light"
    DARK = "dark"

class Theme:
    """Theme management for MetDat."""
    
    # Font configurations
    TITLE_FONT = ("Helvetica Neue", 24, "bold")  # For main titles
    HEADER_FONT = ("Helvetica Neue", 16, "bold")  # For section headers
    BUTTON_FONT = ("Roboto Mono", 12, "bold")    # For buttons
    BODY_FONT = ("Roboto Mono", 12)              # For regular text

    # Color definitions for the entire application
    THEME_COLORS = {
        Mode.LIGHT: {
            "background": "#CCCCCC",  # Much darker gray for main background
            "container": "#DDDDDD",   # Slightly lighter but still notably gray
            "text": "#000000",
            "border": "#BBBBBB",      # Darker border to match new scheme
            "accent": "#404040",
            "button": {
                "bg": "#404040",
                "fg": "#FFFFFF",
                "hover_bg": "#606060",
                "hover_fg": "#FFFFFF"
            },
            "progress": "#808080"
        },
        Mode.DARK: {
            "background": "#202020",   # Dark gray for main background
            "container": "#282828",    # Slightly lighter gray for containers
            "text": "#FFFFFF",
            "border": "#404040",
            "accent": "#C0C0C0",
            "button": {
                "bg": "#404040",
                "fg": "#FFFFFF",
                "hover_bg": "#606060",
                "hover_fg": "#FFFFFF"
            },
            "progress": "#808080"
        }
    }

    @classmethod
    def get_system_mode(cls) -> Mode:
        """Get the current system theme mode."""
        return Mode.DARK if darkdetect.isDark() else Mode.LIGHT

    @classmethod
    def get_colors(cls, mode: Mode = None) -> dict:
        """Get color palette for the specified mode."""
        if mode is None:
            mode = cls.get_system_mode()
        return cls.THEME_COLORS[mode]
