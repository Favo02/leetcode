class Solution {
public:
    int numEquivDominoPairs(vector<vector<int>>& dominoes) {
        vector<vector<int>> seen(9, vector<int>(9));

        int res = 0;
        for (auto d : dominoes) {
            if (d[1] < d[0]) {
                swap(d[1], d[0]);
            }
            d[0]--;
            d[1]--;
            res += seen[d[0]][d[1]];
            seen[d[0]][d[1]]++;
        }

        return res;
    }
};
