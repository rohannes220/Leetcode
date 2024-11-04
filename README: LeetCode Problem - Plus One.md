# README: Plus One Solution

This repository contains my Python solution to the **"Plus One"** problem from [LeetCode's Top Interview Questions - Easy](https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/559/).

## Problem Overview

Problem: You are given a non-empty array of decimal digits representing a non-negative integer. Increment the integer by one and return the resulting array of digits.

### Example:
Input:
```
digits = [1, 2, 3]
```
Output:
```
[1, 2, 4]
```
Explanation: The array represents the integer 123. Incrementing by one results in 124.

### Edge Cases:
- The input array can have digits that result in carry-over, such as `[9, 9, 9]`.
- The input will not have any leading zeroes, except for the single digit `0`.

### Constraints:
- 1 <= `digits.length` <= 100
- 0 <= `digits[i]` <= 9

## Solution Approach

### Method:
- Iterate from right to left** through the array to handle the increment.
- Manage carry-over by checking if the current digit is 9. If it is, set it to 0 and propagate the carry to the next digit on the left.
- If all digits are 9 (e.g., `[9, 9, 9]`), prepend a `1` to the result to handle the carry.

### Complexity:
- Time Complexity: `O(n)`, where `n` is the length of the array, as each digit may be visited once.
- Space Complexity: `O(1)` if the input array is modified in place; otherwise, `O(n)` for a new array.

## How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/plus-one-solution.git
   ```

2. Run the script:
   ```bash
   python plus_one.py
   ```

3. Modify the input in the `main()` function for testing different cases.

## Code Overview

The function `plus_one(digits)` accepts a list of integers and returns a list representing the incremented number.

```python
def plus_one(digits):
    # Logic to increment the array representation of the number
```

## Example Test Case

### Input:
```python
digits = [9, 9, 9]
```
### Output:
```python
[1, 0, 0, 0]
```

This solution handles edge cases involving carries and ensures that the result is always correct.

---

Feel free to explore and use this solution to learn or adapt it to similar array manipulation problems.
