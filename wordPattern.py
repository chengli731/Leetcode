class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        splitstr= str.split(" ")
        str_length = len(splitstr)
        pattern_length = len(pattern)
        
        # should take this else out as a sanity check
        if str_length != pattern_length:
            return False
  
        dic_pattern = {}
        dic_str = {}
        for i in range(str_length):
             elif pattern[i] not in dic_pattern and splitstr[i] not in dic_str:
                 dic_pattern[pattern[i]] = splitstr[i]
                 dic_str[splitstr[i]] = pattern[i]
             elif pattern[i] in dic_pattern and dic_pattern[pattern[i]]!= splitstr[i]:
                 return False
             elif splitstr[i] in dic_str and dic_str[splitstr[i]]!= pattern[i]:
                 return False
        return True
