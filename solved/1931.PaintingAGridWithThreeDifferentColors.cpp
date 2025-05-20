#define MOD 1000000007

class Solution {
private:
    int biga;
    int bigb;

    vector<int> combinations(vector<int> cur, int rep) {
        if (rep <= 0) return cur;

        vector<int> neww;

        for (int i = 0; i < cur.size(); i++) {
            for (int num = 0; num <= 2; num++) {
                neww.push_back(cur[i]*10 + num);
            }
        }

        return combinations(neww, rep-1);
    }

    bool valid(int m, int num) {
        num += biga;

        int last = num % 10;
        num /= 10;
        while (num > 0) {
            if (num % 10 == last) return false;
            last = num % 10;
            num /= 10;
        }
        return true;
    }

    bool compatible(int m, int a, int b) {
        a += biga;
        b += bigb;

        while (a > 0 || b > 0) {
            if (a % 10 == b % 10) {
                return false;
            }
            a /= 10;
            b /= 10;
        }
        return true;
    }

public:
    int colorTheGrid(int m, int n) {
        biga = pow(10, m) * 7;
        bigb = pow(10, m) * 9;

        vector<int> combs;

        for (int v : combinations({0, 1, 2}, m-1)) {
            if (valid(m, v)) {
                combs.push_back(v);
            }
        }

        int C = combs.size();
        vector<int> dp(C, 1);

        for (int i = 1; i < n; i++) {

            vector<int> newdp(C);

            for (int old = 0; old < C; old++) {
                for (int neww = 0; neww < C; neww++) {
                    if (compatible(m, combs[old], combs[neww])) {
                        newdp[neww] = (newdp[neww] + dp[old]) % MOD;
                    }
                }
            }

            dp = newdp;
        }

        int res = 0;
        for (auto d : dp) res = (res + d) % MOD;
        return res;
    }
};
