def plus_one(digits):   
    # Check if the array length is within valid bounds (1 <= length <= 100)
    if len(digits) < 1 or len(digits) > 100:
        return "Wrong array length"
    
    # Case where the array has only one digit
    elif len(digits) == 1:
        new_digits = []
        for digit in digits:
            digit = digit + 1  # Increment the single digit by one
        digit_as_string = str(digit)  # Convert the digit to a string to handle potential carry
        for char in digit_as_string:
            char = int(char)  # Convert each character back to an integer
            new_digits.append(char)
        return new_digits
    
    else:
        target_index = len(digits) - 1  # Index of the last digit in the array
        new_digits = []

        # Validate each digit in the array and handle special cases
        for i, digit in enumerate(digits):
            if digit < 0 or digit > 9:  # Check for invalid digit values
                return "Values too big"
            
            # Case where the last digit is 9 and incrementing it will cause a carry
            elif digits[target_index] == 9:
                number_as_a_string = ""
                for digit in digits:
                    digit = str(digit)  # Convert each digit to a string for concatenation
                    number_as_a_string += digit
                number = int(number_as_a_string)  # Convert the concatenated string back to an integer
                number = number + 1  # Increment the number by one
                number = str(number)  # Convert back to string to split into digits
                for value in number:
                    value = int(value)  # Convert each character back to an integer
                    new_digits.append(value)
                return new_digits
            
            else:
                if i == target_index:
                    digit = digit + 1  # Increment the last digit if no carry is needed
                    new_digits.append(digit)
                else:
                    new_digits.append(digit)  # Append the current digit as-is

        # Return the modified list with the incremented value
        ## return new_digits  # Uncomment to use this return when needed

def main():
    result = plus_one([])  # Test the function with an empty list (modify as needed for testing)
    print(result)

if __name__ == "__main__":
    main()

