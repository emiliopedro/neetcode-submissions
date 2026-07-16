class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        anagrams = {}
        for word in strs:
            freq = [0]*26
            for letter in word:
                freq[letters.index(letter)] += 1 

            freq = tuple(freq)
            if freq not in anagrams:
                anagrams[freq] = [word]
            else:
                anagrams[freq].append(word)

        result = []
        for item in anagrams.values():
            result.append(item)
        
        return result