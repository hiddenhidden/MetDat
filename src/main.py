"""
Main entry point for the MetDat application.
"""
import time
from .ui import LoadingScreen, MainWindow

def main():
    # Create and show loading screen
    loading = LoadingScreen()
    
    # Simulate loading steps (this will be replaced with actual initialization)
    steps = [
        "Initializing application...",
        "Loading resources...",
        "Preparing interface...",
        "Starting MetDat..."
    ]
    
    for i, step in enumerate(steps):
        progress = (i + 1) * 25  # Calculate progress percentage
        loading.update_progress(progress, step)
        time.sleep(0.1)  # Quick progress update
    
    # Close loading screen
    loading.finish()
    
    # Create and run main window
    app = MainWindow()
    app.mainloop()
    
if __name__ == "__main__":
    main()
