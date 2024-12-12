"""
Main window implementation for MetDat.
Implements a single-window architecture with a container-based layout system.
"""
import tkinter as tk
from tkinter import ttk
from .styles import Theme, Mode
from .components import RoundedFrame
import darkdetect

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        
        # Configure window
        self.title("META INJECTOR")
        self.geometry("1200x800")
        self.minsize(1000, 600)
        
        # Initialize theme state
        self.current_theme = Theme.get_system_mode()
        
        # Configure ttk styles
        self.style = ttk.Style()
        self.style.theme_use('default')  # Use default theme as base
        
        # Set up main container
        self.main_container = ttk.Frame(self)
        self.main_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Create header
        self.header = self._create_header()
        
        # Create content area with grid
        self.content = self._create_content()
        
        # Create footer
        self.footer = self._create_footer()
        
        # Apply initial theme
        self._apply_theme()
    
    def _create_header(self):
        """Create the header section with title and theme toggle."""
        header = ttk.Frame(self.main_container, style="App.TFrame")
        header.pack(fill=tk.X, pady=(0, 20))
        
        # Title
        title = ttk.Label(
            header,
            text="META INJECTOR",
            font=("Helvetica Neue", 24, "bold"),
            style="Header.TLabel"
        )
        title.pack(side=tk.LEFT)
        
        # Theme toggle
        theme_btn = ttk.Button(
            header,
            text="TOGGLE THEME",
            command=self._toggle_theme,
            style="Toggle.TButton"
        )
        theme_btn.pack(side=tk.RIGHT)
        
        return header
    
    def _create_content(self):
        """Create the main content area with grid layout."""
        content = ttk.Frame(self.main_container, style="App.TFrame")
        content.pack(fill=tk.BOTH, expand=True)
        
        # Configure grid
        content.grid_columnconfigure(0, weight=1)  # Metadata section
        content.grid_columnconfigure(1, weight=1)  # Processing section
        content.grid_rowconfigure(1, weight=1)     # Main content area
        
        # Section headers
        ttk.Label(
            content,
            text="METADATA CONTROL",
            font=Theme.HEADER_FONT,
            style="Header.TLabel"
        ).grid(row=0, column=0, sticky="w", pady=(0, 10))
        
        ttk.Label(
            content,
            text="FILE PROCESSING",
            font=Theme.HEADER_FONT,
            style="Header.TLabel"
        ).grid(row=0, column=1, sticky="w", pady=(0, 10))
        
        # Create sections with rounded corners
        colors = Theme.get_colors(self.current_theme)
        
        # Metadata section
        metadata_frame = RoundedFrame(
            content,
            background=colors["container"],
            highlightbackground=colors["border"],
            highlightthickness=1,
            fixed_size=False  # This frame should resize with the window
        )
        metadata_frame.grid(row=1, column=0, sticky="nsew", padx=(0, 10))
        
        # Processing section
        processing_frame = RoundedFrame(
            content,
            background=colors["container"],
            highlightbackground=colors["border"],
            highlightthickness=1,
            fixed_size=False  # This frame should resize with the window
        )
        processing_frame.grid(row=1, column=1, sticky="nsew", padx=(10, 0))
        
        return content
    
    def _create_footer(self):
        """Create the footer section with status and controls."""
        footer = ttk.Frame(self.main_container, style="App.TFrame")
        footer.pack(fill=tk.X, pady=(20, 0))
        
        # Status label
        status = ttk.Label(
            footer,
            text="Ready",
            font=("Roboto Mono", 12),
            style="Status.TLabel"
        )
        status.pack(side=tk.LEFT)
        
        # Action buttons
        action_frame = ttk.Frame(footer, style="App.TFrame")
        action_frame.pack(side=tk.RIGHT)
        
        process_btn = ttk.Button(
            action_frame,
            text="PROCESS FILES",
            style="Action.TButton"
        )
        process_btn.pack(side=tk.RIGHT, padx=(10, 0))
        
        return footer
    
    def _toggle_theme(self):
        """Toggle between light and dark themes."""
        self.current_theme = Mode.LIGHT if self.current_theme == Mode.DARK else Mode.DARK
        self._apply_theme()
    
    def _apply_theme(self):
        """Apply the current theme to all widgets."""
        colors = Theme.get_colors(self.current_theme)
        
        # Configure base frame style
        self.style.configure(
            "App.TFrame",
            background=colors["background"]
        )
        
        # Header styles
        self.style.configure(
            "Header.TLabel",
            foreground=colors["text"],
            background=colors["background"]
        )
        
        self.style.configure(
            "SubHeader.TLabel",
            foreground=colors["text"],
            background=colors["background"]
        )
        
        # Button styles
        self.style.configure(
            "Toggle.TButton",
            font=("Roboto Mono", 12, "bold"),
            padding=10,
            background=colors["button"]["bg"],
            foreground=colors["button"]["fg"]
        )
        self.style.map(
            "Toggle.TButton",
            background=[("active", colors["button"]["hover_bg"])],
            foreground=[("active", colors["button"]["hover_fg"])]
        )
        
        self.style.configure(
            "Action.TButton",
            font=("Roboto Mono", 12, "bold"),
            padding=10,
            background=colors["button"]["bg"],
            foreground=colors["button"]["fg"]
        )
        self.style.map(
            "Action.TButton",
            background=[("active", colors["button"]["hover_bg"])],
            foreground=[("active", colors["button"]["hover_fg"])]
        )
        
        # Status style
        self.style.configure(
            "Status.TLabel",
            foreground=colors["text"],
            background=colors["background"]
        )
        
        # Update window colors
        self.configure(bg=colors["background"])
        self.main_container.configure(style="App.TFrame")
        
        # Update section frames
        for widget in self.content.winfo_children():
            if isinstance(widget, RoundedFrame):
                widget.configure(
                    background=colors["container"],
                    highlightbackground=colors["border"]
                )
                widget._draw_rounded_rect()
