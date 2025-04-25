/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    TreeNode* deleteNode(TreeNode* root, int key) {
        if (!root) return nullptr;

        if (key < root->val) {
            root->left = deleteNode(root->left, key);
        }
        else if (key > root->val) {
            root->right = deleteNode(root->right, key);
        }
        // 키를 찾고 삭제해야함
        else {

            // 케이스 1: 자식 없음
            if (!root->left && !root->right) {
                delete root;
                return nullptr;
            }

            // 케이스 2: 오른쪽 자식만 있는 경우
            else if (!root->left) {
                TreeNode* temp = root->right;
                delete root;
                return temp;
            }

            // 케이스 3: 왼쪽 자식만 있는 경우
            else if (!root->right) {
                TreeNode* temp = root->left;
                delete root;
                return temp;   
            }

            // 케이스 둘다 있는 경우
            else {
                // 오른쪽 서브 트리에서 가장 작은 값 찾기
                TreeNode* successor = findMin(root->right);

                // 후계자 대체
                root->val = successor->val;

                // 후계자 노드 삭제
                root->right = deleteNode(root->right, successor->val);
            }
        }
        return root;
    }
private:
    TreeNode* findMin(TreeNode* node) {
        TreeNode* current = node;

        while (current && current->left) {
            current = current->left;
        }

        return current;
    }
};