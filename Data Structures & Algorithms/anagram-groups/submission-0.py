from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        r=defaultdict(list)

        for word in strs:
            sorted_word=''.join(sorted(word))

            r[sorted_word].append(word)

        return list(r.values())
