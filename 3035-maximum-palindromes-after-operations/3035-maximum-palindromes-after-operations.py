from collections import Counter

class Solution:
    def maxPalindromesAfterOperations(self, words: list[str]) -> int:
        # Step 1: Pool all characters together and count total pairs available
        total_counts = Counter()
        for word in words:
            total_counts.update(word)
            
        available_pairs = sum(count // 2 for count in total_counts.values())
        
        # Step 2: Sort the word lengths in ascending order
        lengths = sorted(len(word) for word in words)
        
        palindrome_count = 0
        
        # Step 3: Greedily satisfy shorter lengths first
        for L in lengths:
            needed_pairs = L // 2
            
            if available_pairs >= needed_pairs:
                available_pairs -= needed_pairs
                palindrome_count += 1
            else:
                # If we don't have enough pairs, we can't form any more palindromes
                break
                
        return palindrome_count
