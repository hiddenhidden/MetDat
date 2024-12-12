"""
Loading screen window for MetDat.
"""
import tkinter as tk
from tkinter import ttk
from .styles import Theme, Mode
from .components import RoundedFrame
import darkdetect

class LoadingScreen(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("MetDat")
        self.theme_mode = Theme.get_system_mode()
        colors = Theme.get_colors(self.theme_mode)
        
        self.configure(bg=colors["background"])
        
        # Center the window
        window_width = 400
        window_height = 250
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        center_x = int(screen_width/2 - window_width/2)
        center_y = int(screen_height/2 - window_height/2)
        self.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        
        # Create main container
        container = RoundedFrame(
            self,
            width=window_width - 40,
            height=window_height - 40,
            background=colors["container"],
            highlightbackground=colors["border"],
            highlightthickness=1,
            fixed_size=True  # This frame shouldn't resize
        )
        container.pack(expand=True, padx=20, pady=20)
        container.pack_propagate(False)
        
        # Title
        title_label = tk.Label(
            container,
            text="MetDat",
            font=Theme.TITLE_FONT,
            bg=colors["container"],
            fg=colors["text"]
        )
        title_label.pack(pady=(40, 20))
        
        # Progress bar style
        self.style = ttk.Style()
        self.style.configure(
            "Custom.Horizontal.TProgressbar",
            troughcolor=colors["container"],
            background=colors["progress"],
            darkcolor=colors["progress"],
            lightcolor=colors["progress"],
            bordercolor=colors["border"]
        )
        
        # Progress bar
        self.progress_bar = ttk.Progressbar(
            container,
            style="Custom.Horizontal.TProgressbar",
            length=300,
            mode='determinate'
        )
        self.progress_bar.pack(pady=20)
        
        # Status label
        self.status_label = tk.Label(
            container,
            text="Loading...",
            font=Theme.BODY_FONT,
            bg=colors["container"],
            fg=colors["text"]
        )
        self.status_label.pack(pady=10)
    
    def update_progress(self, value, status_text=None):
        """Update the progress bar value and status text."""
        self.progress_bar["value"] = value
        if status_text:
            self.status_label.config(text=status_text)
        self.update()
        
    def finish(self):
        """Clean up and destroy the loading screen."""
        self.destroy()
