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
