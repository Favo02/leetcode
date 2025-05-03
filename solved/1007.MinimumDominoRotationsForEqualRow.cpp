class Solution {
    public:
        int minDominoRotations(vector<int>& tops, vector<int>& bottoms) {

            vector<int> count(6);

            int N = tops.size();
            for (int i = 0; i < N; i++) {
                count[tops[i]-1]++;
                if (bottoms[i] != tops[i]) {
                    count[bottoms[i]-1]++;
                }
            }

            int res = 1e9;

            for (int i = 0; i < 6; i++) {
                if (count[i] < N) continue;

                int top = 0, bottom = 0;
                for (int ii = 0; ii < N; ii++) {
                    if (tops[ii] != i+1) top++;
                    if (bottoms[ii] != i+1) bottom++;
                }

                res = min(res, top);
                res = min(res, bottom);
            }

            return res == 1e9 ? -1 : res;
        }
    };
