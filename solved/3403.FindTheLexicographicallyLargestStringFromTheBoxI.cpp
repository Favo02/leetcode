class Solution {
public:
    string answerString(string word, int numFriends) {
        if (numFriends == 1) return word;

        int S = word.length();
        int best = 0;
        for (int i = 1; i < S; i++) {
            if (word[i] > word[best]) {
                best = i;
            } else if (word[i] == word[best]) {
                int ii = 1;
                while (true) {
                    if (best + ii >= i) break;
                    if (i + ii >= S) break;
                    if (word[i+ii] > word[best+ii]) {
                        best = i;
                        break;
                    }
                    if (word[i+ii] < word[best+ii]) {
                        break;
                    }
                    ii++;
                }
            }
        }
        return word.substr(best, S - best - max(0, numFriends-1-best));
    }
};
