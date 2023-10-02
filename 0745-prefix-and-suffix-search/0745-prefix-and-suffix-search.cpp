class TrieNode {
public:
    std::vector<TrieNode*> children;
    int index;

    TrieNode() : children(27, nullptr), index(-1) {}
};

class Trie {
public:
    TrieNode* root;

    Trie() {
        root = new TrieNode();
    }

    void insert(const std::string& word, int position) {
        TrieNode* current = root;
        int N = word.length();
        for (int i = 0; i < N; ++i) {
            int index = word[i] - 'a';
            if (!current->children[index])
                current->children[index] = new TrieNode();
            current->index = position;
            current = current->children[index];
        }
        current->index = position;
    }

    int search(const std::string& word) {
        TrieNode* current = root;
        int N = word.length();
        for (int i = 0; i < N; ++i) {
            int index = word[i] - 'a';
            if (!current->children[index])
                return -1;
            current = current->children[index];
        }
        return current->index;
    }
};

class WordFilter {
public:
    Trie trie;

    WordFilter(const std::vector<std::string>& words) {
        for (int index = 0; index < words.size(); ++index) {
            const std::string& word = words[index];
            int N = word.length();
            for (int i = 0; i <= N; ++i)
                trie.insert(word.substr(i) + "{" + word, index);
        }
    }

    int f(const std::string& pref, const std::string& suff) {
        std::string word = suff + "{" + pref;
        return trie.search(word);
    }
};
