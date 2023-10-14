#include <vector>
#include <iostream>
#include <map>
#include <string>
using namespace std;

int hammingDist(string s1, string s2) {
  int count = 0;
  for (int i = 0; i < s1.length(); i++) {
    if (s1[i] != s2[i]) {
      count++;
    }
  }
  return count;
}

map<int, vector<string>> memoization;

vector<string> solve(int start, vector<string>& words, vector<int>& groups) {
  if (memoization.find(start) != memoization.end()) {
    return memoization[start];
  }

  vector<string> res;

  for (int i = start+1; i < words.size(); i++) {
    if (groups[start] != groups[i]) {
      if ((words[start].length() == words[i].length()) && (hammingDist(words[start], words[i]) == 1)) {
        vector<string> next = solve(i, words, groups);
        if (next.size() > res.size()) {
          res = next;
        }
      }
    }
  }

  res.insert(res.begin() + 0, words[start]);
  memoization.insert(make_pair(start, res));
  return res;
}

class Solution {
public:
  vector<string> getWordsInLongestSubsequence(int n, vector<string>& words, vector<int>& groups) {
    memoization.clear();
    vector<string> res;
    for (int i = 0; i < n; i++) {
      vector<string> next = solve(i, words, groups);
      if (next.size() > res.size()) {
        res = next;
      }
    }
    
    for (int i = 0; i < res.size(); i++) 
      cout << res[i] << " ";
    cout << "\n";

    return res;
  }  
};

int main() {
  Solution s;
  vector<string> v1;
  vector<int> v2;

  // bab, dab
  v1 = {"bab","dab","cab"};
  v2 = {1,2,2};
  s.getWordsInLongestSubsequence(3, v1, v2);

  // a b c d
  v1 = {"a","b","c","d"};
  v2 = {1,2,3,4};
  s.getWordsInLongestSubsequence(4, v1, v2);

  // aaa ada
  v1 = {"bdb","aaa","ada"};
  v2 = {2,1,3};
  s.getWordsInLongestSubsequence(3, v1, v2);

  // dc dd da
  v1 = {"bad","dc","bc","ccd","dd","da","cad","dba","aba"};
  v2 = {9,7,1,2,6,8,3,7,2};
  s.getWordsInLongestSubsequence(9, v1, v2);
}
