def longestCommonPrefix(strs:[str]) -> str:
    if len(strs)==0:
        return("")
    if len(strs)==1:
        return(strs[0])
    pref=strs[0]
    plen=len(pref)
    for s in strs[1:]:
        while(pref!= s[0:plen]):
            pref=pref[0:(plen-1)]
            plen-=1
            if plen==0:
                return("")
    return(pref)

ans=longestCommonPrefix(["flower","flow","flight"])
print(ans)

'''we take the first word of string and go through rem strings to compare 
we reduce len if the prefix is not matching and recursively check for all strings

'''


        