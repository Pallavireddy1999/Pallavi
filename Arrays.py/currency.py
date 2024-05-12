
# RBI wants to introduce currency of new denominations,so for this, the Governor conducts a poll about the among N banks. Governor imposed a restriction on the denomination of the currency that is the denomination can be in the range of ==[1,N]==.Votes of all the banks have been stored in the votes array and the RBI will release currency of only those denominations which have got more than 1 vote. So you have been provided with the votes array and you need to return the array which will contain the denominations of the currency which is going to be released by the RBI sorted in increasing order. If no denominations got more than 1 vote then simply return an empty array.
'''
Note: Can you wirte an algorithm that runs in O(N) Time complexity and O(1) space complexity if we exclude the space used by the answer array?

Example 1
Input
votes = [4,3,2,1,2,1]
Output
[1,2]
def findCurrency(votes):
    released_denominations = []
    for i in range(len(votes)):
        if votes[abs(votes[i]) - 1] > 0:
            votes[abs(votes[i]) - 1] *= -1
            print(votes)
        else:
            released_denominations.append(abs(votes[i]))
    return sorted(released_denominations)
          
        


ans=findCurrency([4,3,2,1,2,1])
print(ans)

'''
def find_denominations(votes):
    n = len(votes)
    released_denominations = []
    for i in range(n):
        idx = abs(votes[i])-1
        if votes[idx] > 0:
            votes[idx] *= -1
            print(votes[idx])
    for i in range(n):
        if votes[i] > -1:
            released_denominations.append(votes[i])
    return sorted(released_denominations)

# Test the function
ans=find_denominations([1,4,4,2,6,5])
print(ans)