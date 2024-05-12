
#we are checking for the longest palindrome so we go through length in reverse
#for a 5 letter string we have to check only once ,as we go on reducing length, we have to check more substrings
# we use start index i rnge of 0 to len(s)+1-length as the length will be reducing and we will check for more substrings
#s[start_index:(start_index+length)] indicates the total string if index=0 and length is max.
# we can optimize this more by taking one letter as a point of reference or similarity and checking it's left and right
'''
def longestPalindrome(s: str) -> str:
        def check_palin(s):
              return(s==s[::-1])
        for length in range(len(s),0,-1):
            for start_index in range(0,len(s)+1-length):
                print(s[start_index:(start_index+length)])
                if check_palin(s[start_index:(start_index+length)]):
                  return(s[start_index:(start_index+length)])
ans = longestPalindrome("babad")
print(ans)
'''

def longpalin(s:str) -> str:
    def check_palin(s):
        return(s==s[::-1])
    
    biggest=s[0]
    step=len(biggest)//2
     
    #for single letter centers
    for center in range(1,len(s)-1):
        bounds =[center-(1+step),center+(1+step)]
        while(bounds[0]>-1 and bounds[1]<len(s)):
            if check_palin(s[bounds[0]:bounds[1]+1]):
                biggest=s[bounds[0]:bounds[1]+1]
                step=len(biggest)//2
                bounds[0]-=1
                bounds[1]+=1
            else:
                break
    #for double letter centers
    for center in range(step,len(s)-step-1):
        bounds= [center-(step),center+(1+step)]
        while(bounds[0]>-1 and bounds[1]<len(s)):
            if check_palin(s[bounds[0]:bounds[1]+1]):
                biggest=s[bounds[0]:bounds[1]+1]
                step=len(biggest)//2
                bounds[0]-=1
                bounds[1]+=1
            else:
                break
    return biggest



            
        
    
        
ans=longpalin("aghbb")
print(ans)
