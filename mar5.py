# #Write a program to find the longest increasing subsequence in a list.
# lis=[1, 4, 3, 4, 5, 2, 7]
# cur_count, max_count = 0, 0
# n = len(lis)
# l=0
# r=0
# prev = -1

# while r<n:
#     if lis[r]>prev:
#         cur_count += 1
#         prev = lis[r]
#     else:
#         l_i, r_i = l, r-1
#         max_count = max(max_count, cur_count)
#         cur_count = 0
#         l=r
#         prev=-1
#         r-=1
# print(lis[l:r+1])

# Given an array of integers, find if there exist three numbers that sum up to zero.
nums = [1,2,1,-3,4,0]
k=3
sum = sum(nums[:k])
if sum == 0:
    print('True')
    exit(0)
for i in range(len(nums)-k):
    sum = sum-nums[i]+nums[i+k]
    if sum == 0:
        print('True')
        exit(0)
print('False')

    