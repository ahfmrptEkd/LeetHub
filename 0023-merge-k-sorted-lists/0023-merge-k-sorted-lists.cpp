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
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        // 리스트가 비어있는 경우 처리
        if (lists.empty()) {
            return nullptr;
        }
        
        // (노드값, 리스트 인덱스, 노드) 형태로 힙에 저장하기 위한 구조체
        struct HeapNode {
            int val;
            int index;
            ListNode* node;
            
            bool operator>(const HeapNode& other) const {
                return val > other.val;
            }
        };
        
        priority_queue<HeapNode, vector<HeapNode>, greater<HeapNode>> heap;
        
        // 각 리스트의 첫 노드를 힙에 추가
        for (int i = 0; i < lists.size(); i++) {
            if (lists[i]) {
                heap.push({lists[i]->val, i, lists[i]});
            }
        }
        
        ListNode dummy(0);
        ListNode* curr = &dummy;
        
        // 힙이 빌 때까지 반복
        while (!heap.empty()) {
            HeapNode current = heap.top();
            heap.pop();
            
            curr->next = current.node;
            curr = curr->next;
            
            // 다음 노드가 있으면 힙에 추가
            if (current.node->next) {
                heap.push({current.node->next->val, current.index, current.node->next});
            }
        }
        
        return dummy.next;
    }
};