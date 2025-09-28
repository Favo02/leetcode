class Solution {
private:
    int get(vector<vector<int>> &triangle, int row, int col) {
        if (!(0 <= row && row < triangle.size()))
            return 1e9;
        if (!(0 <= col && col < triangle[row].size()))
            return 1e9;
        return triangle[row][col];
    }

public:
    int minimumTotal(vector<vector<int>> &triangle) {
        for (int row = 1; row < triangle.size(); row++) {
            for (int col = 0; col < triangle[row].size(); col++) {
                triangle[row][col] = triangle[row][col] + min(get(triangle, row - 1, col - 1), get(triangle, row - 1, col));
            }
        }

        int res = 1e9;
        for (auto c : triangle[triangle.size() - 1])
            res = min(res, c);

        return res;
    }
};
