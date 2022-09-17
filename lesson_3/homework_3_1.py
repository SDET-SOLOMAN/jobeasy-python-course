# Enter two numbers. If the first one is greater than the second, save first number in result_1,
# otherwise save the second number to the result_1 variable.

first_number = 23
second_number = 32
result_1 = first_number if first_number > second_number else second_number
print(result_1)

# Enter a random number in number_1 variable. If this number is 20 or
# higher save “Too high” text to result_2, otherwise save “Thank you”.
number_1 = 32
result_2 = "Too high" if number_1 >= 20 else "Thank you"
print(result_2)

# Enter your first name and last name in first_name and last_name variables. If the length of your first name is under
# five characters, join them together (without a space) and save it to result_3 variable in upper case. If the length
# of the first name is five or more characters, save their first name in lower case in result_3 variable.

first_name = "Sdet"
last_name = "Soloman"
result_3 = first_name + " " + last_name if len(first_name) < 5 else first_name.lower()
print(result_3)


# Enter a number between 10 and 20 (inclusive) and save number to number_2 variable
# If they enter a number within this range, save a message “Thank you” to result_4, otherwise a
# message “Incorrect answer” to result_4.

number_2 = 10
result_4 = "Thank you" if 10 <= number_2 <= 20 else "incorrect Number"
print(result_4)


# Enter your age. If you are 18 or over, save the message “You can vote” in result_5,
# if you are aged 17, save the message “You can learn to drive” in result_5 variable,
# if you are 16, save the message “You can buy a lottery ticket” in result_5,
# if you are under 16, save the message “You can go Trick-or-Treating” in result_5 variable.

age = 33
result_5 = None
if age >= 18:
    result_5 = 'You can vote'
elif age >= 17:
    result_5 = 'You can learn to drive'
elif age >= 16:
    result_5 = 'You can buy a lottery ticket'
else:
    result_5 = 'You can go Trick-or-Treating'
print(result_5)


# Enter a number between 1 and 12, save this value to month variable. Find which month is it.
# (January, February, March, April, May, June, Jule, August, September, October, November, December)
# Write answer in result_month in lower case

month = 11
months = ['January', 'February', 'March', 'April', 'May', 'June', 'Jule', 'August', 'September',
          'October', 'November', 'December']
result_month = months[month - 1]
print(result_month)