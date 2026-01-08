# Kadane Algorithm for 2D Arrays

import sys                                                     # Import sys module for system-specific parameters and functions

# Function to implement Kadane's Algorithm
def kadane(matrix, l, b):
    ans = -sys.maxsize - 1                                     # Initialize ans to the smallest possible integer value
    for i in range(b):
        temp =[]
        for j in range(l):
            temp.append(matrix[j][i])
        ans = max(ans, kadane_2d(temp))                 # Call the Kadane 2D algorithm function and update ans with the maximum sum of contiguous subarray

        for j in range(i + 1, b):
            for k in range(l):
                temp[k] += matrix[k][j]
            ans = max(ans, kadane_2d(temp))             # Call the Kadane 2D algorithm function and update ans with the maximum sum of contiguous subarray

    
    show(ans, matrix)                                          # Call the function to display the result

# Function to display the result
def show(ans, matrix):
    print("The given matrix is:")                              # Print the given matrix
    for row in matrix:                                         # Iterate through each row
        print(row)                                            # Print the current row
    print(f"The maximum sum of a contiguous subarray in the given 2D array is: {ans}") # Print the maximum sum of contiguous subarray




def kadane_2d(given_num):

    start = 0                                              # Initialize start pointer
    end = 0                                                # Initialize end pointer
    curr_sum = 0                                           # Initialize current sum
    max_sum = 0                                            # Initialize maximum sum
    n = len(given_num)                                        # Get the number of elements in the matrix

    while end < n:                                         # Iterate through the matrix using end pointer 
        while curr_sum < 0:                                # If current sum is negative, move the start pointer because negative sum will decrease the overall sum
            curr_sum -= given_num[start]                      # Subtract the element at start pointer from current sum as we are moving the start pointer forward
            start += 1                                     # Move the start pointer forward to the next element

        curr_sum += given_num[end]                            # Add the element at end pointer to current sum because we are considering this element in our subarray
        end += 1                                           # Move the end pointer forward to the next element

        max_sum = max(max_sum, curr_sum)                   # Update maximum sum if current sum is greater than maximum sum
    return max_sum                                         # Return the maximum sum of contiguous subarray

# Main function to take input and call Kadane's 2D algorithm
def main():
    l = int(input("Enter the number of rows: "))               # Take input for number of rows from the user
    b = int(input("Enter the number of columns: "))            # Take input for number of columns from the user
    matrix = []                                                # Initialize an empty matrix to store the elements
    for i in range(l):                                           # Iterate through each row
        row = list(map(int, input("Enter the elements of row {} separated by space: ".format(i + 1)).split())) # Take input for each row and split it into a list
        matrix.append(row)

    # Slicing the matrix into l rows and b columns
    for i in range(l):
        matrix[i] = matrix[i][:b]

    kadane(matrix, l, b)                                      # Call the Kadane 2D algorithm function


# Check if the script is being run directly then call the main function
if __name__ == "__main__":                                      # Check if the script is being run directly
    main()                                                    # Call the main function to execute the program