class TrieNode {
public:
    TrieNode* children[2];
    
    TrieNode() {
        children[0] = nullptr;
        children[1] = nullptr;
    }
};

class Trie {
private:
    TrieNode* root;
    
public:
    Trie() {
        root = new TrieNode();
    }
    
    void addNumber(int num) {
        TrieNode* current = root;
        for (int i = 31; i >= 0; i--) {
            int bit = (num >> i) & 1;
            if (!current->children[bit]) {
                current->children[bit] = new TrieNode();
            }
            current = current->children[bit];
        }
    }
    
    int findMaxXOR(int num) {
        TrieNode* current = root;
        int result = 0;
        for (int i = 31; i >= 0; i--) {
            int bit = (num >> i) & 1;
            int flip = bit ^ 1;
            if (current->children[flip]) {
                result |= (1 << i);
                current = current->children[flip];
            } else {
                current = current->children[bit];
            }
        }
        return result;
    }
};

class Solution {
public:
    int findMaximumXOR(std::vector<int>& nums) {
        int result = 0;
        int N = nums.size();
        Trie* trie = new Trie();
        for (int i = 0; i < N; i++) {
            trie->addNumber(nums[i]);
            result = std::max(result, trie->findMaxXOR(nums[i]));
        }
        return result;
    }
};