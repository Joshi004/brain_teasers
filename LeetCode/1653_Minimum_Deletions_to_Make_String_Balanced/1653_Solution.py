from collections import deque

class Solution:
    def minimumDeletions(self, s: str) -> int:
        # Initialize a deque to act as a stack for managing characters
        queue = deque()
        # Initialize a counter to keep track of the minimum deletions needed
        counter = 0
        
        # Iterate through each character in the string s
        for char in s:
            # If the current character is 'a'
            if char == "a":
                # Check if the stack is not empty and the top element is 'b'
                if len(queue) and queue[-1] == "b":
                    # If the condition is met, it means we have an imbalance ('ba')
                    # Remove the 'b' from the stack (pop operation)
                    popped = queue.pop()
                    # Increment the counter since we removed a 'b' to balance the string
                    counter += 1
                else:
                    # If the condition is not met, simply add 'a' to the stack
                    queue.append(char)
            else:   
                # If the current character is 'b', add it to the stack
                queue.append(char)
        
        # Return the total number of deletions needed to make the string balanced
        return counter



