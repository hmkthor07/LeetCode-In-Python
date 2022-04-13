"""
Given an array of strings, 
group anagrams together

An anagram is a word formed by re-arranging the letters of a different word.

"""

from typing import List
class Solution:
    def groupAnagrams(self, letters:List[str]) -> List[List[str]]:
        
        # 각 단어 정렬하고 맵 써야 한다. 

        my_map = {}
        answer_map = {}
        for letter in letters:
            my_map[letter] = ''.join(sorted(letter))

        for letter in my_map:
            if my_map[letter] in answer_map:
                answer_map[my_map[letter]] += (letter,)
            else:
                answer_map[my_map[letter]] = (letter,)

        new_list = []
        for each_list in answer_map.values():
            new_list.append(list(each_list))

        return new_list

    def groupAnagramsSimpler(self, letters:List[str]) -> List:

        answer = []
        hashMap = {} # SC : O(N)

        for letter in letters: # TC O(N)
            if ''.join(sorted(letter)) in hashMap:  # Sorted : T.C. O(NlogN) 
                hashMap[''.join(sorted(letter))].append(letter)
            else:
                hashMap[''.join(sorted(letter))] = [letter]
        

        for l in hashMap.values():
            answer.append(l)

        return answer

s = Solution()
answer = s.groupAnagramsSimpler(["eat", "tea", "tan", "ate", "nat", "bat"])
print(answer)