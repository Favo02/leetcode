class Solution {
private:
    bool hamming(string a, string b) {
        if (a.length() != b.length()) return false;
        bool jolly = true;
        for (int i = 0; i < a.length(); i++) {
            if (a[i] != b[i]) {
                if (jolly) jolly = false;
                else return false;
            }
        }
        return true;
    }

public:
    vector<string> getWordsInLongestSubsequence(vector<string>& words, vector<int>& groups) {
        int N = words.size();

        vector<int> prev(N);
        vector<int> len(N);

        for (int i = 0; i < N; i++) {
            prev[i] = -1;
            len[i] = 1;

            for (int j = 0; j < i; j++) {
                if (len[j] < len[i]) continue;
                if (groups[j] == groups[i]) continue;
                if (!hamming(words[j], words[i])) continue;

                prev[i] = j;
                len[i] = len[j] + 1;
            }
        }

        int max = 0;
        for (int i = 0; i < N; i++) {
            if (len[i] > len[max]) {
                max = i;
            }
        }

        vector<string> res;
        while (max != -1) {
            res.push_back(words[max]);
            max = prev[max];
        }
        reverse(res.begin(), res.end());
        return res;
    }
};
