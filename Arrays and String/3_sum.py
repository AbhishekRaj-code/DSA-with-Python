# Program to find 3 elements in an array that sum to a given target
# O(n^2) time complexity

# Function to find triplets in an array that sum to a given target
def find_triplets_with_sum(arr, target_sum):
    temp = arr.copy()                                                                     # Create a copy of the original array to preserve indices
    arr.sort()                                                                            # Sort the array to use two-pointer technique

    for k in range(len(arr)):
        temp_target = target_sum

        temp_target -= arr[k]                                                                # Reduce the target sum by the fixed element

        start = k + 1                                                                      # Initialize start pointer
        end = len(arr) - 1                                                                 # Initialize end pointer
        check = False                                                                    # Flag to check if triplet is found
        while start < end:                                                                 # Loop until the two pointers meet or cross
            current_sum = arr[start] + arr[end]                                            # Calculate the sum of elements at the two pointers

            if current_sum == temp_target:                                                 # If the sum matches the target sum then we found a triplet
                check = True                                                                # Set check to True
                l1, l2, l3 = 0, 0, 0
                for i in range(len(temp)):                                                 # Loop through the original array to find the indices of the elements
                    if temp[i] == arr[k] and l1 == 0:                                      # Find the index of the first element
                        l1 = i                                                             # Store the index of the first element
                    elif temp[i] == arr[start] and l2 == 0:                               # Find the index of the second element
                        l2 = i                                                             # Store the index of the second element
                    elif temp[i] == arr[end] and l3 == 0:                                 # Find the index of the third element
                        l3 = i                                                             # Store the index of the third element
                show_triplets([(arr[k], arr[start], arr[end])], (l1, l2, l3), temp, target_sum) # Display the triplet found along with their indices
                break                                                                       # Exit after finding the first triplet
            elif current_sum < temp_target:                                                # If the current sum is less than the target sum, move the start pointer to the right
                start += 1                                                                  # Move the start pointer to the right
            else:                                                                          # If the current sum is greater than the target sum, move the end pointer to the left
                end -= 1                                                                    # Move the end pointer to the left
    if not check: show_triplets([], (), temp, target_sum)                                       # Display no triplet found

# Function to display the triplets found
def show_triplets(triplets, location, arr, target):
    print(f"Original array: {arr}")                                                        # Print the original array
    print(f"Target sum: {target}")                                                         # Print the target sum
    print(f"Triplets found at {location}: {triplets}")                                     # Print the triplets found along with their indices

# Main function to take input and call the find_triplets_with_sum function
def main():
    arr = input("Enter the array elements separated by space: ").split()                   # Take input from the user and split it into an array
    arr = [int(x) for x in arr]                                                            # Convert the elements from string to integer
    target_sum = int(input("Enter the target sum: "))                                      # Take the target sum as input from the user
    find_triplets_with_sum(arr, target_sum)                                                # Call the find_triplets_with_sum function

# Check if the script is being run directly
if __name__ == "__main__":
    main()                                                                                 # Call the main function to execute the program