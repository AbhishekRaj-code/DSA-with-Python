# Kadane Algorithm to find the maximum sum of a contiguous subarray

def kadane_algorithm(arr):
    max_current = arr[0]                                     # Initialize max_current to the first element
    max_global = arr[0]                                      # Initialize max_global to the first element

    for i in range(1, len(arr)):                             # Iterate through the array starting from the second element
        max_current = max(arr[i], max_current + arr[i])      # Update max_current
        if max_current > max_global:                         # Update max_global if needed
            max_global = max_current

    return max_global                                         # Return the maximum sum of contiguous subarray

def main():
    arr = input("Enter the array: ").split()             # Take input from the user and split it into an array
    arr = list(map(int, arr))                                 # Convert the elements from string to integer
    max_sum = kadane_algorithm(arr)                           # Call the Kadane algorithm function
    print(f"The maximum sum of a contiguous subarray is: {max_sum}") # Print the maximum sum


if __name__ == "__main__":
    main()                                                    # Call the main function to execute the program                                     