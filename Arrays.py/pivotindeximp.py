def pivotIndex(nums:[int]):
        leftsum=0
        globalsum=sum(nums)
        for i,num in enumerate(nums):
            if globalsum-2*leftsum==num:
                return i
            leftsum+=num
        return -1
ans=pivotIndex([1,7,3,6,5,6])
print(ans)

'''when we reach to the num ,the leftsum == rightsum
so, the total-2*leftsum must be equal to curret num.


'''