# This is Simple Spproach using  Counter

class Solution(object):
    # Create a Counter object for the target array
    # This will count the frequency of each element in the target array
    target_counter = Counter(target)
    
    # Create a Counter object for the arr array
    # This will count the frequency of each element in the arr array
    arr_counter = Counter(arr)
    
    # Compare the two Counter objects
    # If they are equal, it means both arrays have the same elements with the same frequencies
    # Hence, it is possible to make arr equal to target by reversing subarrays
    return target_counter == arr_counter

# Approach 2 Mannual 

class Solution:
    def canBeEqual(self,target, arr):
        # Create dictionaries to count the frequency of each element in the target and arr arrays
        target_counter = {}
        arr_counter = {}

        # Count frequency of each element in the target array
        for num in target:
            if num in target_counter:
                target_counter[num] += 1
            else:
                target_counter[num] = 1

        # Count frequency of each element in the arr array
        for num in arr:
            if num in arr_counter:
                arr_counter[num] += 1
            else:
                arr_counter[num] = 1

        # Compare the two dictionaries
        # If they are equal, it means both arrays have the same elements with the same frequencies
        # Hence, it is possible to make arr equal to target by reversing subarrays
        return target_counter == arr_counter