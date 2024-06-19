from datetime import datetime

name = input("Hello, what is your name?: ")
dob = input("Now what is your birthday? (mm-dd-yyyy): ")

# Parse the date string into a datetime object
date_obj = datetime.strptime(dob, "%m-%d-%Y")

# Get the year from the datetime object
dob_year = date_obj.year
current_year = datetime.now().year
age = current_year - dob_year

print("Hello " + name + ". You are currently " + str(age) + ".")
years_left = 100 - age
print("Since you are currently " + str(age) + " you'll be 100 in " + str(years_left) + " years.")
