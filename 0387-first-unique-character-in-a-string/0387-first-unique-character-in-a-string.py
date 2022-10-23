class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_dict={}
        for i in range(len(s)):
            if(s[i] in char_dict.keys()):
                char_dict[s[i]] +=1
            else:
                char_dict[s[i]]=1
                
        for key,value in char_dict.items():
            if(value==1):
                return s.index(key)
        return -1