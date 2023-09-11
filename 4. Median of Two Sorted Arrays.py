class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mergedList = []
        n1 = 0
        n2 = 0

        num1Len = len(nums1)
        num2Len = len(nums2)
        while (n1 < num1Len and n2 < num2Len):

            if (nums1[n1] <= nums2[n2]):
                mergedList.append(nums1[n1])
                n1+=1
            else:
                mergedList.append(nums2[n2])
                n2+=1

        if (n1 == num1Len):
            mergedList.extend(nums2[n2::])
        else:
            mergedList.extend(nums1[n1::])

        #now do binary search

        totalLen = num1Len+num2Len
        mid = (totalLen-1)//2
        
        if totalLen %2 == 0:
            return (mergedList[mid] + mergedList[mid+1])/2
        else:
            return (mergedList[mid])        