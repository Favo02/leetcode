class Solution {
public:
    int maxAdjacentDistance(vector<int>& nums) {
        int N = nums.size();
        int res = abs(nums[N-1] - nums[0]);
        for (int i = 1; i < N; i++) {
            res = max(res, abs(nums[i] - nums[i-1]));
        }
        return res;
    }
};
