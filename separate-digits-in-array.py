class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        num_str = "".join(str(item) for item in nums)
        str_list = list(num_str)
        int_list = [int(num) for num in str_list]
        return int_list
