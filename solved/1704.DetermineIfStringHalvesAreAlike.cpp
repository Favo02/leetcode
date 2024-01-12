#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
  bool halvesAreAlike(string s) {
    int ac = 0;
    int bc = 0;
    string vowels = "aeiouAEIOU";
    for (size_t i = 0; i < s.size(); i++) {
      if (vowels.find(s[i]) != -1)
        if (i < s.size() / 2)
          ac++;
        else
          bc++;
    }
    return ac == bc;
  }
};
