class Solution {
public:
    bool canSortArray(vector<int>& nums) {

        vector<int> bits;
        for (auto n : nums) {

            int ones = 0;
            for (int i = 0; i <= 8; i++) {
                if ((n & (1 << i)) != 0) {
                    ones++;
                }
            }
            bits.push_back(ones);
        }

        for (int i = 0; i < nums.size(); i++) {
            for (int ii = i+1; ii < nums.size(); ii++) {
                if (nums[i] > nums[ii]) {
                    if (bits[i] != bits[ii]) {
                        return false;
                    }
                    swap(nums[i], nums[ii]);
                }
            }
        }

        return true;
    }
};
