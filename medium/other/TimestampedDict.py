class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.time_dict_sorted_list = dict()
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_dict_sorted_list.keys():
            self.time_dict_sorted_list[key] = [[timestamp, value]]
        else:
            self.time_dict_sorted_list[key].append([timestamp, value])
            
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_dict_sorted_list.keys():
            return ""
        else:
            index = bisect.bisect_right(self.time_dict_sorted_list[key], [timestamp + 1])
            if index == 0:
                return ""
            return self.time_dict_sorted_list[key][index - 1][1]
            


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)