#define ll long long

class Solution {
public:
    unordered_set<string> results;

    vector<string> perms(string from) {
        vector<string> res;
        if (from.length() == 1) {
            res.push_back(from);
            results.insert(from);
            return res;
        }

        for (int i = 0; i < from.length(); i++) {
            for (auto s : perms(from.substr(0, i) + from.substr(i+1, 10))) {
                res.push_back(from.substr(i, 1) + s);
                results.insert(from.substr(i, 1) + s);
            }
        }

        return res;
    }

    int numTilePossibilities(string tiles) {
        perms(tiles);
        return results.size();
    }
};
