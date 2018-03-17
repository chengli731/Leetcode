Python 3.6.0 (v3.6.0:41df79263a11, Dec 22 2016, 17:23:13) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.
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
        if str_length != pattern_length:
            return False
        else:
            dic_pattern = {}
            dic_str = {}
            for i in range(str_length):
                if pattern[i] not in dic_pattern and splitstr[i] not in dic_str:
                    dic_pattern[pattern[i]] = splitstr[i]
                    dic_str[splitstr[i]] = pattern[i]
                if pattern[i] in dic_pattern and dic_pattern[pattern[i]]!= splitstr[i]:
                    return False
                if splitstr[i] in dic_str and dic_str[splitstr[i]]!= pattern[i]:
                    return False
            return True
