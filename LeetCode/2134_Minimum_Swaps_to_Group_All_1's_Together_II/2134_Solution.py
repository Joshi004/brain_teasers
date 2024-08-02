class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        # Initialize swap_count to track the total swaps needed
        swap_count = 0

        # Determine the window size (number of 1's in the array)
        window_size = nums.count(1)

        # Duplicate the array to handle circular property
        nums = nums + nums[0:window_size]

        # Get the total length of the extended array
        n = len(nums)

        # Initialize zero_count with the count of 0's in the initial window
        zero_count = nums[0:window_size].count(0)

        # Initialize min_zero_count with the initial zero_count
        min_zero_count = zero_count

        # Iterate through the circular array
        for i in range(1, n - window_size + 1):
            # Update zero_count based on the elements entering and leaving the window
            if nums[i - 1] == 0:
                zero_count -= 1
            if nums[i + window_size - 1] == 0:
                zero_count += 1

            # Update min_zero_count with the minimum zero_count encountered
            min_zero_count = min(zero_count, min_zero_count)

        # Return the minimum zero_count as the result
        return min_zero_count
