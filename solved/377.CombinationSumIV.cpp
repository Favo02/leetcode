#include <iostream>
#include <vector>
#include <map>
using namespace std;

map<int, int> memoization;

int recursion(vector<int>& nums, int target) {
  if (memoization.find(target) != memoization.end()) {
    return memoization[target];
  }

  if (target == 0) {
    memoization[target] = 1;
    return 1;
  }

  int res = 0;
  for (int i = 0; i < nums.size(); i++) {
    if (target >= nums[i]) {
      res += recursion(nums, target - nums[i]);
    }
  }

  memoization[target] = res;
  return res;
}

class Solution {
public:
  int combinationSum4(vector<int>& nums, int target) {
    memoization.clear();
    int res = recursion(nums, target);
    cout << res << endl;
    return res;
  }
};

int main() {
  Solution s;
  vector<int> nums = {1, 2, 3};
  s.combinationSum4(nums, 32);
}
