class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        n = len(arr)
        count = 0
        lp, rp = 0, 1

        while (count != k):
            lp = lp%n
            rp = rp%n
            # perform mod so we don't get OOB

            # then the element at the LP is greater than all the other element
            # so other checks are now redundant so we can break
            if count == n:
                break

            # then increment the rp and keep the lp pos
            if (arr[lp] >= arr[rp]):
                count+=1
                rp+=1
            else:
                # the element at the rp is greater, so set the lp to this element and increment
                count=1
                lp = rp
                rp+=1
        
        return arr[lp]
        