from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        
        dict_target = Counter(t)
        filtered_string = [(i, x) for i, x in enumerate(list(s)) if x in dict_target.keys()]
        current_dict = {x: 0 for x in dict_target.keys()}
        
        required_substrings = len(dict_target)
        formed_substrings = 0
        l, r = 0, 0

        while r < len(filtered_string):
            left_index, left_char = filtered_string[l]
            right_index, right_char = filtered_string[r]
            
            current_dict[right_char] += 1
            
            if current_dict[right_char] == dict_target[right_char]:
                formed_substrings += 1
            
            if formed_substrings == required_substrings:
                temp = s[left_index: right_index + 1]
                if len(temp) < len(res) or res == "":
                    res = temp
                
                while l < r and formed_substrings == required_substrings:
                    current_dict[left_char] -= 1
                    if dict_target[left_char] > current_dict[left_char]:
                        formed_substrings -= 1
                        l += 1
                    else:
                        l += 1 
                        left_index, left_char = filtered_string[l]
                        temp = s[left_index: right_index + 1]
                        if len(temp) < len(res) or res == "":
                            res = temp               
            
            r += 1
        
        return res
                    
                    
                    
            
        