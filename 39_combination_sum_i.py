class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        def dfs(cand, t, i, temp, ans):
            if i == len(cand) or cand[i] > t:
                return
            if cand[i] == t:
                temp.append(cand[i])
                ans.append(temp[:])
                temp.pop()
            temp.append(cand[i])
            dfs(cand,t-cand[i], i, temp, ans) #  take cand[i] not move on 
            #dfs(cand,t-cand[i], i+1, temp, ans)
            
            temp.pop()
            dfs(cand,t, i+1, temp, ans) #  not take cand[i] and move on 
        temp, ans = [], []
        dfs(candidates, target, 0, temp, ans)
        return ans
