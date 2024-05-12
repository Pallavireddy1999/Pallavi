class Solution:
    def minDifference(self, nums):
      nums.sort()  # Sort the heights in ascending order
      min_diff = float('inf')  # Initialize minimum difference as infinity
      for i in range(len(nums) - 1):
        diff = abs(nums[i] - nums[i+1])  # Calculate difference between neighboring heights
        min_diff = min(min_diff, diff)  # Update minimum difference if necessary
      return min_diff
''' putt represents the heights of friends: 10 12 13 15 10 After sorting the array in ascending order, we get: 10 10 12 13 15 Now, we find the pair of neighboring friends with the minimum absolute height difference. In this case, the minimum difference is 0 which is between the two firends with same height 10 and 10. write python code to get the minimum height difference
'''