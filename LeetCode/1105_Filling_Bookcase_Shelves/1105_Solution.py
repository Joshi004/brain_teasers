class Solution:
    def minHeightShelves(self, books, shelfWidth) -> int:
        from functools import lru_cache
        
        # Recursive function to calculate minimum height of the bookshelf
        def get_height(i, available_width, shelf_max, mem):
            # Memoization key for the current state
            key = (i, available_width)
            
            # If the result for this state is already computed, return it
            if key in mem:
                return mem[key]
            
            # Base case: If all books are placed, return the height of the current shelf
            if i == len(books):
                return shelf_max
            
            # Get the width and height of the current book
            current_width, current_height = books[i]
            
            # Case 1: Place the current book on a new shelf
            # Height required is the height of the current shelf plus the result of placing the next books
            next_shelf_height = shelf_max + get_height(i + 1, shelfWidth - current_width, current_height, mem)
            
            # Case 2: Place the current book on the same shelf if it fits
            same_shelf_height = float('inf')  # Initialize to a large value
            if current_width <= available_width:
                # Update the maximum height of the current shelf
                new_shelf_max = max(shelf_max, current_height)
                # Compute the height with the current book on the same shelf
                same_shelf_height = get_height(i + 1, available_width - current_width, new_shelf_max, mem)
            
            # Determine the minimum height by considering both cases
            result = min(same_shelf_height, next_shelf_height)
            
            # Store the result in the memoization dictionary
            mem[key] = result
            
            return result
        
        # Start recursion with the first book, full shelf width, and initial shelf height of 0
        return get_height(0, shelfWidth, 0, {})