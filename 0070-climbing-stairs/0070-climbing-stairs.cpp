class Solution {
public:
    int climbStairs(int n) {
        if (n == 1) return 1;
        int n1 = 1, n2 = 2;
        for (int i = 3; i <= n; i++) {
            int temp = n2;
            n2 = n2 + n1;
            n1 = temp;
        }
        return n2;
    }
};