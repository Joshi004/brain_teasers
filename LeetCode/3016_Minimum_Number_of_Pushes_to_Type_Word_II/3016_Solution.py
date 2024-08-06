from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        # Count the frequency of each letter in the word
        frequency = Counter(word)
        
        # Sort the letters by their frequency in descending order
        sorted_letters = sorted(frequency.items(), key=lambda x: -x[1])
        
        # Initialize the total number of key presses needed
        presses = 0
        
        # Iterate through the sorted letters and their frequencies
        for index, (letter, count) in enumerate(sorted_letters):
            # Determine which press it is (1st, 2nd, or 3rd press on the key)
            # There are 8 keys (2-9), so we divide by 8 to group the letters
            press_count = (index // 8) + 1
            
            # Multiply the frequency of the letter by the number of presses required
            # and add it to the total presses
            presses += press_count * count
        
        # Return the total number of key presses needed
        return presses
