#include <bits/stdc++.h>
using namespace std;
#define ll long long

class Solution {
public:
    long long getDescentPeriods(vector<int>& prices) {
        ll res = 0, cur = 1;
        for (int i = 1; i < prices.size(); i++) {
            if (prices[i] == prices[i-1]-1) cur++;
            else {
                res += cur*(cur+1)/2;
                cur = 1;
            }
        }
        res += cur*(cur+1)/2;
        return res;
    }
};
