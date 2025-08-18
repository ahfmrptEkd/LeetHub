/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        // 노드가 하나뿐일 때는 nullptr 반환
        if (!head->next) {
            return nullptr;
        }

        ListNode* fast = head;
        ListNode* slow = head;

        // fast 포인터를 n만큼 앞으로 이동
        for (int i = 0; i < n; i++) {
            fast = fast->next;
        }
        
        // fast가 nullptr이면 첫 노드를 삭제
        if (!fast) {
            return head->next;
        }
        
        // fast->next가 nullptr일 때까지 이동하면
        // slow는 삭제할 노드 이전 위치에 도달
        while (fast->next) {
            fast = fast->next;
            slow = slow->next;
        }
        
        // 삭제할 노드를 건너뛰도록 연결 변경
        slow->next = slow->next->next;

        return head;
    }
};