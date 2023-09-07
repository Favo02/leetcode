#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
  ListNode* reverseBetween(ListNode* head, int left, int right) {
    // convert to 0-based index
    left--;

    ListNode* cur = head;
    vector<ListNode*> pointers;

    for (int i = 0; cur != nullptr; i++) {
      pointers.push_back(cur);
      cur = cur->next;
      pointers[i]->next = nullptr;
      // cout << pointers[i] << " " << pointers[i]->val << " " << pointers[i]->next << endl;
    }

    int size = (right-left) / 2;

    for (int i = left, j = right-1; i < right-size; i++, j--) {
      // cout << "swap" << i << "-" << j << endl;
      swap(pointers[i], pointers[j]);
    }

    head = pointers[0];
    cur = head;
    for (int i = 1; i < pointers.size(); i++) {
      cur->next = pointers[i];
      cur = cur->next;
    }

    return head;
  }
};

struct ListNode {
  int val;
  ListNode *next;
  ListNode() : val(0), next(nullptr) {}
  ListNode(int x) : val(x), next(nullptr) {}
  ListNode(int x, ListNode *next) : val(x), next(next) {}
};
