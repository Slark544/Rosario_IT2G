
# Queue Name Operations

from collections import deque

print("=== QUEUE NAME OPERATIONS ===")

letterQueue = deque()

lastName = input("Enter your last name: ").upper()

# Phase 1: Enqueue each letter
print("\n--- Enqueuing Letters ---")

for ch in lastName:
    letterQueue.append(ch)

    print("Enqueued:", ch)

# Phase 2: Dequeue each letter until empty
print("\n--- Dequeuing Letters ---")

while len(letterQueue) > 0:
    dequeuedChar = letterQueue.popleft()

    print("Dequeued:", dequeuedChar)

print("\nQueue is now empty.")
