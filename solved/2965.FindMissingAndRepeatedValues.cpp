class Solution {
public:
    vector<int> findMissingAndRepeatedValues(vector<vector<int>>& grid) {
        vector<int> res;
        int n = grid.size();
        vector<bool> found(n*n);
        for (auto row : grid) {
            for (auto col : row) {
                if (found[col-1])
                    res.push_back(col);
                found[col-1] = true;
            }
        }

        for (int i = 0; i < n*n; i++)
            if (!found[i])
                res.push_back(i+1);

        return res;
    }
};
