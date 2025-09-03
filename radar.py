# radar.py
# A simple weather radar viewer for Kochi, Kerala, India.

import tkinter as tk
from tkinter import messagebox
import urllib.request
import urllib.error
import io
import time
from PIL import Image, ImageTk

# --- Configuration ---
# Source URL for the Kochi weather radar image. This is the new HTTP link.
RADAR_URL = "http://117.221.70.132/dwr/radar/images/caz_koc.gif" # <<< THIS IS THE ONLY LINE THAT CHANGED
INITIAL_WINDOW_WIDTH = 600
INITIAL_WINDOW_HEIGHT = 650 # Includes space for buttons

class RadarApp:
    """
    A simple Tkinter application to display and refresh a weather radar image.
    """
    def __init__(self, root):
        self.root = root
        self.root.title("Kochi Weather Radar")
        self.root.geometry(f"{INITIAL_WINDOW_WIDTH}x{INITIAL_WINDOW_HEIGHT}")
        self.root.minsize(400, 450) # Set a minimum size for the window

        # This will hold the raw PIL Image object, acting as an in-memory cache.
        self.original_image = None
        # This reference is crucial to prevent the Tkinter image from being garbage-collected.
        self.tk_photo_image = None

        self._setup_ui()
        self.root.after(100, self.fetch_and_display_image) # Fetch image shortly after app starts
        self.root.bind('<Configure>', self.on_resize) # Bind resize event

    def _setup_ui(self):
        """Initializes the GUI components."""
        # Main frame
        main_frame = tk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Image label
        self.image_label = tk.Label(main_frame, bg='black')
        self.image_label.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Button frame
        button_frame = tk.Frame(self.root, pady=10)
        button_frame.pack(fill=tk.X)

        # Refresh button
        refresh_button = tk.Button(button_frame, text="Refresh", command=self.fetch_and_display_image)
        refresh_button.pack(side=tk.LEFT, expand=True, padx=10)

        # Close button
        close_button = tk.Button(button_frame, text="Close", command=self.root.destroy)
        close_button.pack(side=tk.RIGHT, expand=True, padx=10)

    def fetch_and_display_image(self):
        """
        Fetches the latest radar image from the URL, caches it, and triggers a display update.
        """
        print("Fetching latest radar image...")
        try:
            # Add a timestamp to the URL to bypass any caches (cache-busting)
            url = f"{RADAR_URL}?timestamp={int(time.time())}"
            
            with urllib.request.urlopen(url) as response:
                image_data = response.read()

            # Open the image data from memory
            image_stream = io.BytesIO(image_data)
            self.original_image = Image.open(image_stream)
            print("Image fetched successfully.")

            # Update the display with the new image
            self._update_image_display()

        except urllib.error.URLError as e:
            error_message = f"Failed to fetch radar image.\n\nPlease check your internet connection.\n\nError: {e}"
            messagebox.showerror("Network Error", error_message)
            print(f"Error: {e}")
            # If the first fetch fails, show a placeholder message
            if not self.original_image:
                 self.image_label.config(text="Could not load radar image.", bg='gray')


    def on_resize(self, event):
        """
        Handles the window resize event by scaling the cached image.
        This does NOT re-download the image.
        """
        self._update_image_display()
        
    def _update_image_display(self):
        """
        Scales the cached PIL image to fit the current window size and updates the label.
        """
        if self.original_image is None:
            return

        # Get the current size of the label widget
        label_width = self.image_label.winfo_width()
        label_height = self.image_label.winfo_height()

        # Avoid processing if the widget hasn't been drawn yet (width/height is 1)
        if label_width <= 1 or label_height <= 1:
            return

        # Create a copy to resize, preserving the original
        image_copy = self.original_image.copy()
        
        # The thumbnail method resizes the image in-place while maintaining aspect ratio
        image_copy.thumbnail((label_width, label_height), Image.Resampling.LANCZOS)

        # Convert the PIL image to a Tkinter-compatible photo image
        self.tk_photo_image = ImageTk.PhotoImage(image_copy)
        # Update the label with the new image
        self.image_label.config(image=self.tk_photo_image, text="")

def main():
    """The main function to run the application."""
    root = tk.Tk()
    app = RadarApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()