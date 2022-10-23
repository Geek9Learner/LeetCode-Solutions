class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        else:
            sdict={}
            for item in s:
                if item in sdict:
                    sdict[item] += 1
                else:
                    sdict[item] = 1
            tdict={}
            for item in t:
                if item in tdict:
                    tdict[item] += 1
                else:
                    tdict[item] = 1
            if(sdict==tdict):
                return True
            
        return False