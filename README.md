# **EmaAI: Emotion and Mood Assistant AI**

EmaAI is an intelligent mood-tracking and suggestion system designed to help users improve their emotional well-being. By leveraging Python, the OpenAI API, and advanced data visualization techniques, EmaAI offers personalized suggestions based on user inputs and tracks mood changes over time.

---

## **Table of Contents**
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

---

## **Overview**

EmaAI is designed to provide emotional support and mood-tracking capabilities. It uses artificial intelligence (AI) powered by the OpenAI API to offer personalized suggestions that can help improve mood based on user input. The system also tracks mood changes over time and provides insightful visualizations.

The application has two main modes for mood input:
1. **Direct Input Mode**: Users enter their current emotional state directly.
2. **Question-Based Mode**: EmaAI asks the user a series of questions to evaluate their emotional state.

By analyzing mood data, the AI offers suggestions like engaging in physical activities, taking breaks, or practicing mindfulness.

---

## **Features**

- **Two Modes of Mood Input**:
  - **Direct Input**: User provides mood input directly.
  - **Question-Based**: User answers questions to help EmaAI assess mood.
  
- **Personalized Suggestions**: Based on user input, EmaAI generates tailored suggestions to improve emotional well-being.
  
- **Mood Score**: EmaAI calculates a mood score reflecting the effectiveness of the suggestions and tracks improvement over time.
  
- **Data Visualization**: EmaAI tracks mood trends and visualizes the data using graphs.
  
- **CSV Data Management**: User mood data and suggestions are stored in CSV files for easy access and export.
  
- **Easy-to-Use GUI**: Built with Tkinter or PyQt for an intuitive, user-friendly interface.
  
- **Data Security and Privacy**: User data is securely stored, and privacy is prioritized.

---

## **Installation**

Follow these steps to install and run **EmaAI** on your local machine.

### Prerequisites
1. **Python 3.7+**
2. **Pip** (for installing dependencies)

### Step 1: Clone the repository
```bash
git clone https://github.com/yourusername/EmaAI.git
cd EmaAI
```

### Step 2: Clone the repository
```bash
pip install -r requirements.txt
```

### This will install the following libraries:

- **``openai``** – For accessing the OpenAI API to generate mood-enhancing suggestions.
  
- **``matplotlib``** – For data visualization (plotting mood trends over time).
  
- **``tkinter``** or PyQt – For GUI development (depending on your choice).
  
- **``csv``** – For handling mood data storage in CSV files.
  
#### If you're using a specific virtual environment, make sure to activate it before running the ``pip install`` command.

### Step 3: Set up the OpenAI API
To generate suggestions, you'll need to set up your OpenAI API key.

 1. Visit OpenAI's website and create an API key if you haven't already.
 2. Replace ``'your-openai-api-key'`` in the ``suggestions_engine.py`` file with your actual API key.

```bash
openai.api_key = 'your-openai-api-key'
```

### Step 4: Run the application
Once you've installed all dependencies and set up the API key, you can start the application by running:

```bash
python main.py
```


### Notes:
- **Replace placeholders**: Update `yourusername` with your actual GitHub username.
- **Screenshot**: Add a screenshot of the GUI under the **Screenshots** section by replacing `path_to_screenshot_image.png` with the actual image file path.
- **License**: You can either include a `LICENSE` file in your project or adjust the **License** section according to your preferences.

This should provide a complete overview and guide for users and contributors to your **EmaAI** project.

Let me know if you'd like to make any further adjustments!

