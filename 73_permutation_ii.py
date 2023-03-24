class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def dfs(nums, d, used, temp, ans):
            """
            nums: List[int] sorted
            d: int depth of dfs 
            used: List[bool]
            temp: List[int]
            ans: List[List[int]]
            rtype: void
            """
            if d == len(nums):
                ans.append(temp[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                used[i] = True
                temp.append(nums[i])
                dfs(nums,d+1,used, temp, ans)
                temp.pop()
                used[i] = False
        nums.sort()
        ans = []
        dfs(nums,0,[False for i in range(len(nums))],[],ans)
        return ans
