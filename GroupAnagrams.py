from collections import defaultdict
def groupAnagrams(strs):
        res=defaultdict(list) # mapping charCount to list of Anagram
        for s in strs:
            count = [0] * 26 # a...z
            for c in s:
                count[ord(c)-ord("a")]+=1
            res[tuple(count)].append(s)

        return list(res.values())

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))