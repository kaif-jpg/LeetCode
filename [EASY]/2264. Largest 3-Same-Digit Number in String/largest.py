class Solution:
    def largestGoodInteger(self, num: str) -> str:
        
        good = ""
        for i in range (len(num) - 2):
            trp = num[i:i+3]
            if trp[0] == trp[1] == trp[2]:
                if good == "" or trp > good:
                     good = trp
        return good