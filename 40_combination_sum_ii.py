class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        def dfs(cand, target, i, temp, ans):
            if target == 0:
                ans.append(temp[:])
                return
            for j in range(i, len(cand)):
                if j > i and cand[j] == cand[j-1]:
                    continue
                if cand[j] > target:
                    return
                temp.append(cand[j])
                dfs(cand, target - cand[j], j+1, temp, ans)
                temp.pop()
            
        temp, ans = [], []
        dfs(candidates, target, 0, temp, ans)
        return ans
