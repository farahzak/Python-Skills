# Aman Patel
# 817629
# ICS3U0C
# Final Summative Part 1 Question 1 Frequent2Letters
# 19 January 2018
# Mr. Veera

# Prompting user for input
word = input("Enter a word which is atleast 6 characters: ")
# Assigning my variables and creating a list with the frequent characters in it.
frequent_letters = ["h","o","e","i"]
letters_seperate = []
frequent = 0
non_frequent = 0
word_length = len(word)

# If codition to strictly enforce that the word inputted must be greater than 6 characters long
if (word_length < 6):
    word = input("Enter a word which is atleast 6 characters: ")
else:
    for letter in word:
        letters_seperate.append(letter)
        
# I am puting the second letter in the list into another varible to then check if it is a frequent letter or not 
second_letter = letters_seperate[1]

# If condition to check if the second letter is one of the frequent letters 
if second_letter in frequent_letters:
    frequent+=1
else:
    non_frequent+=1

# Checking if the second letter is frequent and if it is then it will output that "the second letter is a frequent letter" and if it isn't then it will output "no the second letter is not a frequent letter".
if (frequent == 1):
    print("Yes, the second letter in",word,"is a frequent letter!")
else:
    print("No, the second letter in",word,"is not a frequent letter!")





