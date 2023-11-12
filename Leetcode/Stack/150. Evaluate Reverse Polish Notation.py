class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        dicti = {
            "+":lambda a,b: a+b,
            "*":lambda a,b: a*b,
            "/":lambda a,b: int(a/b),
            "-":lambda a,b: a-b,
        }
        for token in tokens:
            if token in "+*/-":
                operation = dicti[token]
                val1 = int(stack.pop)
                val2 = int(stack.pop)
                stack.append(operation(val2,val1))
            else:
                stack.append(token)
        
        return int(stack[0])
                
            
        