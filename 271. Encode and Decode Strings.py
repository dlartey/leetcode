class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        #append&# to each string
        s = ""
        for x in range(len(strs)):
            if (x < len(strs)-1):
                s=s+strs[x]+"&#15"
            else:
                s+=strs[x]
        return s
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        temp = s.split("&#15")
        return temp
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))