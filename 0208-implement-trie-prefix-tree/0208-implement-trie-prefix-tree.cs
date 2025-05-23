public class Trie {

    public Trie() {
        node = new Dictionary<char, Trie>();
        is_end = false;
    }
    
    public void Insert(string word) {
        Trie curr = this;
        foreach(char c in word) {
            if (!curr.node.ContainsKey(c)){
                curr.node[c] = new Trie();
            }
            curr = curr.node[c];
        }
        curr.is_end = true;
    }
    
    public bool Search(string word) {
        Trie curr = this;
        foreach(char c in word) {
            if (!curr.node.ContainsKey(c)) {
                return false;
            }
            curr = curr.node[c];
        }
        return curr.is_end;
    }
    
    public bool StartsWith(string prefix) {
        Trie curr = this;
        foreach (char c in prefix){
            if (!curr.node.ContainsKey(c)){
                return false;
            }
            curr = curr.node[c];
        }
        return true;
    }

    private Dictionary<char, Trie> node;
    private bool is_end;
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.Insert(word);
 * bool param_2 = obj.Search(word);
 * bool param_3 = obj.StartsWith(prefix);
 */