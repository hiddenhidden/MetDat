"""
Common UI components for MetDat.
"""
import tkinter as tk

class RoundedFrame(tk.Canvas):
    """A frame with rounded corners and drop shadow."""
    
    # Predefined shadow colors from darkest to lightest
    SHADOW_COLORS = ['#A0A0A0', '#B0B0B0', '#C0C0C0']
    
    def __init__(self, parent, **kwargs):
        # Extract our custom parameters
        self.corner_radius = kwargs.pop('corner_radius', 10)
        self.shadow_size = kwargs.pop('shadow_size', 3)
        self.fixed_size = kwargs.pop('fixed_size', False)
        
        # Handle size
        self._width = kwargs.pop('width', None)
        self._height = kwargs.pop('height', None)
        
        if self._width:
            kwargs['width'] = self._width + self.shadow_size * 2
        if self._height:
            kwargs['height'] = self._height + self.shadow_size * 2
            
        super().__init__(parent, **kwargs)
        
        if not self.fixed_size:
            self.bind('<Configure>', self._on_resize)
        self._draw_rounded_rect()
    
    def _draw_rounded_rect(self):
        """Draw the rounded rectangle shape with shadow."""
        self.delete('all')  # Clear canvas
        
        # Get dimensions
        if self.fixed_size:
            width = self._width + self.shadow_size * 2
            height = self._height + self.shadow_size * 2
        else:
            width = self.winfo_width()
            height = self.winfo_height()
        
        # Draw shadow layers
        for i in range(min(self.shadow_size, len(self.SHADOW_COLORS))):
            offset = i + 1
            shadow_color = self.SHADOW_COLORS[i]
            
            self._create_rounded_rect(
                offset,
                offset,
                width - (self.shadow_size - offset),
                height - (self.shadow_size - offset),
                self.corner_radius,
                fill=shadow_color,
                outline=shadow_color
            )
        
        # Draw main rectangle
        self._create_rounded_rect(
            0,
            0,
            width - self.shadow_size,
            height - self.shadow_size,
            self.corner_radius,
            fill=self['background'],
            outline=self['highlightbackground']
        )
    
    def _create_rounded_rect(self, x1, y1, x2, y2, radius, **kwargs):
        """Create a rounded rectangle."""
        points = [
            x1 + radius, y1,
            x2 - radius, y1,
            x2, y1,
            x2, y1 + radius,
            x2, y2 - radius,
            x2, y2,
            x2 - radius, y2,
            x1 + radius, y2,
            x1, y2,
            x1, y2 - radius,
            x1, y1 + radius,
            x1, y1
        ]
        return self.create_polygon(points, smooth=True, **kwargs)
    
    def _on_resize(self, event):
        """Handle resize events."""
        if not self.fixed_size:
            self._draw_rounded_rect()
