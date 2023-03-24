class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(nums, s, used, temp, ans):
            if s == len(nums):
                ans.append(temp[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True
                temp.append(nums[i])
                dfs(nums,s+1,used,temp,ans)
                temp.pop()
                used[i] = False
        used= [False]*len(nums)
        temp, ans = [], []
        dfs(nums,0,used, temp,ans)
        return ans
