"""
Loading screen implementation for MetDat.
"""
import tkinter as tk
from tkinter import ttk
from .styles import Theme

class RoundedFrame(tk.Canvas):
    """A canvas that draws a rounded rectangle frame."""
    def __init__(self, parent, bg, border_color, border_width=2, corner_radius=8, **kwargs):
        super().__init__(parent, **kwargs)
        self.border_width = border_width
        self.corner_radius = corner_radius
        self.border_color = border_color
        self.bg = bg
        
        self.bind('<Configure>', self._on_resize)
        self.configure(highlightthickness=0, bg=self.bg)

    def _on_resize(self, event):
        """Redraw the rounded rectangle when the window is resized."""
        width = event.width
        height = event.height
        
        # Clear previous drawing
        self.delete('all')
        
        # Draw the rounded rectangle
        self.create_rounded_rect(
            self.border_width/2,
            self.border_width/2,
            width - self.border_width,
            height - self.border_width,
            self.corner_radius,
            self.border_color,
            self.bg
        )

    def create_rounded_rect(self, x1, y1, x2, y2, radius, border_color, fill_color):
        """Create a rounded rectangle."""
        points = [
            x1 + radius, y1,                      # Top line
            x2 - radius, y1,
            x2 - radius, y1,                      # Top right corner
            x2, y1,
            x2, y1 + radius,
            x2, y1 + radius,                      # Right line
            x2, y2 - radius,
            x2, y2 - radius,                      # Bottom right corner
            x2, y2,
            x2 - radius, y2,
            x2 - radius, y2,                      # Bottom line
            x1 + radius, y2,
            x1 + radius, y2,                      # Bottom left corner
            x1, y2,
            x1, y2 - radius,
            x1, y2 - radius,                      # Left line
            x1, y1 + radius,
            x1, y1 + radius,                      # Top left corner
            x1, y1,
            x1 + radius, y1,
        ]
        
        return self.create_polygon(
            points,
            smooth=True,
            fill=fill_color,
            outline=border_color,
            width=self.border_width
        )

class LoadingScreen(tk.Tk):
    def __init__(self):
        super().__init__()

        # Configure the window
        self.overrideredirect(True)  # Remove window decorations
        self.attributes('-topmost', True)
        
        # Calculate center position
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        window_width = 400
        window_height = 200
        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2
        
        # Set window size and position
        self.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
        
        # Get current system theme
        self.theme_mode = Theme.get_system_mode()
        
        # Create main container with rounded corners
        self.container = RoundedFrame(
            self,
            bg=Theme.get_color('bg', self.theme_mode),
            border_color=Theme.get_color('border', self.theme_mode),
            border_width=2,  # Thinner border
            corner_radius=6  # Slightly rounded corners
        )
        self.container.pack(fill=tk.BOTH, expand=True, padx=2, pady=2)
        
        # Create main frame
        self.main_frame = tk.Frame(
            self.container,
            bg=Theme.get_color('bg', self.theme_mode)
        )
        # Position the frame within the rounded container
        self.main_frame.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.96)
        
        # Add title
        self.title_label = tk.Label(
            self.main_frame,
            text="META INJECTOR",
            font=Theme.TITLE_FONT,
            fg=Theme.get_color('fg', self.theme_mode),
            bg=Theme.get_color('bg', self.theme_mode)
        )
        self.title_label.pack(pady=(40, 20))
        
        # Create progress bar frame
        self.progress_frame = tk.Frame(
            self.main_frame,
            bg=Theme.get_color('bg', self.theme_mode),
            padx=40
        )
        self.progress_frame.pack(fill=tk.X)
        
        # Configure progress bar style
        self.style = ttk.Style()
        self.style.configure(
            "MetDat.Horizontal.TProgressbar",
            troughcolor=Theme.get_color('accent', self.theme_mode),
            background=Theme.get_color('progress', self.theme_mode),
            bordercolor=Theme.get_color('border', self.theme_mode),
            lightcolor=Theme.get_color('progress', self.theme_mode),
            darkcolor=Theme.get_color('progress', self.theme_mode)
        )
        
        # Add progress bar
        self.progress = ttk.Progressbar(
            self.progress_frame,
            style="MetDat.Horizontal.TProgressbar",
            mode='determinate',
            length=320
        )
        self.progress.pack(fill=tk.X)
        
        # Add status label
        self.status_label = tk.Label(
            self.main_frame,
            text="Loading...",
            font=Theme.BODY_FONT,
            fg=Theme.get_color('fg', self.theme_mode),
            bg=Theme.get_color('bg', self.theme_mode)
        )
        self.status_label.pack(pady=20)

    def update_progress(self, value: int, status: str = None):
        """Update progress bar value and status text."""
        self.progress['value'] = value
        if status:
            self.status_label.config(text=status)
        self.update()

    def finish(self):
        """Close the loading screen."""
        self.destroy()
