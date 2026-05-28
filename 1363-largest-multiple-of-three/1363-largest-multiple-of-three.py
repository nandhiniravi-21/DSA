class Solution:
    def largestMultipleOfThree(self, digits: list[int]) -> str:
        # Group digits by their remainders when divided by 3
        remainders = [[], [], []]
        for d in sorted(digits):  # Sorting first keeps remainder groups sorted ascending
            remainders[d % 3].append(d)
            
        total_sum = sum(digits)
        rem = total_sum % 3
        
        # Helper function to try removing 'count' items from a specific remainder queue
        def remove_digits(rem_type, count):
            if len(remainders[rem_type]) >= count:
                for _ in range(count):
                    remainders[rem_type].pop(0)
                return True
            return False

        # Apply greedy removals based on the total sum remainder
        if rem == 1:
            if not remove_digits(1, 1):
                remove_digits(2, 2)
        elif rem == 2:
            if not remove_digits(2, 1):
                remove_digits(1, 2)
                
        # Combine all leftover digits
        result_digits = remainders[0] + remainders[1] + remainders[2]
        # Sort in descending order to form the maximum number
        result_digits.sort(reverse=True)
        
        if not result_digits:
            return ""
            
        # If the largest number is 0, the entire number evaluates to 0
        if result_digits[0] == 0:
            return "0"
            
        return "".join(map(str, result_digits))
