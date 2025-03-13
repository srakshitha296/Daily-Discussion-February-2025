# Given an array and as integer k, find the maximum sum of the subarray of size k.
 
# Compute the maximum sum and return the value and the subarray.
 
 
# Input : nums = [2,1,5,1,3,2], k = 3
# Output : (9, [5, 1, 3])
 
 
# Input : nums = [2,1,5,1,3,2], k = 4
 
# Output : (11, [5, 1, 3, 2])
def find_max(nums, k):
    n = len(nums)
    cur = sum(nums[0:k])
    max_sum = cur
    print(max_sum)
    for i in range(0, n-k):
        cur = cur-nums[i]+nums[i+k]
        max_sum = max(cur, max_sum) 
    result = [max_sum, nums[i:i+k]]      
    return result
nums = [2,1,5,1,3,2]
k = 3
print(find_max(nums, k))