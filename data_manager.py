# data_manager.py
import csv
import os
import matplotlib.pyplot as plt
from datetime import datetime

CSV_FILE = "mood_data.csv"

mood_data = {
    "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),  # Formatting the datetime
    "Mood": "Happy",
    "Mood Score": 8,
    "Suggestions": "Take a walk"
}

# Save to CSV
with open('mood_data.csv', mode='a', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=mood_data.keys())
    writer.writerow(mood_data)

def create_csv_file():
    """
    Creates the CSV file and adds headers if the file does not exist.
    """
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["Date", "Mood", "Mood Score", "Suggestions"])
            writer.writeheader()

def save_mood_data(mood_data):
    """
    Saves the user's mood data to the CSV file.
    :param mood_data: Dictionary containing the user's mood data (date, mood, score, suggestions).
    """
    create_csv_file()  # Ensure the CSV file exists and has headers
    
    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["Date", "Mood", "Mood Score", "Suggestions"])
        writer.writerow(mood_data)
    print(f"Mood data saved for {mood_data['Date']}")

def load_mood_data():
    """
    Loads and returns all the mood data stored in the CSV file.
    :return: List of dictionaries containing mood data.
    """
    mood_entries = []
    if os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                mood_entries.append(row)
    return mood_entries

def visualize_mood_data():
    """
    Visualizes mood data over time by plotting mood scores.
    """
    mood_entries = load_mood_data()
    if not mood_entries:
        print("No mood data to visualize.")
        return
    
    # Extract date and mood score from the loaded data
    dates = [entry['Date'] for entry in mood_entries]
    mood_scores = [int(entry['Mood Score']) for entry in mood_entries]
    
    # Create the plot
    plt.figure(figsize=(10, 6))
    plt.plot(dates, mood_scores, marker='o', linestyle='-', color='b', label="Mood Score")
    
    # Customize the plot
    plt.title("Mood Score Over Time")
    plt.xlabel("Date")
    plt.ylabel("Mood Score")
    plt.xticks(rotation=45, ha="right")
    plt.grid(True)
    plt.tight_layout()
    
    # Show the plot
    plt.show()
