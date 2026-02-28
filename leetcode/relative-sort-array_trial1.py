class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        counts = Counter(arr1)
        result=[]
        for num in arr2:
            result.extend([num] * counts[num])
            counts[num] = 0
        unique = []
        for num in sorted(counts.keys()):
            if counts[num] > 0:
                unique.extend([num] * counts[num])
        result.extend(unique)
        return result