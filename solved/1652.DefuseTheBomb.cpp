#include <bits/stdc++.h>
using namespace std;

class Solution {
    int mod(int a, int b) {
        return (a % b + b) % b;
    }

public:
    vector<int> decrypt(vector<int>& code, int k) {

        vector<int> res(code.size(), 0);
        int N = code.size();

        if (k > 0) {
            for (int i = 0; i < N; i++) {
                for (int ii = 0; ii < k; ii++) {
                    res[i] += code[(i+ii+1) % N];
                }
            }
        } else if (k < 0) {
            for (int i = 0; i < N; i++) {
                cout << code[i] << ": ";
                for (int ii = 0; ii < -k; ii++) {
                    res[i] += code[mod(i-ii-1, N)];
                }
                cout << endl;
            }
        }

        return res;
    }
};
