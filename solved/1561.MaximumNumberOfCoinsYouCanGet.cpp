#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
  int maxCoins(vector<int>& piles) {
    sort(piles.begin(), piles.end());
    int res = 0;
    int minI = 0;
    int maxI = piles.size() -1;
    while (minI < maxI) {
      maxI--;
      res += piles[maxI--];
      minI++;
    }
    cout << res;
    return res;
  }
};
