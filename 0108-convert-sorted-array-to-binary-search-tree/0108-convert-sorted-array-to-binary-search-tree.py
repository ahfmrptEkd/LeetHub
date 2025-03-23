# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:  # 빈 배열이면 None 반환
            return None
            
        middle = len(nums)//2  # 배열의 중간 인덱스 찾기
        
        # 중간 값으로 루트 노드 생성
        root = TreeNode(nums[middle])
        
        # 왼쪽 절반의 배열로 왼쪽 서브트리 재귀적 생성
        root.left = self.sortedArrayToBST(nums[:middle])
        # 오른쪽 절반의 배열로 오른쪽 서브트리 재귀적 생성
        root.right = self.sortedArrayToBST(nums[middle+1:])
        
        return root
                