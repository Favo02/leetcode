class Solution {
public:
    int triangleNumber(vector<int> &nums) {
        sort(nums.begin(), nums.end());

        int res = 0;
        int N = nums.size();
        for (int iii = N - 1; iii >= 2; iii--) {
            int i = 0;
            int ii = iii - 1;
            while (i < ii) {
                if (nums[i] + nums[ii] > nums[iii]) {
                    res += ii - i;
                    ii--;
                } else {
                    i++;
                }
            }
        }
        return res;
    }
};
