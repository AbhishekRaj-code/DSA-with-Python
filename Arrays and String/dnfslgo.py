# Dutch National Flag Algorithm to sort an array of 0s, 1s, and 2s
# 3 pointers approach with O(n) time complexity and O(1) space complexity

# Function to implement Dutch National Flag Algorithm
def dnf_algoritm(arr):
    n = len(arr)                                                                              # Length of the array
    low = 0                                                                                   # Initialize low pointer
    mid = 0                                                                                   # Initialize mid pointer
    high = n - 1                                                                              # Initialize high pointer

    while mid <= high:                                                                         # Loop until mid pointer crosses high pointer
        if arr[mid] == 0:                                                                      # If the element is 0 then swap it with the element at low pointer beacause 0s should be at the beginning
            arr[low], arr[mid] = arr[mid], arr[low]                                            # Swap the elements at low and mid pointers
            low += 1                                                                           # Increment low pointer because we have placed a 0 at the beginning
            mid += 1                                                                           # Increment mid pointer to check the next element
        elif arr[mid] == 1:                                                                    # If the element is 1 then increment mid pointer because 1s should be in the middle
            mid += 1                                                                           # Just increment mid pointer to check the next element
        else:                                                                                  # If the element is 2 then swap it with the element at high pointer because 2s should be at the end
            arr[mid], arr[high] = arr[high], arr[mid]                                          # Swap the elements at mid and high pointers 
            high -= 1                                                                          # Decrement high pointer because we have placed a 2 at the end

    return arr                                                                                 # Return the sorted array

# Main function to take input and call the dnf_algorithm function
def main():
    arr = input("Enter the array elements (0s, 1s, and 2s) separated by space: ").split()      # Take input from the user and split it into an array
    arr = [int(x) for x in arr]                                                                # Convert the elements from string to integer
    print(f"Sorted array: {dnf_algoritm(arr)}")                                                # Call the dnf_algorithm function and print the sorted array

# Check if the script is being run directly
if __name__ == "__main__":
    main()                                                                                      # Call the main function