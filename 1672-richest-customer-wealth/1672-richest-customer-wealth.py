class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth=[]
        for customer in accounts:
            wealth.append(sum(customer))
        return max(wealth)
        