class Solution {
public:
    int minOperations(vector<int>& nums) {
        int N = nums.size();
        int res = 0;
        for (int i = 0; i < N-2; i++) {
            if (nums[i] == 1) continue;
            nums[i] = 1;
            nums[i+1] = 1 - nums[i+1];
            nums[i+2] = 1 - nums[i+2];
            res++;
        }
        if (nums[N-1] == 1 && nums[N-2] == 1) {
            return res;
        }
        return -1;
    }
};
