class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        inc_queue = deque()
        dec_queue = deque()
        window = []
        left = 0
        max_len = 0
        for i in range(len(nums)):
            window.append(nums[i])
            while dec_queue and dec_queue[-1]<nums[i]:
                dec_queue.pop()
            while inc_queue and inc_queue[-1]>nums[i]:
                inc_queue.pop()
            dec_queue.append(nums[i])
            inc_queue.append(nums[i])
            while dec_queue and inc_queue and dec_queue[0]-inc_queue[0]>limit:
                if nums[left]==dec_queue[0]:
                    dec_queue.popleft()
                if nums[left] == inc_queue[0]:
                    inc_queue.popleft()
                left+=1
            max_len = max(max_len, i-left+1)
        return max_len
            




                



        
