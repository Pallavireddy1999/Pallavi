
#O(n^2) TC 
'''
def twoSum(nums, target):
    i=0
    n=len(nums)
    for i in range(n-1): 
        for j in range(i+1,n):
            current_sum=nums[i]+nums[j]
            if current_sum == target:
                return([i,j])
    return -1

ans=twoSum([2,5,5,11],10)
print(ans)
'''
#O(n) TC ,not going through all elements again 
# saving the seen elements {1:0,2:1,3:2} when target - num becomes 2 which is in seen 
# index of target-num would be seen[target-num] =seen[2] =1,  seen[num]=seen[4]=3


def tSum(nums,target):
        seen={}
        for i,num in enumerate(nums):
            if target - num in seen:
                return(seen[target-num],i)
            elif num not in seen:
                seen[num]=i
ans=tSum([1,2,3,4],6)
print(ans)

