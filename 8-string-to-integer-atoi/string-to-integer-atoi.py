class Solution:
    def myAtoi(self, s: str) -> int:

        # for removing whitespace 
        s=s.strip()
        if not s:
            return 0

        # determine the sign 

        
        sign=1
        if s[0]=='-':
            sign=-1
            s=s[1:]
        elif s[0]=='+':
            s=s[1:]
            

        # read digits until the next non-digit character
        digit=[]
        for i in s:
            if not i.isdigit():
                break
            digit.append(i)

        if not digit:
            return 0
        # convert digit into int removing any words or non digit char if exist
        number="".join(digit)
        
        
            



        res=int(number)*sign
        res=max(min(res,2**31-1),-2**31)

        return int(res)