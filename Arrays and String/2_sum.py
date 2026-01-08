# Program to find elements in an array that sum to a given target
# O(n log n) time complexity due to sorting


# Function to find pairs in an array that sum to a given target
def find_pairs_with_sum(arr, target_sum): 
    temp = arr.copy()                                                                      # Create a copy of the original array to preserve indices
    l1 =0                                                                                  # index of first element
    l2 =0                                                                                  # index of second element
    arr.sort()                                                                             # Sort the array to use two-pointer technique

    start = 0                                                                              # Initialize start pointer 
    end = len(arr) - 1                                                                     # Initialize end pointer

    while start < end:                                                                     # Loop until the two pointers meet or cross
        current_sum = arr[start] + arr[end]                                                # Calculate the sum of elements at the two pointers 
        if current_sum == target_sum:                                                      # If the sum matches the target sum then we found a pair
            for i in range(len(temp)):                                                     # Loop through the original array to find the indices of the elements
                if temp[i] == arr[start]:                                                  # Find the indices of the elements
                    l1 = i                                                                 # Store the index of the first element
                if temp[i] == arr[end]:                                                    # Find the index of the second element
                    l2 = i                                                                 # Store the index of the second element
            show_pairs([(arr[start], arr[end])], (l1, l2), temp, target_sum)               # Display the pair found along with their indices
            break                                                                          # Exit the loop
        elif current_sum < target_sum:                                                     # If the current sum is less than the target sum, move the start pointer to the right
            start += 1                                                                     # Move the start pointer to the right
        else:                                                                              # If the current sum is greater than the target sum, move the end pointer to the left
            end -= 1                                                                       # Move the end pointer to the left

# Function to display the pairs found
def show_pairs(pairs, location, arr, target): 
    print(f"Original array: {arr}")                                                        # Print the original array
    print(f"Target sum: {target}")                                                         # Print the target sum
    print(f"Pairs found at {location}: {pairs}")                                           # Print the pairs found along with their indices


# Main function to take input and call the find_pairs_with_sum function
def main():
    arr = input("Enter the array elements separated by space: ").split()                   # Take input from the user and split it into an array
    arr = [int(x) for x in arr]                                                            # Convert the elements from string to integer
    target_sum = int(input("Enter the target sum: "))                                      # Take the target sum as input from the user
    find_pairs_with_sum(arr, target_sum)                                                   # Call the find_pairs_with_sum function
    
# Check if the script is being run directly
if __name__ == "__main__": 
    main()                                                                                 # Call the main function to execute the program