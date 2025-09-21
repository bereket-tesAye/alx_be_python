# daily_reminder.py

# Prompt for user input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process the task based on priority
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task"
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task"
    case "low":
        reminder = f"Note: '{task}' is a low priority task"
    case _:
        reminder = f"'{task}' has an unspecified priority. Please clarify."

# Adjust message based on time sensitivity
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
elif time_bound == "no":
    if priority == "low":
        reminder += ". Consider completing it when you have free time."
    else:
        reminder += ". Plan accordingly."

# Display the final reminder
print(reminder)
