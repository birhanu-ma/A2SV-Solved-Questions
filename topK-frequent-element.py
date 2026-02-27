class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter =Counter(nums)
        top_k = []
        for i in range(k):
            max_key = max(counter, key= counter.get)
            top_k.append(max_key)
            del counter[max_key]
        return top_k
