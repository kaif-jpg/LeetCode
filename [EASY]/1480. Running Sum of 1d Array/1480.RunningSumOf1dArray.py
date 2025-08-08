from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        current = 0
        answer = []
        for i in range(n):
            current += nums[i]
            answer.append(current)
        return answer
 

 
# if __name__ == "__main__":
#      nums = [1, 2, 3, 4] 
#      result = Solution().runningSum(nums)
#      print(result)  