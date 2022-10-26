class Solution:
    def isValid(self, s: str) -> bool:
        validBracket=[]
        if(len(s)==1):
            return False
        for i in range(len(s)):
            if(s[i]=='(' or s[i]=='{' or s[i]=='['):
                validBracket.append(s[i])
                continue
            elif(len(validBracket)==0):
                return False
            elif(s[i]==')'):
                ch=validBracket[-1]
                validBracket.pop()
                if(ch=='{' or ch=='['):
                    return False
            elif(s[i]=='}'):
                ch=validBracket[-1]
                validBracket.pop()
                if(ch=='[' or ch=='('):
                    return False
            elif(s[i]==']'):
                ch=validBracket[-1]
                validBracket.pop()
                if(ch=='{' or ch=='('):
                    return False
        
        if(len(validBracket)==0):
            return True
        #print(validBracket)
        return False