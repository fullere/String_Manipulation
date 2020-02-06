# Elizabeth Fuller
# 2/5/2020
# string manipulation

print("Please enter a string of words separated by commas.")
print("ex: dog, cat, pizza, house")
print("Hit ENTER when done.")
user_string = input("> ")

length = len(user_string)
first_letter = user_string[0]
last_letter = user_string[-1]
usr_string = user_string[:2]+user_string[3:]
split_string = user_string.split()
print(f"\nThis is the length of the string: {length}")
print(f"First letter of the string: {first_letter}")
print(f"Last letter of the string: {last_letter}")
print(f"This is the string without the third character:\n{usr_string}")
print(f"This is the string in all caps:\n{user_string.upper()}")
print(f"This is the string if it were a title:\n{user_string.title()}")

char_val = user_string.isalpha()
if char_val == True:
    print(f"The string only has alphabetic characters.")
else:
    print("the string does not contain only alphabetic characters.")

print(f"This is the string split apart:\n{split_string}")
str2 = 'a'
print("This is the location of the first 'a' in the string: "+str(user_string.find(str2)))
