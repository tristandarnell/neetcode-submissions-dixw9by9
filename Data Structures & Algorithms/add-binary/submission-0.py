class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1
        carry = 0

        ans = []
        while (i >= 0 or j >= 0 or carry > 0):
            digitA = int(a[i]) if i >= 0 else 0
            digitB = int(b[j]) if j >= 0 else 0

            sumD = digitA + digitB + carry
            ans.append(sumD % 2)
            carry = sumD // 2
            i-=1
            j-=1
        ans.reverse()
        return "".join(map(str, ans))