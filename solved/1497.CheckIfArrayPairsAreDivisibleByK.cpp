class Solution {
public:
    long mod(long a, long b) {
        return (a%b+b)%b;
    }

    bool canArrange(vector<int>& arr, int k) {

        vector<int> rem(k);
        for (auto n : arr) {
            rem[mod(n, k)]++;
        }

        if ((k % 2 == 0) && (rem[k/2] % 2 != 0)) {
            return false;
        }

        for (int i = 1; i <= k/2; i++) {
            if (rem[i] != rem[k-i]) {
                return false;
            }
        }

        return true;
    }
};
