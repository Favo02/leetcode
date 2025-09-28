class Solution {
public:
    int largestPerimeter(vector<int> &nums) {
        sort(nums.begin(), nums.end());
        int N = nums.size();
        for (int i = N - 1; i >= 2; i--) {
            int ii = i - 1;
            int iii = i - 2;
            if (nums[i] + nums[ii] > nums[iii] && nums[i] + nums[iii] > nums[ii] && nums[ii] + nums[iii] > nums[i])
                return nums[i] + nums[ii] + nums[iii];
        }
        return 0;
    }
};
