#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int numberOfAlternatingGroups(vector<int>& colors, int k) {
        int N = colors.size();
        int res = 0;

        int start = 0;
        bool last = colors[0] == 1;

        for (int i = 1; i < N+k-1; i++) {
            if ((colors[i % N] == 1) == last) start = i;
            if (i - start + 1 >= k) res++;
            last = colors[i % N] == 1;
        }

        return res;
    }
};
