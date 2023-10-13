import datetime

# Get the current date and time
current_datetime = datetime.datetime.now()
print("Current Date and Time:", current_datetime)

# Get the current date
current_date = datetime.date.today()
print("Current Date:", current_date)

# Create a specific date
specific_date = datetime.date(2022, 12, 31)
print("Specific Date:", specific_date)

# Create a specific time
specific_time = datetime.time(12, 30, 45)
print("Specific Time:", specific_time)

# Format a date and time as a string
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted Date and Time:", formatted_datetime)

# Parse a string to a datetime object
parsed_datetime = datetime.datetime.strptime("2022-12-31 12:30:45", "%Y-%m-%d %H:%M:%S")
print("Parsed Date and Time:", parsed_datetime)

# Perform date arithmetic
future_date = current_date + datetime.timedelta(days=30)
print("Future Date:", future_date)

# Calculate the time difference between two dates
date1 = datetime.date(2022, 1, 1)
date2 = datetime.date(2022, 12, 31)
time_difference = date2 - date1
print("Time Difference:", time_difference.days, "days")
