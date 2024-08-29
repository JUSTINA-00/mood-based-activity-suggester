import tkinter as tk
from tkinter import messagebox

# Function to suggest activity based on mood and preferences
def suggest_activity():
    mood = mood_var.get()
    selected_preferences = [preference for i, preference in enumerate(preferences) if preferences_vars[i].get()]
    
    activities = {
        "happy": {
            "indoor": ["Watch a feel-good movie", "Do a puzzle", "Listen to music"],
            "outdoor": ["Go for a nature walk", "Play a sport", "Have a picnic"],
            "solo": ["Read a book", "Write in a journal", "Practice yoga"],
            "group": ["Play a board game", "Have a party", "Join a group workout"],
            "screen": ["Watch a movie", "Play video games", "Surf the web"],
            "no screen": ["Cook a meal", "Do some gardening", "Meditate"],
            "productive": ["Clean your room", "Learn a new skill", "Write a to-do list"],
            "leisure": ["Take a nap", "Play a musical instrument", "Listen to a podcast"]
        },
        "sad": {
            "indoor": ["Watch a comforting movie", "Read a book", "Take a warm bath"],
            "outdoor": ["Take a walk in nature", "Visit a quiet park", "Sit by a lake"],
            "solo": ["Write in a journal", "Listen to calming music", "Practice deep breathing"],
            "group": ["Spend time with close friends", "Attend a support group", "Have a game night"],
            "screen": ["Watch a movie", "Listen to a podcast", "Browse comforting websites"],
            "no screen": ["Cook a comforting meal", "Do some light stretching", "Practice mindfulness"],
            "productive": ["Organize your space", "Plan for the week ahead", "Create art or crafts"],
            "leisure": ["Take a nap", "Listen to calming music", "Read a comforting book"]
        },
        "angry": {
            "indoor": ["Break something (safely)", "Play a competitive game", "Clean or rearrange a space"],
            "outdoor": ["Go for a run", "Play a sport", "Do some landscaping or yard work"],
            "solo": ["Write in a journal", "Listen to aggressive music", "Punch a pillow"],
            "group": ["Play a team sport", "Have a karaoke night", "Join a martial arts class"],
            "screen": ["Watch an action movie", "Play a fast-paced video game", "Write a review"],
            "no screen": ["Do some physical exercise", "Do a craft or hobby", "Cook a spicy meal"],
            "productive": ["Clean your room", "Learn a new skill", "Write a to-do list"],
            "leisure": ["Take a nap", "Play a musical instrument", "Listen to a podcast"]
        },
        "bored": {
            "indoor": ["Learn a new skill", "Try a new hobby", "Explore a new genre of music"],
            "outdoor": ["Go for a hike", "Visit a new park", "Try geocaching"],
            "solo": ["Read a book", "Write in a journal", "Practice a new language"],
            "group": ["Play a board game", "Have a movie night", "Join a club"],
            "screen": ["Watch a documentary", "Play a puzzle game", "Browse a new website"],
            "no screen": ["Do some cooking or baking", "Do some gardening", "Try a new exercise"],
            "productive": ["Clean your room", "Organize your workspace", "Plan a project"],
            "leisure": ["Take a nap", "Listen to a podcast", "Play a musical instrument"]
        },
    }
    
    selected_activities = []
    for preference in selected_preferences:
        if preference in activities[mood]:
            selected_activities.extend(activities[mood][preference])
    
    if selected_activities:
        activities_output.config(text="\n".join(selected_activities))
    else:
        activities_output.config(text="No activity found for selected mood and preferences.")

# Create the main window
root = tk.Tk()
root.title("Activity Suggestion")
root.geometry("600x700")
root.configure(bg="purple")

# Define colors and fonts
bg_color = "pink"
font_style = ("Arial", 12)

# Mood selection
mood_frame = tk.Frame(root, bg=bg_color)
mood_frame.pack(pady=10)

mood_label = tk.Label(mood_frame, text="Select your mood:", font=font_style, bg=bg_color)
mood_label.grid(row=0, column=0, padx=5, pady=5)

moods = ["happy", "sad", "angry", "bored"]
mood_var = tk.StringVar()
mood_dropdown = tk.OptionMenu(mood_frame, mood_var, *moods)
mood_dropdown.config(font=font_style, bg=bg_color)
mood_dropdown.grid(row=0, column=1, padx=5, pady=5)

# Preferences selection
preferences_frame = tk.Frame(root, bg=bg_color)
preferences_frame.pack(pady=10)

preferences_label = tk.Label(preferences_frame, text="Select your preferences:", font=font_style, bg=bg_color)
preferences_label.grid(row=0, column=0, padx=5, pady=5)

preferences = ["indoor", "outdoor", "solo", "group", "screen", "no screen", "productive", "leisure"]
preferences_vars = []
for i, preference in enumerate(preferences):
    var = tk.IntVar()
    cb = tk.Checkbutton(preferences_frame, text=preference, variable=var, bg=bg_color, font=font_style)
    cb.grid(row=i//2+1, column=i%2, padx=5, pady=2, sticky="w")
    preferences_vars.append(var)

# Button to suggest activity
suggest_button = tk.Button(root, text="Suggest Activity", font=font_style, bg="orange", fg="black", command=suggest_activity)
suggest_button.pack(pady=10)

# Output label for suggested activity
activities_output = tk.Label(root, text="", font=font_style, bg="light blue", fg="black", wraplength=350, justify="left")
activities_output.pack(pady=10, padx=20)

root.mainloop()