class Solution {
public:
    int rob(vector<int>& nums) {
        int first = 0, second = 0;
        for (int i = nums.size() - 1; i > -1; i--) {
            int temp = first;
            first = max(nums[i] + second, first);
            second = temp;
        }
        return max(first, second);
    }
};




