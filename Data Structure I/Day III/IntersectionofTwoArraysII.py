# Given two integer arrays nums1 and nums2, return an array of their intersection. 
# Each element in the result must appear as many times as it shows in both arrays 
# and you may return the result in any order.

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        commons = list(set(nums1.copy()).intersection(set(nums2.copy())))
        commonsList = list()
        for i in commons:
            k = nums1.count(i)
            l = nums2.count(i)
            if k < l:    
                j = 0
                while j < k:
                    commonsList.append(i)
                    j += 1
            else:
                j = 0
                while j < l:
                    commonsList.append(i)
                    j += 1
        return commonsList
        
sol = Solution()
nums1 = [1,2,2,1]
nums2 = [2,2]
sol.intersect(nums1,nums2)


