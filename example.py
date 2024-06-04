print("Pretty Printer Text Formatter:")

print("Image 1: The Line")
for i in range(1, 4):
    print("X", end="")

print("\n")
print("Image 2: The Box")
for i in range(0, 4):
    print()
    for j in range(0, 4):
        print("X", end="")


print("\n")
print("Image 3: The While Box")
continue_box = "y"
while(continue_box == "y"):
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of cols: "))

    for j in range(0, rows):
        print()
        for j in range(0, cols):
            print("X", end="")

    continue_box = input("\nDo you want to continue? (y/n): ")

print("\n")
print("Image 4: The Triangle")

len = 0
for i in range(0, 4):
    print()
    len = len + 1
    for j in range(0, len):
        print("X", end="")

print("\n")
print("Image 5: The Triangle Application")
continue_program = True
while(continue_program):
    rows = int(input("Enter the number of rows: "))
    character = input("Enter the input character: ")

    len = 0
    for i in range(0, rows):
        print()
        len = len + 1
        for j in range(0, len):
            print(character, end="")
    
    if (input("\nDo you want to continue? (y/n): ") == "n"):
        continue_program = False
    else:
        continue_program = True

print("Program Completed!")