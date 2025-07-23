class Solution {
public:
    string makeFancyString(string s) {
        string res = "";
        for (int i = 0; i < s.size(); i++) {
            if (res.size() >= 2 && res[res.size()-1] == s[i] && res[res.size()-2] == s[i]) continue;
            res += s[i];
        }
        return res;
    }
};
