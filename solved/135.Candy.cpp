class Solution {
public:
    int candy(vector<int>& ratings) {
        int N = ratings.size();
        vector<int> res(N, 1);

        for (int i = 1; i < N; i++) {
            if (ratings[i] > ratings[i-1]) {
                res[i] = res[i-1]+1;
            }
        }

        int ress = 0;
        for (int i = N-1; i > 0; i--) {
            if (ratings[i] < ratings[i-1] && !(res[i] < res[i-1])) {
                res[i-1] = res[i]+1;
            }
        }

        return accumulate(res.begin(), res.end(), 0);
    }
};
