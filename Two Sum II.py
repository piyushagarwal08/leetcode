class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i=0
        while True:
            val=target-numbers[i]
            if val in numbers:
                break
            else:
                i+=1
        return [i+1,numbers[i+1:].index(val)+i+2]
