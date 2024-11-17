#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {

        int res = 1e9;

        int sum = 0;
        int start = 0;
        for (int end = 0; end < nums.size(); end++) {
            sum += nums[end];

            while (sum - nums[start] >= target) {
                sum -= nums[start];
                start++;
            }

            if (sum >= target) res = min(res, end-start+1);
        }

        return res == 1e9 ? 0 : res;
    }
};
