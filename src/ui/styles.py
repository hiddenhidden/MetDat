"""
Styles and theme configuration for the application.
"""
from enum import Enum

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
    # These will be populated based on the palette file
    COLORS = {
        Mode.LIGHT: {
            'bg': '#FFFFFF',
            'fg': '#000000',
            'accent': '#808080',
            'border': '#D3D3D3',
            'progress': '#404040',
        },
        Mode.DARK: {
            'bg': '#000000',
            'fg': '#FFFFFF',
            'accent': '#808080',
            'border': '#404040',
            'progress': '#D3D3D3',
        }
    }

    @classmethod
    def get_color(cls, color_name: str, mode: Mode = Mode.LIGHT) -> str:
        """Get color value based on current theme mode."""
        return cls.COLORS[mode].get(color_name, '#000000')
