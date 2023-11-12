class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        
        def search(openRem,closeRem, current):
    
            if (closeRem == 0 and openRem == 0):
                ans.append(current)
                
            if (closeRem > openRem):
                search(openRem,closeRem-1,current+")")
            
            if openRem > 0:
                search(openRem-1,closeRem,current+"(")
        

        search(n-1,n,"(")
        return ans
        