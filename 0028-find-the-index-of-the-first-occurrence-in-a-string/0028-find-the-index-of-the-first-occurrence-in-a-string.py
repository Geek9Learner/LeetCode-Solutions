class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        stringList=[]
        for i in range(len(haystack)):
            temp=haystack[i:len(needle)+i]
            if(len(temp)==len(needle)):
                stringList.append(temp)
        return stringList.index(needle) if needle in stringList else -1