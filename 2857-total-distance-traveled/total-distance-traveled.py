class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        total_fuel_used = 0
        
        while mainTank >= 5:
            mainTank -= 5
            total_fuel_used += 5
            
            if additionalTank >= 1:
                additionalTank -= 1
                mainTank += 1
                
        total_fuel_used += mainTank
        return total_fuel_used * 10
