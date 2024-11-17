#include <bits/stdc++.h>
using namespace std;

class Solution {
    bool valid(int n, vector<int>& quantities, int div) {
        int nn = 0;
        for (auto q : quantities) {
            nn += ceil(float(q) / float(div));
        }
        return nn <= n;
    }

public:
    int minimizedMaximum(int n, vector<int>& quantities) {

        int high = *max_element(quantities.begin(), quantities.end());
        if (n == quantities.size()) {
            return high;
        }

        int low = 1;
        while (low < high) {
            int mid = (low+high) / 2;

            if (valid(n, quantities, mid)) {
                high = mid;
            } else {
                low = mid+1;
            }
        }

        return low;
    }
};
