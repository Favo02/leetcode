#include <bits/stdc++.h>
using namespace std;

struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode() : val(0), left(nullptr), right(nullptr) {}
  TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
  TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
  int maxAncestorDiff(TreeNode *root) {
    return dfs(root, root->val, root->val);
  }

private:
  int dfs(TreeNode *start, int maxx, int minn) {
    if (!start)
      return abs(maxx - minn);
    maxx = max(maxx, start->val);
    minn = min(minn, start->val);
    return max(
      dfs(start->left, maxx, minn),
      dfs(start->right, maxx, minn)
    );
  }
};
