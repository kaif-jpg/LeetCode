#ms 36 beats 0.32%

# class Solution:
#     def largestAltitude(self, gain: List[int]) -> int:
#         highest_a = current_a = 0

#         for current_gain in gain:
#             current_a += current_gain
#             highest_a = max(highest_a, current_a)
#         return highest_a

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        s = m = 0

        for g in gain:
            s += g
            if s > m:
                m = s
        return m