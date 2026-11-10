
# Linked List Name Operations

print("=== LINKED LIST NAME OPERATIONS ===")

# Create a Node class
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# Initialize an empty linked list
class LinkedList:
    def __init__(self):
        self.head = None

    # Append a new node
    def append(self, value):
        newNode = Node(value)

        if self.head is None:
            self.head = newNode
        else:
            current = self.head

            while current.next is not None:
                current = current.next

            current.next = newNode

    # Remove the head node
    def removeHead(self):
        if self.head is not None:
            removedChar = self.head.value
            self.head = self.head.next

            return removedChar

        return None


nameList = LinkedList()

lastName = input("Enter your last name: ").upper()

# Phase 1: Add each letter as a node
print("\n--- Appending Nodes ---")

for ch in lastName:
    nameList.append(ch)

    print("Appended node:", ch)

# Phase 2: Remove nodes until empty
print("\n--- Removing Nodes ---")

while nameList.head is not None:
    removedChar = nameList.removeHead()

    print("Removed head node:", removedChar)

print("\nLinked List is now empty.")
