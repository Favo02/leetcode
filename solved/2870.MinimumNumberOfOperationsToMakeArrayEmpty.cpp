class Solution {
public:
  int minOperations(vector<int>& nums) {
    map<int,int> counter;
    for (auto n : nums) counter[n]++;

    int res = 0;
    for (auto [n, v] : counter) {
      if (v == 1) return -1;

      if (v % 3 == 0) res += v / 3;
      else res += v / 3 + 1;
      cout << n << ": " << counter[n] << "->" << res << "\n" ;
    }

    return res;
  }
};
