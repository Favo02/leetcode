#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;

map<string, int> memoization;

int countRealSize(string s) {
  int count = 0;
  for (int i = 0; i < s.size(); i++) {
    if (s[i] != '-')
      count++;
  }
  return count;
}

pair<vector<string>, vector<string>> splitDictionary(vector<string>& dictionary) {
  vector<string> oneChar;
  vector<string> moreChar;

  copy_if(dictionary.begin(), dictionary.end(), back_inserter(oneChar), [](string i){return i.size() == 1;} );
  copy_if(dictionary.begin(), dictionary.end(), back_inserter(moreChar), [](string i){return i.size() > 1;} );

  return make_pair(oneChar, moreChar);
}

int recMinExtraChar(string s, vector<string>& dictionaryOne, vector<string>& dictionaryMore) {
  if (memoization.find(s) != memoization.end()) {
    return memoization[s];
  }

  if (countRealSize(s) == 0) {
    memoization.insert(make_pair(s, 0));
    return 0;
  }

  string oldS = s;

  int min = 1000000;
  for (int i = 0; i < dictionaryMore.size(); i++) {

    int pos = s.find(dictionaryMore[i]);

    if (pos != string::npos) {   
      string newS = s;
      newS.replace(pos, dictionaryMore[i].size(), 1, '-');

      int res = recMinExtraChar(newS, dictionaryOne, dictionaryMore);
      if (res < min)
        min = res;
    }
  }

  for (int i = 0; i < dictionaryOne.size(); i++) {
    if (dictionaryOne[i].size() > 1) 
      continue;

    int pos = s.find(dictionaryOne[i]);
    while (pos != string::npos) {   
      s.replace(pos, 1, 1, '-');
      
      int start = pos + dictionaryOne[i].size();
      pos = s.find(dictionaryOne[i], start);
    }

  }

  int res = (min != 1000000) ? min : countRealSize(s);
  memoization.insert(make_pair(oldS, res));
  return res;
}

class Solution {
public:
  int minExtraChar(string s, vector<string>& dictionary) {
    memoization.clear();

    pair<vector<string>, vector<string>> p = splitDictionary(dictionary);
    int res = recMinExtraChar(s, p.first, p.second);
    cout << res << endl;
    return res;
  }
};


int main() {
  Solution s;
  vector<string> v;

  // 1
  v = {"leet","code","leetcode"};
  s.minExtraChar("leetscode", v);

  // 3
  v = {"hello","world"};
  s.minExtraChar("sayhelloworld", v);

  // 1
  v = {"rs","j","h","g","fy","l","fc","s","zf","i","k","x","gl","qr","qj","b","m","cm","pe","y","ei","wg","e","c","ll","u","lb","kc","r","gs","p","ga","pq","o","wq","mp","ms","vp","kg","cu"};
  s.minExtraChar("eglglxa", v);

  // 2
  v = {"m","its","imaby","pa","ijmnvj","k","mhka","n","y","nc","wq","p","mjqqa","ht","dfoa","yqa","kk","pixq","ixsdln","rh","dwl","dbgnxa","kmpfz","nhxjm","wg","wky","oct","og","uhin","zxb","qz","tpf","hlrc","j","l","tew","xbn","a","uzypt","uvln","mchay","onnbi","hlytk","pjoqlo","dxsjr","u","uj"};
  s.minExtraChar("octncmdbgnxapjoqlofuzypthlytkmchayflwky", v);

  // 5
  v = {"lkycpd","emj","fj","syuqcg","hrn","c","j","csgdel","o","xhfubv","lo","yoommo","zmef","ual","kolx","qgyrwj","im","jgs","f","knhihb","qbx","qg","uhft","wurdt"};
  s.minExtraChar("xtcsgdelqbxxhfubvorjfsyuqcgsyuqcgplf", v);

  // 9
  v = {"yv","bmab","hv","bnsll","mra","jjqf","g","aiyzi","ip","pfctr","flr","ybbcl","biu","ke","lpl","iak","pirua","ilhqd","zdhx","fux","xaw","pdfvt","xf","t","wq","r","cgmud","aokas","xv","jf","cyys","wcaz","rvegf","ysg","xo","uwb","lw","okgk","vbmi","v","mvo","fxyx","ad","e"};
  s.minExtraChar("kevlplxozaizdhxoimmraiakbak", v);

  // 10
  v = {"mhxxn"};
  s.minExtraChar("omawwmhxxnmhxxnnmhxxnqfvd", v);

  // 10
  v = {"nrwks","t","mcgjko","xm","vac","ypqdr","zwlghw","gz","xbsmr","hhkkv","qviu","yvvobml","cfk","fxu","pm","nwobfce","eu","y","krzbg","xoktzxa","doftmgc","qpcpd","oj","bl","kylslpr","cpzcvlc","ogscaz","l","nztlq","ai","o","wdhlanl","ot","hqe"};
  s.minExtraChar("jqnrwkslbhhkkvveotpfaidoftmgcojcpzcvlctsqyvvobmlzo", v);

  // 10
  v = {"xvud","orcl","wkni","fxalw","rq","cskr","cph","t","czb","cuwnk","fg","dstl","wpw","iyx","fwyq","c","lkxw","phw","sjilo","of","vf","j","ltpug","opu","do","a","lw","as","d","pz","xsa","npqg","xebx","nh","ddo","pcxhr","xkuyw","zes"};
  s.minExtraChar("vfkjxebxgmelwcskrlevfmpwknifglpzlwq", v);
}

