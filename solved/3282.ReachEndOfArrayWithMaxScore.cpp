#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    long long findMaximumScore(vector<int>& nums) {
        int N = nums.size();

        long long res = 0;
        int cur = 0;
        for (int i = 1; i < N; i++) {
            if (nums[i] > nums[cur]) {
                res += (i - cur) * (long long)(nums[cur]);
                cur = i;
            }
        }
        res += (N-1 - cur) * (long long)(nums[cur]);
        return res;
    }
};
