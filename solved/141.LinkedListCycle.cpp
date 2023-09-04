#include <map>
#include <iostream>
#include <algorithm>
using namespace std;

class Solution {
public:
  bool hasCycle(ListNode *head) {
    map<ListNode*, bool> found;

    while (head != nullptr) {
      if (found[head]) {
        return true;
      }

      found[head] = true;

      head = head->next;
    }
    return false;
  }
};

struct ListNode {
  int val;
  ListNode *next;
  ListNode(int x) : val(x), next(nullptr) {}
};
