current_hours = 14
current_minutes = 34
current_seconds = 42


# Write a program that prints the remaining seconds (as an integer) from a
# day if the current time is represented bt the variables
currentInSec = (current_hours * 3600 + current_minutes * 60 + current_seconds)
print(currentInSec)
dayInSec = 86400
print(dayInSec - currentInSec)
