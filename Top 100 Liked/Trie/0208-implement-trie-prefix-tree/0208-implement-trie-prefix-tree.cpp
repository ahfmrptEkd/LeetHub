class Trie {
public:
    Trie() {
        
    }
    
    void insert(string word) {
        Trie* curr = this;
        for(char c : word) {
            if (!curr->node.contains(c)) {
                curr->node[c] = new Trie();
            }
            curr = curr->node[c];
        }
        curr->is_end = true;
    }
    
    bool search(string word) {
        Trie* curr = this;
        for (char c : word) {
            if (!curr->node.contains(c)){
                return false;
            }
            curr = curr->node[c];
        }
        return curr->is_end;
    }
    
    bool startsWith(string prefix) {
        Trie* curr = this;
        for (char c : prefix) {
            if (!curr->node.contains(c)){
                return false;
            }
            curr = curr->node[c];
        }
        return true;
    }

private:
    unordered_map<char, Trie*> node;
    bool is_end = false;
};
/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */