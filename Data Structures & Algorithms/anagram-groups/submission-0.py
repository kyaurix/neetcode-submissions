class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # the plan is to group in hashtable by sorted order
        groupedWords = {}
        for i in strs:
            if "".join(sorted(i)) in groupedWords:
                groupedWords["".join(sorted(i))].append(i)
            else:
                groupedWords["".join(sorted(i))] = [i]
        return list(groupedWords.values())