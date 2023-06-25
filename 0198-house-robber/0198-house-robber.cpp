class Solution {
public:
    int rob(vector<int>& nums) {
        vector<int> memory(nums.size() + 2, 0);
        for (int i = nums.size() - 1; i > -1; i--) {
            memory[i] = max(nums[i] + memory[i + 2], memory[i + 1]);   
        }
        return memory[0];
    }
};




