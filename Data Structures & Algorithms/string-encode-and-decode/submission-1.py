class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            length = len(s)
            result += str(length)
            result += "#"
            result += s
        print(result)
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = i;
            while s[j] != "#":
                j+=1
            length = int(s[i: j])
            substring = s[j+1: j+length+1]
            result.append(substring)
            i = j + length + 1
            print(result)
        return result
