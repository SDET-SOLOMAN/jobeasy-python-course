# Save to variable result_1 the first character of string_1 variable. In result_2 save the last character
# of string_1. Use indexes.

string_1 = 'Python'
result_1 = string_1[0]
result_2 = string_1[-1]


# Save to variable result_3 string value from string_2 variable, written in reverse order, using concatenation.

string_2 = 'Python'
result_3 = string_2[::-1]
result3_3 = string_2[-1::-1]
print(result_3)
print(result3_3)
result3_3_3 = ""
index = -1
for char in string_2:
    result3_3_3 += string_2[index]
    index -= 1
print(result3_3_3)


# Slice string string_3 from 5th to 20th (excluding 20th) character and save the result to variable result_4

string_3 = 'Python is a programming language that lets you work quickly and integrate systems more effectively'
result_4 = string_3[5:20]


# Slice string string_4 from 10th character to the end of the string. Save only every second character to variable
# result_5

string_4 = 'Python is a programming language that lets you work quickly and integrate systems more effectively'
result_5 = string_4[4::2]


# Slice string string_5 from the first to the last character, save only every forth character and
# save the result to variable result_6

string_5 = 'Python is a programming language that lets you work quickly and integrate systems more effectively'
result_6 = string_5[1:-1:4]


# Slice string string_6 from the first to 14th (including 14th) character, save only every third character and save
# the result to variable result_7

string_6 = 'Python is a programming language that lets you work quickly and integrate systems more effectively'
result_7 = string_6[1:14:3]


# Save to variable result_8 string value from string_7 variable, written in reverse order, using slicing.

string_7 = 'Python'
result_8 = string_7[::-1]


# Create a range of numbers from 0 to 10 (excluding 10) and save it to result_9 variable

result_9 = range(0,10)
