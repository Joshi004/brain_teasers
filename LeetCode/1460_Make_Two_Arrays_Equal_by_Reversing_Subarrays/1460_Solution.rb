def can_be_equal(target, arr)
    # Create a hash to count the frequency of each element in the target array
    target_counter = Hash.new(0)
    target.each do |num|
      target_counter[num] += 1
    end
  
    # Create a hash to count the frequency of each element in the arr array
    arr_counter = Hash.new(0)
    arr.each do |num|
      arr_counter[num] += 1
    end
  
    # Compare the two hash objects
    # If they are equal, it means both arrays have the same elements with the same frequencies
    # Hence, it is possible to make arr equal to target by reversing subarrays
    target_counter == arr_counter
  end