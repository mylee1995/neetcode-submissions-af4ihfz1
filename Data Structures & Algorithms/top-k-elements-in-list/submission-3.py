class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        import heapq
        max_heap = []
        for number, frequency in freq.items():
            heapq.heappush(max_heap, (-frequency, number)) # negate frequency to mimic max heap

        result = []
        for i in range(0, k):
            result.append(heapq.heappop(max_heap)[1])

        return result