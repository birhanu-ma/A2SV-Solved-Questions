class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        ptr = len(arr) - 1
        sorted_arr = sorted(arr)
        ans = []
        while arr != sorted_arr:
            max_num = max(arr[:ptr + 1])
            index = arr.index(max_num)
            temp = []
            if not index:
                temp = arr[:ptr + 1]
                temp.reverse()
                if ptr + 1 < n:
                    temp += arr[ptr + 1:]
            else:
                temp = arr[:index + 1]
                temp.reverse()
                if index + 1 < n:
                    temp += arr[index + 1:]

            if index: ans.append(index + 1)
            else: ans.append(ptr + 1)
            arr = temp
            new_index = arr.index(max_num)
            if new_index == ptr:
                ptr -= 1
        return ans

        



        
