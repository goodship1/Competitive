class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        if num1 == 0 or num2 ==0: 
            return 0 
        count = 0
        while num1 !=0 or num2 !=0:
            count += 1
            if num1 >=num2:
                num1 = num1 - num2
                print(num1)
            elif num1 <= num2:
                num2 = num2 - num1
            if num1==0 or num2 == 0:
                break
        return count
            
