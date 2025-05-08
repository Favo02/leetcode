class Solution {
public:
    vector<int> buildArray(vector<int>& nums) {
        int N = nums.size();
        vector<int> res(N);
        for (int i = 0; i < N; i++) {
            res[i] = nums[nums[i]];
        }
        return res;
    }
};
