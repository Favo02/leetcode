class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        int R = matrix.size();
        int C = matrix[0].size();

        bool frow = false;
        bool fcol = false;

        for (int i = 0; i < C; i++) {
            if (matrix[0][i] == 0) frow = true;
        }

        for (int i = 0; i < R; i++) {
            if (matrix[i][0] == 0) fcol = true;
        }

        for (int row = 1; row < R; row++) {
            for (int col = 1; col < C; col++) {
                if (matrix[row][col] == 0) {
                    matrix[0][col] = 0;
                    matrix[row][0] = 0;
                }
            }
        }

        for (int row = 1; row < R; row++) {
            for (int col = 1; col < C; col++) {
                if (matrix[row][0] == 0 || matrix[0][col] == 0) {
                    matrix[row][col] = 0;
                }
            }
        }

        if (frow) {
            for (int i = 0; i < C; i++) {
                matrix[0][i] = 0;
            }
        }

        if (fcol) {
            for (int i = 0; i < R; i++) {
                matrix[i][0] = 0;
            }
        }
    }
};
