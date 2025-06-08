#include <bits/stdc++.h>

using namespace std;

#pragma GCC optimize("Ofast,unroll-loops")
#pragma GCC target("avx,avx2,fma")

class Solution {
private:
    vector<int> RES;
    int N;

    void dfs(int prefix) {
        for (int i = 0; i < 10; i++) {
            if (prefix*10 + i > N) return;
            RES.push_back(prefix*10 + i);
            dfs(prefix*10 + i);
        }
    }

public:
    vector<int> lexicalOrder(int n) {
        N = n;
        for (int i = 1; i < 10; i++) {
            if (i > N) break;
            RES.push_back(i);
            dfs(i);
        }
        return RES;
    }
};

int main() {
    Solution s;
    auto res = s.lexicalOrder(13);
    for (auto r : res) {
        cout << r << " ";
    }
    cout << endl;
}
