class Solution:
    #start with left
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1 , p2 = m-1, n-1
        i = m+n-1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] >= nums2[p2]:
                nums1[i] = nums1[p1]
                p1 -= 1
            else:
                nums1[i] = nums2[p2]
                p2 -= 1
            i -= 1
        nums1[:p2+1] = nums2[:p2+1]

    #start with right
    def merge2(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1_copy = nums1[:m]
        nums1[:] = []
        p1, p2 = 0, 0

        while p1 < m and p2 < n:
            if nums1_copy[p1] <= nums2[p2]:
                nums1.append(nums1_copy[p1])
                p1 += 1

            else:
                nums1.append(nums2[p2])
                p2 += 1
        if p1 < m:
            nums1[p1+p2:] = nums1_copy[p1:]
        if p2 < n:
            nums1[p1+p2:] = nums2[p2:]
