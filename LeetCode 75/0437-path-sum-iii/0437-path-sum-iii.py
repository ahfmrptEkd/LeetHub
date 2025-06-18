# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # 접두사 합 딕셔너리 : key = prefix sum, value = frenquency of number
        # 초기에 0을 한번 넣어둠 (경로가 없는 경우 처리)
        prefix_sum = {0:1}

        # 결과 카운트
        count = 0

        def dfs(node, current_sum):
            nonlocal count

            if not node:
                return
            
            # 현재의 노드 까지의 prefix sum
            current_sum += node.val

            # 현재 prefix sum - targetSum 이 존재한다면, 그 두 지점 사이의 합이 targetSum 과 동일함
            count += prefix_sum.get(current_sum - targetSum, 0)

            # 딕셔너리에 합을 추가/업데이트
            prefix_sum[current_sum] = prefix_sum.get(current_sum, 0) + 1

            # 차일드 노드 탐색
            dfs(node.left, current_sum)
            dfs(node.right, current_sum)

            # 중요!! - backtracking
            # 현재 경로 탐색이 끝나면 해시맵에서 현재 접두사 합 제거하여 현재 경로가 다른 경로에 영향을 미치지 않도록 함
            prefix_sum[current_sum] -= 1
        
        dfs(root, 0)

        return count
