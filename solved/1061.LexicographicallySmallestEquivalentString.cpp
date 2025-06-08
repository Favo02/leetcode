class Solution {
public:
    string smallestEquivalentString(string s1, string s2, string baseStr) {

        vector<unordered_set<char>> eq(26);
        int S = s1.length();
        for (int i = 0; i < S; i++) {
            eq[s1[i] - 'a'].insert(s2[i] - 'a');
            eq[s2[i] - 'a'].insert(s1[i] - 'a');
        }

        vector<char> lexmin(26, '-');
        for (int i = 0; i < 26; i++) {
            if (lexmin[i] != '-') continue;

            char minn = 'a' + i;

            deque<int> open;
            open.push_back(i);

            unordered_set<int> seen;
            seen.insert(i);

            while (!open.empty()) {
                int cur = open.back();
                open.pop_back();
                minn = min(minn, char(cur+'a'));

                for (auto adj : eq[cur]) {
                    if (seen.count(adj)) continue;
                    seen.insert(adj);
                    open.push_back(adj);
                }
            }

            for (auto s : seen) {
                lexmin[s] = minn;
            }
        }

        string res = "";
        for (auto bs : baseStr) {
            res += (lexmin[bs - 'a']);
        }

        return res;
    }
};
