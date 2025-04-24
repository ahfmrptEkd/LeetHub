/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
public class Solution {
    public IList<int> RightSideView(TreeNode root) {
        // 결과를 저장할 리스트 초기화
        var result = new List<int>();
        
        if (root == null) {
            return result;
        }
        
        // BFS를 위한 큐 초기화, 시작 노드 추가
        var queue = new Queue<TreeNode>();
        queue.Enqueue(root);
        
        // 큐가 빌 때까지 반복 (모든 레벨을 순회)
        while (queue.Count > 0) {
            // 현재 레벨의 노드 개수
            int levelSize = queue.Count;
            
            // 현재 레벨의 모든 노드를 처리
            for (int i = 0; i < levelSize; i++) {
                TreeNode node = queue.Dequeue();
                
                // 현재 레벨의 마지막 노드인 경우 (= 오른쪽에서 보이는 노드)
                if (i == levelSize - 1) {
                    result.Add(node.val);
                }
                
                // 왼쪽 자식을 큐에 추가
                if (node.left != null) {
                    queue.Enqueue(node.left);
                }
                // 오른쪽 자식을 큐에 추가
                if (node.right != null) {
                    queue.Enqueue(node.right);
                }
            }
        }
        
        return result;
    }
}