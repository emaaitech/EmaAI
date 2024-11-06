import csv
from datetime import datetime
from mood_input import get_user_mood
from suggestion_engine import generate_suggestions
from data_manager import save_mood_data, load_mood_data
from gui import start_gui

def main():
    print("Welcome to EmaAI - Your Emotional and Mood Assistant\n")

    try:
        # Step 1: Get user mood input (direct or question-based)
        user_mood = get_user_mood()
        
        if not user_mood:
            print("Error: Could not retrieve user mood. Please try again.")
            return

        # Step 2: Generate suggestions based on mood input
        suggestions = generate_suggestions(user_mood['description'])

        # If API call fails, handle it gracefully
        if not suggestions:
            print("Warning: Unable to retrieve suggestions at this time.")
            suggestions = "No suggestions available."

        # Step 3: Save mood data to CSV with current date and time
        mood_data = {
            "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Mood": user_mood['description'],  # user's mood description
            "Mood Score": user_mood['score'],  # computed score
            "Suggestions": suggestions
        }
        
        save_mood_data(mood_data)
        
        # Step 4: Display GUI for user interaction
        start_gui(mood_data)
        
    except Exception as e:
        print(f"An error occurred: {e}")
    
    print("\nThank you for using EmaAI. Take care!")

if __name__ == "__main__":
    main()
