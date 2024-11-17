#include <bits/stdc++.h>
using namespace std;

#define ll long long

class Solution {
public:
    int shortestSubarray(vector<int>& nums, int k) {

        int res = 1e9;

        ll sum = 0;
        ll neg = 0;
        int start = 0;

        for (int end = 0; end < nums.size(); end++) {
            sum += nums[end];

            if (sum < 0) {
                start = end+1;
                sum = 0;
                continue;
            }

            if (nums[end] < 0) neg -= nums[end];

            if (sum >= k) {
                tuple<int, int, int> last_valid;

                res = min(res, end-start+1);

                while (start < end && (sum - nums[start] + neg) >= k) {
                    if (sum >= k) last_valid = {start, sum, neg};

                    sum -= nums[start];
                    if (nums[start] < 0) neg += nums[start];
                    start++;

                    if (sum >= k) {
                        res = min(res, end-start+1);
                    }
                }

                if (sum < k) {
                    start = get<0>(last_valid);
                    sum = get<1>(last_valid);
                    neg = get<2>(last_valid);
                }

            }
        }

        return res == 1e9 ? -1 : res;
    }
};
