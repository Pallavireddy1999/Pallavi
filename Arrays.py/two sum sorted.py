def twoSum(nums, target):
        i=0
        j=len(nums)-1
        nums_sorted=sorted(nums)
        while i<j:
            current_sum=nums_sorted[i]+nums_sorted[j]
            if current_sum== target:
                x=nums_sorted[i]
                y=nums_sorted[j]
                return ([nums.index(x),nums.index(y)])
            elif current_sum < target:
                i+=1
            else:
                j-=1
        return -1

ans=twoSum([3,2,4],6)
print(ans)

        