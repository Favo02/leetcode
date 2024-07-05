class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        keys = map(lambda k: [k] * min(c1[k], c2[k]), c1.keys() & c2.keys())
        return list(chain.from_iterable(keys))
