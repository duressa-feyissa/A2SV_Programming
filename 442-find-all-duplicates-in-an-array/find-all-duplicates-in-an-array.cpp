#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    vector<int> findDuplicates(vector<int>& nums) {
        int size = nums.size();
        vector <int> answer;

        for (int i = 0; i < size;) {
            if (nums[i] == i + 1) {
                i++;
            }
            else {
                int correct = nums[i] - 1;
                if (nums[correct] == nums[i]) {
                    answer.push_back(nums[i]);
                    i += 1;
                } else if (nums[i] < i + 1) {
                    nums[correct] = nums[i];
                    i += 1;
                } else {
                    swap(nums[correct], nums[i]);
                }
            }
        }

        return answer;
    }
};