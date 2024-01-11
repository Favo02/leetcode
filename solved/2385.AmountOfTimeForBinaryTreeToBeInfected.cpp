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
  int amountOfTime(TreeNode *root, int start) {
    auto graph = treeToGraph(root);
    auto time = bfs(graph, start);
    cout << time << "\n";
    return time;
  }

private:
  map<int, vector<int>> treeToGraph(TreeNode *root) {
    map<int, vector<int>> graph;
    queue<TreeNode *> q;
    q.push(root);
    while (!q.empty()) {
      TreeNode *cur = q.front();
      q.pop();

      int v = cur->val;
      if (cur->left) {
        q.push(cur->left);
        int c = cur->left->val;
        graph[v].push_back(c);
        graph[c].push_back(v);
      }
      if (cur->right) {
        q.push(cur->right);
        int c = cur->right->val;
        graph[v].push_back(c);
        graph[c].push_back(v);
      }
    }
    return graph;
  }

  int bfs(map<int, vector<int>> graph, int start) {
    int res = 0;
    set<int> seen;
    queue<pair<int, int>> q;
    q.push({start, 0});
    while (!q.empty()) {
      auto [cur, dist] = q.front();
      q.pop();
      if (seen.find(cur) != seen.end())
        continue;
      seen.insert(cur);
      res = max(dist, res);
      for (auto adj : graph[cur])
        q.push({adj, dist + 1});
    }
    return res;
  }
};
