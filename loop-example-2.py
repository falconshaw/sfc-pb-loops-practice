print("-----------------------------------")    
print("Galvanize Sticker Printer Service:")
print("Dynamic Images")


### ------------------------------ Image 1 ------------------------------ ###
print("\n")
print("Image 1: Making Varying Length and Varying Character Stickers")
### Use the variables and pseudocode below to print the following pattern:
### **
### vvvvv
### xxxxxxxxxx

characters = ["*", "v", "x"]
row_length = [2, 5, 10]

### Use a for loop to iterate through the characters list.
### Make an empty print statement inside the for loop.
### Use another for loop to iterate through the corresponding row_length list.
### Inside the nested for loop, print the character at the current outer index.


### ------------------------------ Image 2 ------------------------------ ###
print("\n")
print("Image 2: Another Varying Length and Varying Character Stickers")
### Use the variables and pseudocode below to print the following pattern:
### **
### vvvvv
### xxxxxxxxxx

characters = ["*", "v", "x"]
row_length = [2, 5, 10]

### Create a counter variable and set it to 0.
### Use a while loop to iterate through the characters list.
### Make an empty print statement inside the while loop.
### Create an inner counter variable and set it to 0.
### Use another while loop to iterate through the corresponding row_length list.
### Inside the nested while loop, print the character at the current outer index.
### Inside the nested while loop, increment the inner counter.
### Outside the nested while loop, increment the outer counter.



### ------------------------------ Image 3 ------------------------------ ###
print("\n")
print("Image 3: User Input Custom Stickers")
### Use the variables and pseudocode below to make stickers based on user input:

### A user session might look like:

### Enter the number of the columns: 5
### Enter the character for row 1: M
### Enter the number of characters in row 1: 10
### Enter the character for row 2: xo
### Enter the number of characters in row 2: 5
### Enter the character for row 3: OX
### Enter the number of characters in row 3: 5
### Enter the character for row 4: xo 
### Enter the number of characters in row 4: 5
### Enter the character for row 5: W
### Enter the number of characters in row 5: 10
### MMMMMMMMMM
### xoxoxoxoxo
### OXOXOXOXOX
### xoxoxoxoxo
### WWWWWWWWWW
### Enter y to make another sticker: 

go_again = "y"

### Create a while loop that will run as long as go_again is "y".
    ### Create an empty list called chars.
    ### Create an empty list called row_lengths.
    ### Ask the user to input the number of columns.
    ### Nested loop over the number of columns.
        ### Inside the loop, ask the user to input a character for the current row.
        ### Inside the loop, ask the user to input a number of characters for the current row.
        ### Add each to the appropriate empty list.
    ### In a separate loop, iterate over the number of columns.
        ### Inside the loop, iterate over the number of characters for the current row.
            ### Print the character for the current row.
        ### Print a new line in the column length loop level.
    ### In the outermost loop, get the user's input and store it in go_again.


