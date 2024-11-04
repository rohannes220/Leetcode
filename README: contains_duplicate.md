# README: Contains Duplicate

## Overview

This repository contains a Python solution to the **"Contains Duplicate"** problem from [LeetCode's Top Interview Questions - Easy](https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/578/).

### Problem Description

**Objective**: Given an integer array `nums`, determine if any value appears at least twice in the array. Return `True` if any value appears more than once, and `False` if every element is distinct.

### Example:
**Input**:
```python
nums = [1, 2, 3, 1]
```
**Output**:
```
True
```

**Input**:
```python
nums = [1, 2, 3, 4]
```
**Output**:
```
False
```

### Constraints:
- 1 <= `len(nums)` <= 10^5
- -10^9 <= `nums[i]` <= 10^9

### Implementation:
```python
def contains_duplicate(nums):
    seen = set()  # Initialize an empty set to store unique elements
    for num in nums:  # Iterate through each number in the list
        if num in seen:  # Check if the number is already in the set
            return True  # Return True if a duplicate is found
        seen.add(num)  # Add the number to the set if not already present
    return False  # Return False if no duplicates are found
```

## How to Run

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/contains-duplicate.git
   ```

2. **Run the script**:
   ```bash
   python contains_duplicate.py
   ```

3. **Modify the input** in the `main()` function to test different cases.

## Example Usage

```python
nums = [1, 2, 3, 1]  # Replace with any list for testing
result = contains_duplicate(nums)
print("Duplicate found" if result else "No duplicates found")
```
---

Feel free to explore, use, or adapt this solution for learning and enhancing your coding skills!
