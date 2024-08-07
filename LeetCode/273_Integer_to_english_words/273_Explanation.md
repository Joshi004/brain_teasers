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

By following this structured approach, the problem is broken down into smaller, manageable pieces, making the solution both intuitive and efficient.
