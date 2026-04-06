class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        freq = {}
        for c in s:
            if c in freq:
                freq[c] = freq[c] + 1
            else:
                freq[c] = 1
        
        for c in t:
            if c in freq:
                freq[c] = freq[c] - 1
                if freq[c] == 0:
                    del freq[c]
            else:
                return False
        
        return len(freq) == 0
