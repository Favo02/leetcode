#include <bits/stdc++.h>
using namespace std;

struct ListNode {
  int val;
  ListNode *next;
  ListNode() : val(0), next(nullptr) {}
  ListNode(int x) : val(x), next(nullptr) {}
  ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
  ListNode* mergeKLists(vector<ListNode*>& lists) {
    ListNode* head = new ListNode();
    ListNode* cur = head;

    bool all_empty = false;
    while (!all_empty) {
      all_empty = true;

      int minv = 10e4 + 1;
      for (auto hd : lists) {
        if (hd) {
          all_empty = false;
          minv = min(minv, hd->val);
        }
      }

      for (size_t i = 0; i < lists.size(); i++) {
        auto hd = lists[i];

        while (hd && hd->val == minv) {
          cur->next = new ListNode();
          cur = cur->next;
          cur->val = minv;

          hd = hd->next;
        }

        lists[i] = hd;
      }
    }

    cur = head;
    while ((cur = cur->next)) {
      cout << cur->val << " ";
    }
    cout << "\n";

    return head->next;
  }
};

int main(int argc, char const *argv[]) {
  Solution s;
  vector<ListNode*> v = {new ListNode(4, new ListNode(5, new ListNode(6))), new ListNode(10)};
  s.mergeKLists(v);
  return 0;
}
