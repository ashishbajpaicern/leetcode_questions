class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def combinationSumHelper(index=0, total=0, combination=[]):
            if total == target:
                result.append(combination[:])
                return

            if index >= len(candidates) or total > target:
                return

            # * Include candidates[index]
            combination.append(candidates[index])
            combinationSumHelper(index, total + candidates[index], combination)
            # * Don't include candidates[index]
            combination.pop()
            combinationSumHelper(index + 1, total, combination)

        combinationSumHelper()
        return result
