#include <vector>
#include <queue>
#include <iostream>
using namespace std;

TreeNode* deepCloneTree(TreeNode* root) {
  if (root == nullptr) return nullptr;
  TreeNode* newRoot = new TreeNode(root->val);
  newRoot->left = deepCloneTree(root->left);
  newRoot->right = deepCloneTree(root->right);
  return newRoot;
}

bool compare(TreeNode* a, TreeNode* b) {
  if (a == nullptr && b == nullptr) return true;
  if (a == nullptr || b == nullptr) return false;
  return compare(a->left, b->left) && compare(a->right, b->right);
}

vector<TreeNode*> genTrees(int n) {
  if (n == 1) {
    return { new TreeNode(0) };
  }

  vector<TreeNode*> trees;
  trees.push_back(new TreeNode(0));

  for ( ; n > 1; n-=2) {
    vector<TreeNode*> newTrees;
    for (auto tree : trees) {

      queue<TreeNode*> searchQ;
      searchQ.push(tree);

      queue<TreeNode*> insertQ;

      while (!searchQ.empty()) {
        TreeNode* node = searchQ.front();
        searchQ.pop();

        if (node->left != nullptr) {
          searchQ.push(node->left);
          searchQ.push(node->right);
        }
        else {
          insertQ.push(node);
        }
      }

      while (!insertQ.empty()) {
        TreeNode* node = insertQ.front();
        insertQ.pop();

        node->left = new TreeNode(0);
        node->right = new TreeNode(0);

        TreeNode* cloneTree = deepCloneTree(tree);

        bool found = false;
        for (auto nt : newTrees) {
          if (compare(nt, cloneTree)) {
            found = true;
            break;
          }
        }
        
        if (!found)
          newTrees.push_back(cloneTree);

        node->left = nullptr;
        node->right = nullptr;
      }
    }
    trees = newTrees;
  }
  return vector(trees.begin(), trees.end());
}

class Solution {
public:
  vector<TreeNode*> allPossibleFBT(int n) {
    if (n % 2 == 0) return {};

    return genTrees(n);
  }
};

struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode() : val(0), left(nullptr), right(nullptr) {}
  TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
  TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};
