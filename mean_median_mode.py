#This program calculates the mean, median, and mode of a given set of numbers.
# It takes input from the user and displays the results in a formatted manner.
#The program uses functions to perform the calculations and print the results.

#Function to calculate mean
def mean(elements, number_of_elements):               #elements: list of numbers, number_of_elements: number of elements in the list
    
    sum = 0                                           #initialize sum to 0 so that we can add elements to it
    for i in elements:                                #iterate through each element in the list so that we can add it to sum
        sum = sum + i                                 #add the current element to sum to get the total sum of all elements
    mean_value = sum / number_of_elements             #calculate mean by dividing sum by number of elements
    return mean_value                                 #return the mean value

#Function to calculate median
def median(elements, number_of_elements):            #elements: list of numbers, number_of_elements: number of elements in the list
    
    elements.sort()                                  #sort the elements in ascending order to find the median because median is the middle value in a sorted list
    if number_of_elements % 2 == 0:                  #check if the number of elements is even as the median calculation differs for even and odd number of elements
        mid1 = elements[number_of_elements // 2]     #get the two middle elements
        mid2 = elements[(number_of_elements // 2) - 1] #get the two middle elements
        median_value = (mid1 + mid2) / 2              #calculate median by taking the average of the two middle elements as the median for even number of elements is the average of the two middle values
    else:                                             #if the number of elements is odd
        median_value = elements[number_of_elements // 2] #get the middle element as the median for odd number of elements is the middle value
    return median_value                               #return the median value

#Function to calculate mode
def mode(elements, number_of_elements):               #elements: list of numbers, number_of_elements: number of elements in the list
    
    elements.sort()                                   #sort the elements in ascending order to find the mode because mode is the most frequently occurring value in a sorted list
    max_count = 0                                     #initialize max_count to 0 to keep track of the highest frequency of any element
    mode_value = elements[0]                          #initialize mode_value to the first element in the list because we will compare other elements to it
    current_count = 1                                 #initialize current_count to 1 to count the frequency of the current element because we start counting from the first element
    for i in range( number_of_elements - 1):          #iterate through each element in the list except the last one to compare it with the next element
        if elements[i] == elements[i + 1]:            #check if the current element is equal to the next element as we want to count the frequency of each element
            current_count += 1                        #increment current_count by 1 if the current element is equal to the next element
        else:                                         #if the current element is not equal to the next element
            if current_count > max_count:             #check if the current_count is greater than max_count to update the mode_value if necessary
                max_count = current_count             #update max_count to current_count if current_count is greater than max_count
                mode_value = elements[i]              #update mode_value to the current element if current_count is greater than max_count
            current_count = 1                         #reset current_count to 1 for the next element because we are moving to a new element
    if current_count > max_count:                     #check for the last element in the list to update the mode_value if necessary
        mode_value = elements[-1]                     #update mode_value to the last element if current_count is greater than max_count
    if mode_value == elements[0] and max_count == 1: #check if all elements are unique
        mode_value = "No mode"                       #set mode_value to "No mode" if all elements are unique
    return mode_value                                #return the mode value

#Function to print statistics
def print_statistics(mean_value, median_value, mode_value, elements): #mean_value: calculated mean, median_value: calculated median, mode_value: calculated mode, elements: list of numbers
    print("Statistics:")
    print("----------------")
    print("The given data set is analyzed below:", elements)
    print("----------------")
    print(f"Mean: {mean_value}")
    print(f"Median: {median_value}")
    print(f"Mode: {mode_value}")

#Main function to take input and call other functions
def main():                                                              #main function to execute the program
    number_of_elements = int(input("Enter the number of elements: "))    #take input for number of elements from the user
    elements = input("Enter the elements separated by space: ").split()  #take input for elements from the user and split them into a list
    elements = list(map(int, elements))                                  #convert the elements from string to integer

     #call the functions to calculate mean, median, and mode
    mean_value = mean(elements, number_of_elements)                   #calling mean function to calculate mean and store the result in mean_value
    median_value = median(elements, number_of_elements)               #calling median function to calculate median and store the result in median_value
    mode_value = mode(elements, number_of_elements)                   #calling mode function to calculate mode and store the result in mode_value
    print_statistics(mean_value, median_value, mode_value, elements) #calling print_statistics function to print the results

if __name__ == "__main__":                                            #check if the script is being run directly
    main()                                                            #call the main function to execute the program