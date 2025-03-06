#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool checkPowersOfThree(int n) {

        vector<int> p;
        for (int i = 0; true; i++) {
            p.push_back(pow(3, i));
            if (*p.rbegin() >= n) break;
        }

        reverse(p.begin(), p.end());

        int summ = 0;
        for (auto pp : p) {
            if (summ + pp <= n) summ += pp;
            if (summ == n) return true;
        }
        return false;
    }
};
