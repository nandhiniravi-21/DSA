class Solution:
    def longestWord(self, words: list[str]) -> str:
        # Create a set for O(1) lookups
        word_set = set(words)
        
        # Sort words: longest first; if lengths are equal, alphabetically smaller first
        words.sort(key=lambda w: (-len(w), w))
        
        for word in words:
            is_valid = True
            
            # Check all prefixes of the current word
            for i in range(1, len(word)):
                if word[:i] not in word_set:
                    is_valid = False
                    break
                    
            # The first valid word we encounter is our best answer
            if is_valid:
                return word
                
        return ""
