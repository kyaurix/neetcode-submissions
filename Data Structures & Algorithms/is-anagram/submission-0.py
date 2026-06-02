class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_freq = {}
        t_freq = {}
        for char in s:
            #if it is in we increm
            if char in s_freq:
                s_freq[char] = s_freq[char] + 1
            #if its not in we set it to 1
            else: 
                s_freq[char] = 1
        for char in t:
            #if it is in we increm
            if char in t_freq:
                t_freq[char] = t_freq[char] + 1
            #if its not in we set it to 1
            else: 
                t_freq[char] = 1
        if s_freq == t_freq:
            return True
        else:
            return False