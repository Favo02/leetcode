#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> pivotArray(vector<int>& nums, int pivot) {

        int pre = 0, piv = 0;
        for (auto n : nums) {
            if (n < pivot) pre++;
            if (n == pivot) piv++;
        }

        vector<int> res(nums.size());

        int ipre = 0, ipiv = pre, ipost = pre + piv;
        for (auto n : nums) {
            if (n < pivot) res[ipre++] = n;
            if (n == pivot) res[ipiv++] = n;
            if (n > pivot) res[ipost++] = n;
        }

        return res;
    }
};
