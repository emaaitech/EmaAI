def get_user_mood():
    """
    Get the user's mood input either directly or through a series of questions.
    Returns a dictionary containing the user's mood description and a calculated mood score.
    """
    print("\nChoose your mood input method:")
    print("1. Direct Input")
    print("2. Question-Based")
    
    choice = input("Enter the number of your choice: ")
    
    if choice == '1':
        return direct_input_mode()
    elif choice == '2':
        return question_based_mode()
    else:
        print("Invalid choice. Please try again.")
        return None

def direct_input_mode():
    """
    Allow the user to directly input their mood.
    Returns a dictionary containing the user's mood description and score.
    """
    mood_description = input("Please enter your current emotional state (e.g., happy, sad, stressed): ")
    
    # A simple mood score calculation (can be improved based on mood descriptions)
    mood_score = calculate_mood_score(mood_description)
    
    return {
        "description": mood_description,
        "score": mood_score
    }

def question_based_mode():
    """
    Ask a series of questions to determine the user's mood.
    Returns a dictionary containing the user's mood description and score.
    """
    print("\nAnswer the following questions to help me understand your mood:")
    
    # Example questions
    questions = [
        ("How are you feeling right now?", ["happy", "neutral", "sad"]),
        ("Are you stressed?", ["yes", "no"]),
        ("Have you been sleeping well?", ["yes", "no"])
    ]
    
    mood_responses = []
    
    for question, options in questions:
        print(f"{question} ({', '.join(options)})")
        response = input("Your answer: ").lower()
        
        while response not in options:
            print(f"Invalid response. Please choose from: {', '.join(options)}")
            response = input("Your answer: ").lower()
        
        mood_responses.append(response)
    
    # Calculate mood score based on answers
    mood_score = calculate_mood_score(mood_responses)
    
    # Based on responses, set the mood description
    mood_description = "Neutral"
    if "happy" in mood_responses:
        mood_description = "Happy"
    elif "sad" in mood_responses:
        mood_description = "Sad"
    
    return {
        "description": mood_description,
        "score": mood_score
    }

def calculate_mood_score(mood_data):
    """
    Calculate the mood score based on user input.
    For simplicity, return a score between 1-10 based on responses.
    """
    if isinstance(mood_data, str):  # Direct input mode
        mood_data = mood_data.lower()
        if "happy" in mood_data:
            return 8
        elif "sad" in mood_data:
            return 3
        elif "stressed" in mood_data:
            return 4
        else:
            return 5
    else:  # Question-based mode
        score = 0
        if "happy" in mood_data:
            score += 3
        if "yes" in mood_data:
            score += 2
        if "sad" in mood_data:
            score -= 2
        
        return max(1, min(10, score))  # Ensure the score is between 1 and 10
