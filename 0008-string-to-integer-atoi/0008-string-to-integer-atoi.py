class Solution:
    def myAtoi(self, s: str) -> int:
        if s=="":
            return 0
        num=0;s=s.strip();symbol=0
        if s=="":
            return 0
        if (s[0]=='+' or s[0]=='-') and len(s)==1:
            return 0
        if s[0]=='-' and s[1]=='+':
            return 0
        if s[0]=='+' and s[1]=='-':
            return 0
        if s[0]=='-':
            symbol=-1
            s=s[1:]
        if s[0]=='+':
            symbol=1
            s=s[1:]
        #print(s)
        for i in range(len(s)):
            if not s[i].isdigit():
                break
            if ord(s[i])>=48 and ord(s[i])<=57:
                num=num*10+int(s[i])
        
        if symbol==-1:
            num=num*-1
        if num>=0 and num<=2147483647:
            return num
        elif num>2147483647:
            return 2147483647
        elif num<0 and num>=-2147483648:
            return num
        else:
            return -2147483648
      
        