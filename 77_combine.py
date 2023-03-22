class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def dfs(n, k, i ,temp, ans):
            if k == 0: # taken up all digits
                ans.append(temp[:])
                return
            if i > n: # first availiable num larger than max 
                return
            for j in range(i,n+1):
                temp.append(j)
                dfs(n,k-1,j+1,temp,ans)
                temp.pop()
        temp,ans = [],[]
        dfs(n,k,1,temp,ans)
        return ans
