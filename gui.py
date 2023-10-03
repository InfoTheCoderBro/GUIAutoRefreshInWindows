# Import necessary libraries
import tkinter as tk              # For creating the GUI
from tkinter import messagebox   # For displaying message boxes
from cv2 import imread            # For image processing
from gui_automation import GuiAuto  # Custom library for GUI automation
import pyautogui                 # For mouse and keyboard automation
import sys                       # For system-related functionality
import os                        # For working with file paths

# Define a function to get the resource path, taking into account different environments
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS2  # Check if the script is packaged with PyInstaller
    except Exception:
        base_path = os.path.abspath(".")  # Use the current directory if not packaged

    return os.path.join(base_path, relative_path)

# Define the function responsible for refreshing the window
def RefreshWin():
    pyautogui.PAUSE = 0.1  # Set a pause between each action for better control
    
    timeRefresh = entry.get()  # Get the user input for the number of refreshes
    for i in range(int(timeRefresh)):
        screen_width, screen_height = pyautogui.size()  # Get the screen dimensions
        
        # Calculate the center of the screen
        x = screen_width / 2
        y = screen_height / 2
        
        # Simulate a right-click at the center of the screen
        pyautogui.rightClick(x, y)
        
        # Create an instance of GuiAuto for GUI automation
        Gcurser = GuiAuto()
        
        # Detect and click on the 'Refresh' button (assuming it's an image)
        if Gcurser.detect(imread('.\icon\Refresh.png'), 0.8):
            Gcurser.click()

# Create the main application window
root = tk.Tk()
root.title("AutoRefreshWin")  # Set the window title

# Create a label widget for user instructions
label = tk.Label(root, text="How many times do you want to refresh:")
label.pack()

# Create an entry widget for user input
entry = tk.Entry(root)
entry.pack()

# Create a button widget that triggers the RefreshWin function when clicked
button = tk.Button(root, text="Submit", command=RefreshWin)
button.pack()

# Start the main event loop for the GUI
root.mainloop()
