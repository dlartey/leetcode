
#Q1.2
def isPermutation(stringA, stringB):
    charA = [0]*26
    charB = [0]*26
    for letter in stringA:
        charA[ord(letter)-ord("a")]+=1

    for letter in stringB:
        charB[ord(letter)-ord("a")]+=1
    
    return charA==charB

#Q1.3
def replaceSpaces(word):
    newWord = ""
    
    for i,letter in enumerate(word):
        if (letter == " "):
            newWord+="%20"
        else:
            newWord+=letter
    return newWord

# Q1.4
def palindromePermutation(word):
    dicti = {}
    if (len(word) < 2):
        return True
    
    word=word.lower()
    
    for letter in word:
        if (letter not in dicti):
            dicti[letter] = 1
        else:
            dicti[letter]+=1
            
    oddCounter = 0
    for key, value in dicti.items():
        if value % 2 == 1:
            oddCounter+=1
    
    return True if oddCounter < 2 else False
        
#print(palindromePermutation("RandomWords"))

def threeSum(nums):
        ans = []
        nums.sort()
        
        for lp in range(len(nums)):
            # calculate the missing number to find
            rp = len(nums)-1
            mid = lp+1
            while (lp < rp and mid < rp):
                missing = 0 - (nums[lp]+nums[rp])
                if (nums[mid] == missing):
                    ans.append([nums[lp],nums[mid],nums[rp]])
                    break
                if (nums[mid] > missing):
                    rp-=1
                    # calculate
                if (nums[mid] < missing):
                    mid+=1
        return ans
    
print(threeSum([-1,0,1,2,-1,-4]))