class Solution(object):
    data={'M':'1000','D':'500','C':'100','L':'50','X':'10','V':'5','I':'1'}
    def romanToInt(self, s):
        
        num=0
        a=0
        while a<=len(s)-1:
            if a==len(s)-1:
                num+=int(data[s[a]])
                a+=1
            elif int(data[s[a]])<int(data[s[a+1]]):
                num+=int(data[s[a+1]])-int(data[s[a]])
                a+=2
            else:
                num+=int(data[s[a]])
                a+=1
        return num
            
s="MCMXCIV"
print(Solution.romanToInt(s,s))

    
       
        


        
