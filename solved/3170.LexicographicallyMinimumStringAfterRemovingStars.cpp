class Solution {
public:
    string clearStars(string s) {
        int S = s.length();
        vector<vector<int>> chr(26);
        for (int i = 0; i < S; i++) {
            if (s[i] != '*') {
                chr[s[i] - 'a'].push_back(i);
                continue;
            }

            for (int ii = 0; ii < 26; ii++) {
                if (chr[ii].size() > 0) {
                    s[chr[ii].back()] = '*';
                    chr[ii].pop_back();
                    break;
                }
            }
        }

        string res;
        for (int i = 0; i < S; i++) {
            if (s[i] != '*') {
                res += s[i];
            }
        }
        return res;
    }
};
