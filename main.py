def lengthOfLongestSubstring(s: str) -> int:
    sub={}
    cur_sub_start=0
    cur_len=0
    longest=0
    for i, char in enumerate(s):
        if char in sub and sub[char]>=cur_sub_start:
            print(sub)
            print(sub[char])
            cur_sub_start = sub[char]+1
            cur_len=i-sub[char]
            sub[char]=i
            print(sub)
        else:
            sub[char]=i
            cur_len+=1
            if cur_len>longest:
                longest=cur_len
    return longest

ans = lengthOfLongestSubstring("abcabcbb")
print(ans)
