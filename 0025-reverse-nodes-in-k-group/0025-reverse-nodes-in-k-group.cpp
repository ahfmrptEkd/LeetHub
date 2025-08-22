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
private:
    bool has_node(ListNode* curr, int k) {
        ListNode* temp = curr;
        
        for (int i = 0; i < k; i++) {
            if (!temp) {
                return false;
            }
            temp = temp->next;
        }
        return true;
    }

public:
    ListNode* reverseKGroup(ListNode* head, int k) {
        /*
        k의 원소를 k-1만큼 그걸 다음것과 연결
        다음 원소가 k 만큼 남았는지 확인 필요
        없으면 나머지는 그대로.
        */
        if (k == 1) {
            return head;
        }

        ListNode* ans = new ListNode(0);
        ans->next = head;
        ListNode* prev = ans;
        ListNode* curr = prev->next;
        
        while (curr && has_node(curr, k)) {
            for (int i = 0; i < k - 1; i++) {  // k 번 순서 바꾸기
                ListNode* temp = curr->next;    // 다음 노드
                curr->next = temp->next;   // 다다음 노드를 봄
                temp->next = prev->next;    // 다음 노드가 바뀐 자리의 노드를 보고
                prev->next = temp; // 현재 노드가 다음노드가 되는 자리 바뀜.
            }

            /// 여기에 바뀐 마지막 원소의 자리로 봐야하러 같은데.
            prev = curr;
            curr = curr->next;
        }

        return ans->next;
    }
};