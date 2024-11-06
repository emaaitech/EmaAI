# gui.py
import tkinter as tk
from tkinter import messagebox
from ttkthemes import ThemedTk
from tkinter import ttk
from suggestion_engine import generate_suggestions
from data_manager import save_mood_data, visualize_mood_data
from datetime import datetime

# Create the main window with a modern theme
root = ThemedTk()
root.set_theme("arc")  # Set a modern theme (arc is a popular one)

# Set window size and title
root.title("EmaAI - Mood Tracker")
root.geometry("450x500")

# Function to handle mood input and suggestion generation
def handle_input():
    # Get user mood input
    mood = mood_entry.get()
    
    if not mood:
        messagebox.showwarning("Input Error", "Please enter your mood.")
        return
    
    # Generate suggestion based on mood
    suggestion = generate_suggestions(mood)
    
    # Calculate a basic mood score (this can be improved later)
    mood_score = len(mood)  # Simple score based on mood length for demonstration
    
    # Display the suggestion and mood score
    suggestion_label.config(text=f"Suggested activity: {suggestion}")
    mood_score_label.config(text=f"Mood Score: {mood_score}")
    
    # Save the mood data
    mood_data = {
        "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Mood": mood,
        "Mood Score": mood_score,
        "Suggestions": suggestion
    }
    save_mood_data(mood_data)

# Function to visualize mood data over time
def show_graph():
    visualize_mood_data()

# Create the input field for mood
mood_label = ttk.Label(root, text="Enter your current mood:", font=("Arial", 12))
mood_label.pack(pady=10)

mood_entry = ttk.Entry(root, width=40, font=("Arial", 12))
mood_entry.pack(pady=5)

# Button to generate suggestions and save mood data
submit_button = ttk.Button(root, text="Submit Mood", command=handle_input, width=20)
submit_button.pack(pady=20)

# Label to display the generated suggestion
suggestion_label = ttk.Label(root, text="Suggested activity will appear here.", font=("Arial", 12), wraplength=350)
suggestion_label.pack(pady=5)

# Label to display the mood score
mood_score_label = ttk.Label(root, text="Mood Score will appear here.", font=("Arial", 12))
mood_score_label.pack(pady=5)

# Button to visualize mood trends
visualize_button = ttk.Button(root, text="Visualize Mood Trends", command=show_graph, width=20)
visualize_button.pack(pady=20)

# Start the GUI main loop
root.mainloop()
