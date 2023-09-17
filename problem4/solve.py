class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        newArr = []
        p1 =0
        p2 =0
        while p1 < len(nums1) and p2 < len(nums2):
            if(nums1[p1] < nums2[p2]):
                newArr.append(nums1[p1])
                p1+=1
            else:
                newArr.append(nums2[p2])
                p2+=1
        while p1 < len(nums1):
            newArr.append(nums1[p1])
            p1 += 1
        while p2 < len(nums2):
            newArr.append(nums2[p2])
            p2+= 1
        if len(newArr) % 2 == 0:
            index = len(newArr) // 2
            median = (newArr[index] + newArr[index-1]) / 2
        else:
            median = float(newArr[len(newArr)//2])
        return median
