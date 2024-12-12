"""
Styles and theme configuration for the application.
"""
from enum import Enum
import darkdetect

class Theme:
    # Font configurations
    TITLE_FONT = ("Helvetica Neue", 24, "bold")  # For main titles
    HEADER_FONT = ("Helvetica Neue", 16, "bold")  # For section headers
    BUTTON_FONT = ("Roboto Mono", 12, "bold")    # For buttons
    BODY_FONT = ("Roboto Mono", 12)              # For regular text

    class Mode(Enum):
        LIGHT = "light"
        DARK = "dark"

    # Colors from GrayScalePalette.png
    COLORS = {
        Mode.LIGHT: {
            'bg': '#FFFFFF',
            'fg': '#000000',
            'accent': '#808080',
            'border': '#000000',  # Thick black border for light mode
            'progress': '#404040',
        },
        Mode.DARK: {
            'bg': '#000000',
            'fg': '#FFFFFF',
            'accent': '#808080',
            'border': '#FFFFFF',  # Thick white border for dark mode
            'progress': '#D3D3D3',
        }
    }

    @classmethod
    def get_system_mode(cls) -> Mode:
        """Get the current system theme mode."""
        return cls.Mode.DARK if darkdetect.isDark() else cls.Mode.LIGHT

    @classmethod
    def get_color(cls, color_name: str, mode: Mode = None) -> str:
        """Get color value based on theme mode."""
        if mode is None:
            mode = cls.get_system_mode()
        return cls.COLORS[mode].get(color_name, '#000000')
