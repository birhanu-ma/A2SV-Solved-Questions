from collections import Counter
class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)
        total_counter = Counter(nums)
        print(total_counter)
        captain, total_count = total_counter.most_common(1)[0]
        print(captain)
        print(total_count)
        left_captain_count = 0
        for i in range(n - 1):
            if nums[i] == captain:
                left_captain_count += 1
            left_split_len = i + 1
            right_split_len = n - left_split_len
            right_captain_count = total_count - left_captain_count
            if left_captain_count * 2 > left_split_len and \
                right_captain_count * 2 > right_split_len:
                return i
        return -1
        
        



    
