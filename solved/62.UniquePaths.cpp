#include <iostream>
#include <vector>
#include <map>
using namespace std;

map<pair<int,int>, int> memoization;

int bfs(int m, int n, int x, int y) {  
  if (memoization.find(make_pair(x,y)) != memoization.end()) {
    return memoization[make_pair(x,y)];
  }

  if (x == m-1 && y == n-1) {
    memoization.insert(make_pair(make_pair(x,y), 1));
    return 1;
  }

  int count = 0;
  if (x < m-1) {
    count += bfs(m, n, x+1, y);
  }
  if (y < n-1) {
    count += bfs(m, n, x, y+1);
  }

  memoization.insert(make_pair(make_pair(x,y), count));
  return count;
}

class Solution {
public:
  int uniquePaths(int m, int n) {
    memoization.clear();
    return bfs(m, n, 0, 0);
  }
};

int main() {
  Solution s;
  cout << s.uniquePaths(3,7) << endl;
  cout << s.uniquePaths(3,2) << endl;
  return 0;
}
