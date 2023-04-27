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
#include <deque>

class Solution {
public:
    vector<double> averageOfLevels(TreeNode* root) {
        deque<TreeNode*> Queue;
        Queue.push_back(root);
        vector<double> answer;
        
        while (!Queue.empty()) {
            int N = Queue.size();
            double add = 0;
            for (int i = 0; i < N; i++) {
                TreeNode* popped = Queue.front(); 
                Queue.pop_front();
                add += popped->val;
                if (popped->left)
                    Queue.push_back(popped->left);
                if (popped->right)
                    Queue.push_back(popped->right);
            }
            answer.push_back(add / N);
        }
        
        return answer;
        
    }
};