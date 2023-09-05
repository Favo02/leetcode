#include <map>
#include <iostream>
using namespace std;

class Solution {
public:
  Node* copyRandomList(Node* head) {
    if (!head) return nullptr;

    Node* cur = head;

    map<Node*, Node*> randoms;

    Node* newList = new Node(head->val);
    Node* res = newList;

    // clone list
    while (cur != nullptr) {
      cout << cur->val << endl;

      if (cur->next != nullptr) {
        newList->next = new Node(cur->next->val);
      }

      // save (old pointer -> new pointer)
      randoms[cur] = newList;

      cur = cur->next;
      newList = newList->next;
    }

    // randoms
    cur = head;
    newList = res;
    while (cur != nullptr) {
      newList->random = randoms[cur->random];

      cur = cur->next;
      newList = newList->next;
    }

    return res;
  }
};

class Node {
public:
  int val;
  Node* next;
  Node* random;
  
  Node(int _val) {
      val = _val;
      next = nullptr;
      random = nullptr;
  }
};
