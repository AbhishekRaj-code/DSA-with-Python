# Moore's Voting Algorithm to find the majority element in an array

# Function to find majority element by sorting
def majority(arr): 
    arr.sort()                                                                                   # Sort the array as the majority element will be in the middle after sorting

    majority_element = arr[0]                                                                   # Initialize majority element
    count = 1                                                                                   # Initialize count
    max_count = 0                                                                               # Initialize max_count

    for i in range(len(arr) - 1):                                                               # Loop through the array
        if arr[i] == arr[i + 1]:                                                                # If the current element is equal to the next element
            count += 1                                                                          # Increment count
            if max_count < count:                                                               # If max_count is less than count
                majority_element = arr[i]                                                       # Update majority element
                max_count = count                                                               # Update max_count
                count = 1                                                                       # Reset count
            else:                                                                               # If current element is not equal to the next element
                count += 1                                                                      # Reset count
        
        if max_count < count:                                                                   # Final check for the last element
            majority_element = arr[-1]                                                          # Update majority element

    return majority_element                                                                     # Return the majority element

# Function to implement Moore's Voting Algorithm
def moore_algoritm(arr):
    majority_element = -1                                                                      # Initialize majority element
    votes = 0                                                                                  # Initialize votes

    for i in arr:                                                                              # Loop through the array
        if votes == 0:                                                                         # If votes is 0, set the current element as majority element
            majority_element = i                                                               # Set the current element as majority element
            votes = 1                                                                          # Set votes to 1
        else:                                                                                  # If votes is not 0
            if i == majority_element:                                                          # If the current element is equal to majority element
                votes += 1                                                                     # Increment votes
            else:                                                                              # If the current element is not equal to majority element
                votes -= 1                                                                     # Decrement votes

    votes = 0                                                                                  # Reset votes for verification

    for i in arr:                                                                              # Loop through the array to verify majority element
        if i == majority_element:                                                              # If the current element is equal to majority element
            votes += 1                                                                         # Increment votes

    if votes > len(arr) // 2:                                                                  # If votes is greater than half the length of the array
        return majority_element                                                                # Return the majority element
    else:                                                                                      # If votes is not greater than half the length of the array
        return -1                                                                              # Return -1 indicating no majority element
    
# Main function to take input and call the moore_algorithm function
def main():
    arr = input("Enter the array elements separated by space: ").split()                       # Take input from the user and split it into an array
    arr = [int(x) for x in arr]                                                                # Convert the elements from string to integer
    print(f"The majority element is: {moore_algoritm(arr)}")                                   # Call the moore_algorithm function and print the majority element

# Check if the script is being run directly
if __name__ == "__main__":
    main()                                                                                      # Call the main function