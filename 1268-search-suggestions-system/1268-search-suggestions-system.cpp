class Solution {
public:
    vector<vector<string>> suggestedProducts(vector<string>& products, string searchWord) {
        // 1단계: 제품들을 사전순으로 정렬
        sort(products.begin(), products.end());
        
        // 2단계: Trie 구축
        struct TrieNode {
            unordered_map<char, TrieNode*> children;  // 자식 노드들
            vector<string> suggestions;               // 해당 prefix의 제안 목록 (최대 3개)
        };
        
        TrieNode* root = new TrieNode();
        
        // 각 제품을 Trie에 삽입하면서 각 노드에 제안 목록 저장
        for (const string& product : products) {
            TrieNode* currentNode = root;
            
            // 제품명의 각 문자를 따라 Trie 구축
            for (char c : product) {
                if (currentNode->children.find(c) == currentNode->children.end()) {
                    currentNode->children[c] = new TrieNode();
                }
                
                // 다음 노드로 이동
                currentNode = currentNode->children[c];
                
                // 현재 제품을 제안 목록에 추가 (최대 3개까지)
                if (currentNode->suggestions.size() < 3) {
                    currentNode->suggestions.push_back(product);
                }
                // 현재 product는 사전순으로 더 뒤에 있으면, 추가 안함.
            }
        }
        
        // 3단계: 검색어의 각 글자마다 제안 목록 생성
        vector<vector<string>> result;
        TrieNode* currentNode = root;
        
        for (char c : searchWord) {
            // 현재 노드에서 해당 문자로 이동할 수 있는지 확인
            if (currentNode && currentNode->children.find(c) != currentNode->children.end()) {
                currentNode = currentNode->children[c];  //  다음 노드로 이동
                result.push_back(currentNode->suggestions);  //  이동한 노드의 제안 목록 추가
            } else {
                result.push_back({});
                currentNode = nullptr;  // 이후 모든 검색이 실패하도록 설정
            }
        }
        
        return result;
    }
};
