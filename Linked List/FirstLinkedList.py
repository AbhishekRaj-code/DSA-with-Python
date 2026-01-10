# Program to create a simple linked list and insert elements at the tail

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
    
    def instionAtTail(self, value):                                        # Method to insert a new node at the tail of the linked list
        if self.head == None:                                              # Checking if the linked list is empty to insert the first node
            self.head = node(value)                                        # If empty, create a new node and set it as the head
            return                                                         # Return after inserting the first node
        
        temp = self.head                                                  # Start from the head to find the tail of the linked list
        while temp.next != None:                                          # Traverse until the last node (tail) is reached
            temp = temp.next                                              # Move to the next node
        temp.next = node(value)                                           # Create a new node and link it as the next of the last node

LinkedList = LinkedList()                                                # Create an instance of the LinkedList class
LinkedList.instionAtTail(1)                                              # Insert elements at the tail of the linked list
LinkedList.instionAtTail(2)                                              # Insert elements at the tail of the linked list
LinkedList.instionAtTail(3)                                              # Insert elements at the tail of the linked list
LinkedList.instionAtTail(4)                                              # Insert elements at the tail of the linked list
LinkedList.instionAtTail(5)                                              # Insert elements at the tail of the linked list

LinkedList.printLinkedList()                                              # Print the linked list