
# Stack Name Operations

print("=== STACK NAME OPERATIONS ===")

letterStack = []

lastName = input("Enter your last name: ").upper()

# Phase 1: Push each letter into the stack
print("\n--- Pushing Letters ---")

for ch in lastName:
    letterStack.append(ch)

    print("Pushed:", ch)

# Phase 2: Pop each letter until empty
print("\n--- Popping Letters ---")

while len(letterStack) > 0:
    poppedChar = letterStack.pop()

    print("Popped:", poppedChar)

print("\nStack is now empty.")
