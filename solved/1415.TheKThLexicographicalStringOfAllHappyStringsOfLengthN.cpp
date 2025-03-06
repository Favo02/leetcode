#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<vector<string>>> dp;
    // n * 3 vectors of string

    string getHappyString(int n, int k) {

        dp = vector<vector<vector<string>>>(n+1, vector<vector<string>>(3));

        auto strings = happyStrings(n, 'z');

        if (strings.size() < k) return "";
        return strings[k-1];
    }

    vector<string> happyStrings(int n, char last) {
        if (n == 0) return {""};

        if (last != 'z' && dp[n][last - 'a'].size() > 0) {
            return dp[n][last - 'a'];
        }

        vector<string> res;
        for (auto c : {'a', 'b', 'c'}) {
            if (c == last) continue;
            for (auto rec : happyStrings(n-1, c)) {
                res.push_back(c + rec);
            }
        }

        if (last != 'z') {
            dp[n][last - 'a'] = res;
        }
        return res;
    }
};
