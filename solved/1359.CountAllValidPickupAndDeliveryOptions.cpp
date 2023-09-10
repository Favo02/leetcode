#include <iostream>
#include <vector>
#include <map>
using namespace std;

map<pair<int, int>, long> memoization;

long recursion(int toPickup, int toDeliver) {
  if (toPickup + toDeliver == 0) {
    return 1;
  }

  if (memoization.find({toPickup, toDeliver}) != memoization.end()) {
    return memoization[{toPickup, toDeliver}];
  }

  long res = 0;

  // to pickup
  if (toPickup > 0) {
    res += toPickup * recursion(toPickup-1, toDeliver+1);
  }
  
  // to deliver
  if (toDeliver > 0) {
    res += toDeliver * recursion(toPickup, toDeliver-1);
  }

  res %= 1000000007;
  memoization[{toPickup, toDeliver}] = res;
  return res;
}

class Solution {
public:
  int countOrders(int n) {
    memoization[{0,0}] = 1;
    long res = recursion(n, 0);
    cout << res << endl;
    return res;
  }
};

int main() {
  Solution s;
  
  s.countOrders(1); // 1
  s.countOrders(2); // 6
  s.countOrders(3); // 90
  s.countOrders(4); // 2520
  s.countOrders(5);
  s.countOrders(6);
  s.countOrders(7);
  s.countOrders(8);
  s.countOrders(9);
  s.countOrders(10);
  s.countOrders(18);
  s.countOrders(488);
  s.countOrders(492);
  s.countOrders(500);
}
