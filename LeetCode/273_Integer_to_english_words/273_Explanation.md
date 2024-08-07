# Solution Explanation for "Integer to English Words"

## Intuition and Thought Process

To convert a non-negative integer to its English words representation, we can break the problem into manageable parts:

1. **Handling Small Numbers:** 
   - Numbers less than 20 have unique names (e.g., One, Eleven, Nineteen) that do not follow a consistent pattern.
   - Numbers from 20 to 99 follow a tens pattern (e.g., Twenty-One, Thirty-Five).

2. **Handling Larger Numbers:**
   - Numbers from 100 to 999 can be described using hundreds (e.g., One Hundred Twenty-Three).
   - Numbers larger than 999 can be broken into thousands, millions, and billions.

## Approach

1. **Special Arrays:**
   - Create arrays to store words for numbers below 20, tens, and large units (thousands, millions, billions).

2. **Helper Function:**
   - Implement a recursive helper function that converts numbers less than 1000 to words.
   - This function handles numbers in three cases:
     - Numbers less than 20: directly use the `below_20` array.
     - Numbers less than 100: use the `tens` array and recurse for the remainder.
     - Numbers less than 1000: handle hundreds and recurse for the remainder.

3. **Main Conversion Function:**
   - Iterate over the input number in chunks of 1000.
   - For each chunk, if it’s non-zero, convert it to words using the helper function and append the appropriate unit (thousand, million, billion).

4. **Edge Case:**
   - Directly return "Zero" if the input number is zero.

## Detailed Explanation of the Code

```python
class Solution:
    def numberToWords(self, num: int) -> str:
        # If the input number is zero, directly return "Zero"
        if num == 0:
            return "Zero"
        
        # Define arrays to store the words for numbers below 20, tens, and large units
        below_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
                    "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        thousands = ["", "Thousand", "Million", "Billion"]

        # Helper function to convert numbers less than 1000 to words
        def helper(n):
            if n == 0:
                return ""  # Base case: return an empty string for zero
            elif n < 20:
                return below_20[n] + " "  # Directly use below_20 array for numbers less than 20
            elif n < 100:
                return tens[n // 10] + " " + helper(n % 10)  # For numbers less than 100, use tens array and recurse for the remainder
            else:
                return below_20[n // 100] + " Hundred " + helper(n % 100)  # For numbers less than 1000, handle hundreds and recurse for the remainder

        res = ""  # Initialize the result string
        # Iterate over each thousand unit (thousand, million, billion)
        for i, unit in enumerate(thousands):
            if num % 1000 != 0:  # Only process non-zero chunks
                res = helper(num % 1000) + unit + " " + res  # Convert the chunk to words and add the appropriate unit
            num //= 1000  # Move to the next chunk

        return res.strip()  # Remove any trailing spaces and return the final result
```

## Time and Space Complexity Analysis

### Time Complexity
- The time complexity of this solution is \(O(\log_{1000}(n))\) because we are processing the number in chunks of 1000.
  - Each recursive call processes a number less than 1000 in constant time \(O(1)\).
  - The number of chunks processed is \(\log_{1000}(n)\), where \(n\) is the input number.

### Space Complexity
- The space complexity is \(O(\log_{1000}(n))\) due to the recursion stack used in the helper function.
  - In the worst case, the depth of the recursion stack is \(\log_{1000}(n)\) because each call processes one chunk of the number.

## Dry Runs on Sample Test Cases

### Test Case 1
**Input:** `num = 123`

**Flow:**
- The number 123 is processed as:
  - `123 % 1000 = 123` 
  - Convert 123 to words: `One Hundred Twenty Three`
  - Final result: `"One Hundred Twenty Three"`

### Test Case 2
**Input:** `num = 12345`

**Flow:**
- The number 12345 is processed in chunks:
  - `12345 % 1000 = 345`
  - Convert 345 to words: `Three Hundred Forty Five`
  - `12345 // 1000 = 12`
  - Convert 12 to words: `Twelve`
  - Combine with the thousand unit: `"Twelve Thousand Three Hundred Forty Five"`

### Test Case 3
**Input:** `num = 1234567`

**Flow:**
- The number 1234567 is processed in chunks:
  - `1234567 % 1000 = 567`
  - Convert 567 to words: `Five Hundred Sixty Seven`
  - `1234567 // 1000 = 1234`
  - `1234 % 1000 = 234`
  - Convert 234 to words: `Two Hundred Thirty Four`
  - `1234 // 1000 = 1`
  - Convert 1 to words: `One`
  - Combine with the thousand and million units: `"One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"`

