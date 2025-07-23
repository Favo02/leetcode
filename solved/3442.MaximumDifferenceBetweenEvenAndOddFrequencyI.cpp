class Solution {
public:
    int maxDifference(string s) {
        vector<int> freqs(26);
        for (auto ss : s) {
            freqs[ss - 'a']++;
        }
        int maxO = -1;
        int minE = 101;
        for (auto f : freqs) {
            if (f == 0) continue;
            if (f % 2 == 0) {
                minE = min(minE, f);
            } else {
                maxO = max(maxO, f);
            }
        }
        return maxO - minE;
    }
};
