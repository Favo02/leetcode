class Solution {
private:
    vector<string> split(string s, string delimiter) {
        vector<string> tokens;
        size_t pos = 0;
        string token;
        while ((pos = s.find(delimiter)) != string::npos) {
            token = s.substr(0, pos);
            tokens.push_back(token);
            s.erase(0, pos + delimiter.length());
        }
        tokens.push_back(s);

        return tokens;
    }

public:
    int compareVersion(string version1, string version2) {

        auto v1 = split(version1, ".");
        auto v2 = split(version2, ".");

        for (int i = 0; i < max(v1.size(), v2.size()); i++) {
            int v11 = 0;
            int v22 = 0;
            if (i < v1.size()) v11 = stoi(v1[i]);
            if (i < v2.size()) v22 = stoi(v2[i]);

            if (v11 > v22) return 1;
            if (v11 < v22) return -1;
        }

        return 0;
    }
};
