class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        result = {}
        for index, char in enumerate(s):
            if char not in result:
                result[char] = [index]  
            else:
                result[char].append(index) 
        char_length = []
        for char in result:
             char_index = result[char]
             end = max(char_index)
             start = min(char_index)
             char_length.append([start, end])
        first_char_len=char_length[0]
        min_idx = first_char_len[0]
        max_idx = first_char_len[1]
        boundary = []
        for [char_min_idx, char_max_idx] in char_length:
             if min_idx <=char_min_idx<=max_idx:      
                min_idx = min(min_idx, char_min_idx)
                max_idx = max(max_idx, char_max_idx)
             else:
                    boundary.append([min_idx, max_idx])
                    min_idx = char_min_idx
                    max_idx = char_max_idx
        boundary.append([min_idx, max_idx])
        num_char_per_slice = []
        for idx_srt, idx_end in boundary:
             diff = idx_end - idx_srt
             num_char_per_slice.append(diff+1)
        return num_char_per_slice
                    
        
