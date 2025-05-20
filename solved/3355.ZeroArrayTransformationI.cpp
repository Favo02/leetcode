class Solution {
public:
    bool isZeroArray(vector<int>& nums, vector<vector<int>>& queries) {
        int N = nums.size();
        int Q = queries.size();
        vector<int> diff(N+1);

        for (int i = 0; i < Q; i++) {
            diff[queries[i][0]]++;
            diff[queries[i][1]+1]--;
        }

        int sum = 0;
        for (int i = 0; i < N; i++) {
            sum += diff[i];
            if (sum < nums[i]) return false;
        }

        return true;
    }
};
