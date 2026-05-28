class Solution:
    def sortVowels(self, s: str) -> str:
        # Step 1: Define the set of valid vowels
        vowels_set = set("aeiouAEIOU")
        
        # Step 2: Extract and sort all vowels present in the string
        extracted_vowels = sorted([char for char in s if char in vowels_set])
        
        # Step 3: Rebuild the string with sorted vowels in place
        result = []
        vowel_index = 0
        
        for char in s:
            if char in vowels_set:
                result.append(extracted_vowels[vowel_index])
                vowel_index += 1
            else:
                result.append(char)
                
        return "".join(result)
