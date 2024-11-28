#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    long long maximumSubarraySum(vector<int>& nums, int k) {

        long long sum = 0;
        unordered_map<int, int> in_window;

        long long res = 0;
        for (int i = 0; i < nums.size(); i++) {
            if (i >= k) {
                sum -= nums[i-k];
                in_window[nums[i-k]]--;
                if (in_window[nums[i-k]] == 0) {
                    in_window.erase(nums[i-k]);
                }
            }
            sum += nums[i];
            in_window[nums[i]]++;

            if (in_window.size() == k) {
                res = max(res, sum);
            }
        }

        return res;
    }
};
