class Solution:
    def checkArithmeticSubarrays(self, nums: list[int], l: list[int], r: list[int]) -> list[bool]:
        answer = []
        
        # Process each query independently
        for left, right in zip(l, r):
            subarray = nums[left:right+1]
            min_val = min(subarray)
            max_val = max(subarray)
            k = len(subarray)
            
            # Case 1: All elements are identical (e.g., [7, 7, 7])
            if min_val == max_val:
                answer.append(True)
                continue
                
            # Case 2: The span cannot be divided into k - 1 even steps
            if (max_val - min_val) % (k - 1) != 0:
                answer.append(False)
                continue
                
            diff = (max_val - min_val) // (k - 1)
            num_set = set(subarray)
            is_arithmetic = True
            
            # Case 3: Verify if every expected step exists in the set
            for j in range(k):
                expected_val = min_val + j * diff
                if expected_val not in num_set:
                    is_arithmetic = False
                    break
                    
            answer.append(is_arithmetic)
            
        return answer
