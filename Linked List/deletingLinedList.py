# Implementation of a singly linked list with insertion operations and deletion


# Definition of a node in the linked list
class node:                                                                # Node class to represent each element in the linked list
    def __init__(self, value):                                             # Constructor to initialize the node with a value and a next pointer
        self.val = value                                                   # Value of the node
        self.next = None                                                   # Pointer to the next node in the linked list

# Definition of the linked list
class LinkedList:                                                          # LinkedList class to manage the linked list operations
    def __init__(self):                                                    # Constructor to initialize the linked list with a head pointer
        self.head = None                                                   # Head pointer of the linked list to store the first node
    
    def printLinkedList(self):                                             # Method to print the linked list
        temp = self.head                                                   # Start from the head of the linked list
        while temp != None:                                                # Traverse until the end of the linked list
            print(temp.val, end=" -> ")                                    # Print the value of the current node
            temp = temp.next                                               # Move to the next node
    
    def insertionAtTail(self, value):                                        # Method to insert a new node at the tail of the linked list
        if self.head == None:                                              # Checking if the linked list is empty to insert the first node
            self.head = node(value)                                        # If empty, create a new node and set it as the head
            return                                                         # Return after inserting the first node
        
        temp = self.head                                                  # Start from the head to find the tail of the linked list
        while temp.next != None:                                          # Traverse until the last node (tail) is reached
            temp = temp.next                                              # Move to the next node
        temp.next = node(value)                                           # Create a new node and link it as the next of the last node

    def insertionAtHead(self, value):                                        # Method to insert a new node at the head of the linked list
        new_node = node(value)                                             # Create a new node with the given value
        new_node.next = self.head                                         # Link the new node to the current head
        self.head = new_node                                              # Update the head to point to the new node

    def insertionAtPosition(self, position, value):                          # Method to insert a new node at a specific position in the linked list
        if position == 0:                                                  # If the position is 0, insert at the head
            self.insertionAtHead(value)                                   # Call the method to insert at head
            return                                                         # Return after insertion
        
        count = 2                                                      # Initialize a counter to track the current position
        temp = self.head                                                  # Start from the head of the linked list
        while count < position and temp != None:                                      # Traverse until the desired position or end of the list
            temp = temp.next                                              # Move to the next node
            count += 1                                                   # Increment the position counter
        
        if count < position:                                               # If the desired position is beyond the current length of the list
            print("Position out of bounds")                               # Print an error message
            return                                                         # Return without insertion
        
        rest = temp.next                                               # Store the reference to the next node
        temp.next = node(value)                                           # Create a new node and link it at the desired position
        temp.next.next = rest                                            # Link the new node to the rest of the list

    def deleteAtPosition(self, position):                                # Method to delete a node at a specific position in the linked list
        if position == 1:                                                  # If the position is 1, delete the head node
            if self.head is not None:                                     # Check if the linked list is not empty
                self.head = self.head.next                                # Update the head to point to the next node
            return                                                         # Return after deletion
        count = 2                                                      # Initialize a counter to track the current position
        temp = self.head                                                  # Start from the head of the linked list
        while count < position and temp != None:                                      # Traverse until the desired position or end of the list
            count += 1                                                   # Increment the position counter
            temp = temp.next                                              # Move to the next node
        
        if count < position:                                               # If the desired position is beyond the current length of the list
            print("Position out of bounds")                               # Print an error message
            return                                                         # Return without deletion
        
        temp.next = temp.next.next                                      # Bypass the node at the desired position to delete it


LinkedList = LinkedList()                                                  # Create an instance of the LinkedList class
LinkedList.printLinkedList()                                               # Print the linked list (should be empty initially)
print("After Insertion at Tail:")                                          # Print a message indicating the next operations
LinkedList.insertionAtTail(1)                                              # Insert elements at the tail of the linked list
LinkedList.insertionAtTail(2)                                              # Insert elements at the tail of the linked list
LinkedList.insertionAtTail(3)                                              # Insert elements at the tail of the linked list
LinkedList.insertionAtTail(4)                                              # Insert elements at the tail of the linked list
LinkedList.insertionAtTail(5)                                              # Insert elements at the tail of the linked list
LinkedList.printLinkedList()                                               # Print the linked list
print("\nAfter Insertion at Head:")                           # Print a message indicating the next operations
LinkedList.insertionAtHead(10)                                            # Insert element at the head of the linked list
LinkedList.insertionAtHead(20)                                            # Insert element at the head of the linked list
LinkedList.printLinkedList()                                              # Print the linked list
print("\nAfter Insertion at Position 3 and 5")                            # Print a newline for better readability
LinkedList.insertionAtPosition(3, 25)                                    # Insert element at position 3 of the linked list
LinkedList.insertionAtPosition(5, 30)                                    # Insert element at position 5 of the linked list
LinkedList.printLinkedList()                                              # Print the linked list
print("\nAfter Deletion at Position 1, 4 and 6")                           # Print a message indicating the next operations
LinkedList.deleteAtPosition(1)                                           # Delete node at position 1 of the linked list
LinkedList.deleteAtPosition(4)                                           # Delete node at position 4 of the linked list
LinkedList.deleteAtPosition(6)                                           # Delete node at position 6 of the linked list
LinkedList.printLinkedList()                                              # Print the linked list