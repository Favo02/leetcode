class Solution {
public:
    int punishmentNumber(int n) {
        int res = 0;
        for (int i = 1; i <= n; i++) {
            if (partition(i, i*i, 0)) res += i*i;
        }
        return res;
    }

    bool partition(int target, int n, int acc) {
        if (target == n + acc) return true;
        if (n == 0) return false;

        for (int i = 1; true; i++) {
            auto [res, rem] = div(n, (int)pow(10, i));
            if (partition(target, res, acc+ rem)) return true;
            if (res == 0) break;
        }

        return false;
    }
};
