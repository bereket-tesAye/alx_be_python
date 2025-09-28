# explore_datetime.py

from datetime import datetime, timedelta

# Part 1: Display the Current Date and Time
def display_current_datetime():
    # Save the current date and time
    current_date = datetime.now()

    # Format it as YYYY-MM-DD HH:MM:SS
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")

    # Print result
    print("Current date and time:", formatted_date)


# Part 2: Calculate a Future Date
def calculate_future_date():
    # Ask user for number of days
    number_of_days = int(input("Enter the number of days to add to the current date: "))

    # Current date and time
    current_date = datetime.now()

    # Calculate future date
    future_date = current_date + timedelta(days=number_of_days)

    # Format as YYYY-MM-DD
    formatted_future = future_date.strftime("%Y-%m-%d")

    # Print result
    print("Future date:", formatted_future)


# Run functions
if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()
