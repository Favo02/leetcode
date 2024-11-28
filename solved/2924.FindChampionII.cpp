#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int findChampion(int n, vector<vector<int>>& edges) {
        vector<bool> valid(n, true);

        for (auto ed : edges) {
            valid[ed[1]] = false;
        }

        int res = -1;
        for (int i = 0; i < n; i++) {
            if (valid[i] && res != -1) return -1;
            if (valid[i]) res = i;
        }
        return res;
    }
};
