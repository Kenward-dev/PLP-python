with open("my_file.txt", "w") as file:
    
    file.write("Hello, this is the first line with some text.\n")
    file.write("The second line has a number: 12345\n")
    file.write("And the third line includes both text and numbers: 42 is the answer!\n")


print("my_file.txt has been created and written to successfully.")