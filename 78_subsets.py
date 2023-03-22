class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(nums, i, l, temp, ans):
            if len(temp) == l:
                ans.append(temp[:])
                return
            for j in range(i, len(nums)):
                temp.append(nums[j])
                dfs(nums, j+1,l, temp, ans)
                temp.pop()
        temp,ans=[],[]
        for l in range(len(nums)+1):
            dfs(nums,0,l,temp,ans)
        return ans
