class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    def enqueue(self, item):
        if (self.rear + 1) % self.size == self.front:
            print("Queue Overflow! Cannot insert", item)
            return

        if self.front == -1:  # Queue is empty
            self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = item
        print(f"Inserted {item}. Front: {self.front}, Rear: {self.rear}")

    def dequeue(self):
        if self.front == -1:  # Queue is empty
            print("Queue Underflow! Cannot delete")
            return

        item = self.queue[self.front]
        self.queue[self.front] = None

        if self.front == self.rear:  # Queue becomes empty after this operation
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

        print(f"Deleted {item}. Front: {self.front}, Rear: {self.rear}")
        return item

    def display(self):
        if self.front == -1:  # Queue is empty
            print("Queue is empty")
            return

        print("Queue contents:", end=" ")
        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print(f"\nFront: {self.front}, Rear: {self.rear}")

# Interactive user input
def main():
    size = int(input("Enter the size of the circular queue: "))
    q = CircularQueue(size)

    while True:
        print("\nOperations:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Display")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            item = int(input("Enter the item to enqueue: "))
            q.enqueue(item)
        elif choice == 2:
            q.dequeue()
        elif choice == 3:
            q.display()
        elif choice == 4:
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
