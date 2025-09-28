class Solution {
public:
    double largestTriangleArea(vector<vector<int>> &points) {
        float res = 0;
        int P = points.size();
        for (int i = 0; i < P; i++) {
            int x1 = points[i][0];
            int y1 = points[i][1];
            for (int ii = 0; ii < P; ii++) {
                int x2 = points[ii][0];
                int y2 = points[ii][1];
                for (int iii = 0; iii < P; iii++) {
                    int x3 = points[iii][0];
                    int y3 = points[iii][1];
                    res = max(res, abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0f);
                }
            }
        }
        return res;
    }
};
