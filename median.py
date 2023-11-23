class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        lis3=nums1+nums2
        lis3.sort()
        if(len(lis3)%2==0):
            mid=int(len(lis3)/2)
            sum=float((lis3[mid]+lis3[mid-1])/2)
            med=format(sum,'.5f')
            return float(med)
        else:
            mid=int(len(lis3)/2)
            med=format(lis3[mid],'.5f')
            return float(med)