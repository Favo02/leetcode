#include <iostream>
#include <bitset>
#include <vector>
using namespace std;

int countOnes(unsigned int n) {
  int count = 0;
  while (n > 0) {
    count += (n % 2 == 0) ? 0 : 1;
    n /= 2;
  }
  return count;
}

class Solution {
public:
  vector<int> countBits(int n) {
    vector<int> res;

    for (int i = 0; i <= n; i++) {
      res.push_back(countOnes(i));
    }

    return res;
  }
};

int main() {
  Solution s;
  vector<int> res = s.countBits(5);
  for (int i = 0; i < res.size(); i++) {
    cout << res[i] << " ";
  }
  cout << endl;
  return 0;
}
