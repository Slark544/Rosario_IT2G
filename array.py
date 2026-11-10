
# Array Name Operations

print("=== ARRAY NAME OPERATIONS ===")

lastName = input("Enter your last name (maximum 7 letters): ").upper()

# Initialize a fixed-size array of 7
letterArray = [None] * 7

if len(lastName) > 7 or len(lastName) == 0:
    print("Please enter 1 to 7 letters only.")
else:

    # Phase 1: Add each letter to the array
    index = 0

    print("\n--- Inserting Letters ---")

    while index < len(lastName):
        letterArray[index] = lastName[index]

        print("Inserted at index", index, ":", letterArray[index])

        index += 1

    # Phase 2: Remove each letter backwards
    index = len(lastName) - 1

    print("\n--- Removing Letters ---")

    while index >= 0:
        removedChar = letterArray[index]
        letterArray[index] = None

        print("Removed from index", index, ":", removedChar)

        index -= 1

    print("\nArray is now empty.")
