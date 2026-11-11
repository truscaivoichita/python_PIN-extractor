# Step 1
# In this workshop, you will create a PIN extractor. The PIN digits are hidden in each line of a poem.

# Start by creating a function called pin_extractor with a parameter poem. A function without a body raises an error, so add pass inside the function as a temporary placeholder to make it valid.

# Step 2
# You will need a variable to hold the secret code while you decode it, so remove pass and create a variable called secret_code inside the function and assign to it an empty string.

# Step 3
# While you work on the function, it would be useful to have a function call for debugging. Outside the function, create a poem variable that contains this poem:

# Example Code
# Stars and the moon
# shine in the sky
# white and bright
# until the end of the night
# You can use a multi-line string for that.

# Then call the function with the poem variable as an argument.

# Step 4
# Now that you have added a function call you can see any error created inside the function in the terminal, and you can always use print to see the value of things.

# There is a digit of the PIN hidden in every line, so use the split method inside the function to divide the string into a list of lines. Split the lines on the newline character (\n), and assign the resulting list to a variable called lines.

def pin_extractor(poem):
    secret_code = ""
    lines = poem.split("/n")
    # print(lines)
poem = "Stars and the moon\nshine in the sky\nwhite and bright\nuntil the end of the night"
pin_extractor(poem)
