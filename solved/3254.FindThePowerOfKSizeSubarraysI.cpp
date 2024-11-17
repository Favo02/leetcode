#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> resultsArray(vector<int>& nums, int k) {

        vector<int> stack, res;

        for (int i = 0; i < nums.size(); i++) {
            auto n = nums[i];

            if (!stack.empty() && stack.back() != n-1) stack.clear();
            stack.push_back(n);

            if (i >= k-1) res.push_back(stack.size() >= k ? n : -1);
        }

        return res;
    }
};
