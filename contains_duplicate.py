def compare(num, nums, start_index):
    initial_assumption = False  # Initialize assumption as False, indicating no duplicate found yet
    for i, value in enumerate(nums):  # Loop through each element in the list
        if i == start_index:  # Skip the current element to avoid self-comparison
            continue
        if value == num:  # Check if any other element matches the current number
            initial_assumption = True  # Set to True if a duplicate is found
    return initial_assumption  # Return the result of the comparison

def contains_duplicate(nums):
    if len(nums) <= 1 or len(nums) >= 100000:  # Check if the list length is within the valid range
        return "Inaccurate Length"  # Return error message if length is out of bounds
    for num in nums:  # Loop through each number in the list
        if num >= 10**9:  # Check if the number is too large
            return "Value too big"  # Return error message if a number is too large
        if num <= -10**9:  # Check if the number is too small
            return "Value too small"  # Return error message if a number is too small
    for i, num in enumerate(nums):  # Iterate through the list with index and value
        are_there_duplicates = compare(num, nums, i)  # Call `compare` to check for duplicates
        if are_there_duplicates:  # If a duplicate is found, return True immediately
            return True
    return False  # Return False if no duplicates are found

def main():
    nums = [1, 2, 3, 4, 2]  # Example input list (modify as needed for testing)
    result = contains_duplicate(nums)  # Call the `duplicate` function and store the result

    # Print appropriate message based on the result
    if result == True:
        print("Duplicate found")
    elif result == False:
        print("No duplicates found")
    else:
        print(result)  # Print the error message if result is a string

if __name__ == "__main__":
    main()  # Run the `main` function when the script is executed directly



