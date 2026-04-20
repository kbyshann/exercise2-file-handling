try:
    note = input("Enter a short note: ")
    with open("notes.txt", "w") as file:
        file.write(note)

    # STEP 2: Read
    with open("notes.txt", "r") as file:
        print("\nFile content:")
        print(file.read())

    # STEP 3: Append
    new_note = input("\nEnter another note: ")
    with open("notes.txt", "a") as file:
        file.write("\n" + new_note)

    # Display updated content
    with open("notes.txt", "r") as file:
        print("\nUpdated content:")
        print(file.read())

except FileNotFoundError:
    print("Error: File not found.")