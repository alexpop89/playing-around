from datetime import datetime


# The function takes one parameter, birth_date_str, which is a string representing the birthdate in the format
# mm-dd-yyyy
def calculate_age(birth_date_str):

    # Parse the input date string (The strptime method of the datetime class converts the birth_date_str into a
    # datetime object. The format string '%m-%d-%Y' specifies that the input string should be parsed as month (%m),
    # day (%d), and year (%Y).)
    birth_date = datetime.strptime(birth_date_str, "%m-%d-%Y")

    today = datetime.today()

    age = today.year - birth_date.year

    # Adjust the age if the birthday hasn't occurred yet this year (If the current month (today.month) is less than
    # the birth month (birth_date.month), it means the birthday hasn't occurred yet this year, so we subtract one
    # from the initial age. If the current month is the same as the birth month but the current day (today.day) is
    # less than the birthday (birth_date.day), the birthday also hasn't occurred yet, so we subtract one from the
    # initial age.)
    if today.month < birth_date.month or (today.month == birth_date.month and today.day < birth_date.day):
        age -= 1

    # Return the calculated age:
    return age


name = input("Hello, what is your name?: ")
birth_date_str = input("Now what is your birthday? (mm-dd-yyyy): ")
years_left = 100 - calculate_age(birth_date_str)

age = calculate_age(birth_date_str)
print('Hi ' + name + ', since you are currently ' + str(age) + " you'll be 100 years old in " + str(years_left) + ' years.')
