
'''ans[-1] gives the last element 
we are XoR ing the encoded with first to get the decoded

'''


def decode(encoded:[int], first: int):
        ans= [first]
        for x in encoded:
            ans.append(ans[-1]^x)
        return ans

ans =decode([1,2,3],1)
print(ans)


