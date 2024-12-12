"""
Loading screen implementation for MetDat.
"""
import tkinter as tk
from tkinter import ttk
from .styles import Theme

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
        
        # Create main frame
        self.main_frame = tk.Frame(self, bg=Theme.get_color('bg'))
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Add title
        self.title_label = tk.Label(
            self.main_frame,
            text="META INJECTOR",
            font=Theme.TITLE_FONT,
            fg=Theme.get_color('fg'),
            bg=Theme.get_color('bg')
        )
        self.title_label.pack(pady=(40, 20))
        
        # Create progress bar frame
        self.progress_frame = tk.Frame(
            self.main_frame,
            bg=Theme.get_color('bg'),
            padx=40
        )
        self.progress_frame.pack(fill=tk.X)
        
        # Configure progress bar style
        self.style = ttk.Style()
        self.style.configure(
            "MetDat.Horizontal.TProgressbar",
            troughcolor=Theme.get_color('border'),
            background=Theme.get_color('progress'),
            bordercolor=Theme.get_color('border'),
            lightcolor=Theme.get_color('progress'),
            darkcolor=Theme.get_color('progress')
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
            fg=Theme.get_color('fg'),
            bg=Theme.get_color('bg')
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
