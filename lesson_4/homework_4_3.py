# WHILE LOOPS EXERCISES

# Enter a random string in the variable string_1, then enter a character and save it in the variable char_1.
# Write code, which will count how many times your character is included in your string.
# Save result to result_1 variable

string_1 = "Michael Jordan was a superstar, but not as good as Jordan Miohael"
char_1 = 'a'
result_1 = string_1.lower().count(char_1)
print(result_1)

#another way using while

char_counter = 0
index = 0
while index < len(string_1):
    if char_1 in string_1.lower()[index]:
        char_counter += 1
    index += 1
print(char_counter)


# Enter a random number and save it in variable number_1. Then create code to multiply all the digits together
# and save result in the result_2 variable.

number_1 = 123456789
result_ = [x for x in str(number_1)]
result_2 = 1

for char in result_:
    result_2 *= int(char)
print(result_2)



# Enter a random number and save it in variable number_2. Then create code which will return
# a number with digits of number_1 in reverse order. Save it in result_3 variable

number_2 = 8475632381001
result_3 = int(str(number_2)[::-1])
print(result_3)