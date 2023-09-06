#include <vector> 
#include <iostream> 
using namespace std;

class Solution {
public:
  vector<ListNode*> splitListToParts(ListNode* head, int k) {

    int len = 0;
    for (ListNode* node = head; node != nullptr; node = node->next) {
      len++;
    }

    int elems = len / k; 
    int rem = len % k;

    vector<ListNode*> res;

    for (int listInd = 0; listInd < k; listInd++) {

      int listLen = (listInd < rem) ? (elems+1) : (elems);
      ListNode* newList = nullptr;
      ListNode* last = nullptr;

      for (int size = 0; size < listLen; size++) {
        if (size == 0) {
          newList = head;
          last = head;
        }
        else {
          last->next = head;
          last = head;
        }
        // save next node
        head = head->next;
        // but cut the pointer to the list just generated
        last->next = nullptr;
      }

      res.push_back(newList);
    }

    return res;
  }
};

struct ListNode {
  int val;
  ListNode *next;
  ListNode() : val(0), next(nullptr) {}
  ListNode(int x) : val(x), next(nullptr) {}
  ListNode(int x, ListNode *next) : val(x), next(next) {}
};
