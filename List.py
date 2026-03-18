hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

# Step 1: write a line of code that prompts the user
# to replace the middle number with an integer number entered by the user.
userNumber = int(input("Enter a number to replace the middle number:"))
hat_list[2] = userNumber

# Step 2: write a line of code that removes the last element from the list.
del hat_list[4]
# Step 3: write a line of code that prints the length of the existing list.
hat_list_length = len(hat_list)
print("The length of the hat list:", hat_list_length)
print(hat_list)

