class Solution(object):
    def maxWidthRamp(self, A):
        ans = 0
        m = float('inf')
        for i in sorted(range(len(A)), key = A.__getitem__):
            ans = max(ans, i - m)
            m = min(m, i)
        return ans
val=Solution()
a=list(map(int,input().split()))
print(val.maxWidthRamp(a))
