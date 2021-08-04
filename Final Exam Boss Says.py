# Aman Patel
# 817629
# ICS3U0C
# Final Summative Part 1 Question 1 Frequent2Letters
# 19 January 2018
# Mr. Veera

# Prompting user for input 
count = int(input("What is the count: "))

# Creating an empty list to store the values the boss says and assigning variables
boss_says = []
total = 0
count_2 = 0

# While loop to continue the process until count_2 is equal to count
while(count_2<count):
    # Prompting user for what the boss says 
    value = int(input("What does the boss say: "))
    # If condition to check if the value inputted is 0, if it is then used pop to get rid of the last value and adding 1 to count_2
    if (value == 0):
        boss_says.pop()
        count_2+=1
        # If the value does not equal 0 then it adds 1 to count and adds the value to list
    else:
        count_2+=1
        boss_says.append(value)
        # If condition to check if count_2 is equal to count and if it is then it will stop the loop 
        if (count_2 == count):
            break
        
# Calculating the sum of the list boss_says 
total = sum(boss_says)
# Outputting the total of the numbers in list 
print("The total is:",total)


