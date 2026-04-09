import string 

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create map for each word
        topLevelMap = {}
        for s in strs:
            freqMap = self.createFrequencyMap(s)

            if freqMap in topLevelMap:
                topLevelMap[freqMap].append(s)
            else:
                topLevelMap[freqMap] = [s]
        
        result = []
        for val in topLevelMap.values():
            result.append(val)

        return result


    def createFrequencyMap(self, s: str) -> str:
        freqMap = [0] * 26
        for c in s:
            freqMap[string.ascii_lowercase.index(c)] += 1

    
        return str(freqMap)