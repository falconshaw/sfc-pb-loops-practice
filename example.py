print("Pretty Printer Text Formatter:")

print("Image 1: The Line")
###Use a for loop to print a line of 4 "X" characters.

print("\n")
print("Image 2: The Box")
###Complete the following pseudocode to create a box of 4 rows and 4 columns of
###the character "$".

###For each row of 4 rows
    ###For each column of 4 columns
        ###Print an "$"
    ###Print a newline


print("\n")
print("Image 3: The While Box")
###Complete the following code to create a box of an arbitrary size a user
###specified character.

continue_box = "y"
##Add a loop that will continue while continue_box is equal to "y"
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of cols: "))
    character = input("Enter the character that should be printed: ")

    ##Add a nested loop that will print a box of the size specified by the user
        ###Print the character specified by the user

    continue_box = input("\nDo you want to continue? (y/n): ")

print("\n")
print("Image 4: The Triangle")
###Follow the following pseudocode to create a 4 row tall triangle composed of 
###the character "X".

###The first row should contain 1 "X", with each subsequent row containing one 
###additional "X".

#Set Len to 0
##Enter row loop here
    ##Print a space
    ##Increment len
    ##Use a loop to print len number of "X"s

print("\n")
print("Image 5: The Triangle Application")
###Complete all of the following code to create a triangle of an arbitrary
###size.

###The user should be able to continue to create triangles until 
### continue_program is equal to "n".

##Enter your code here

print("Program Completed!")