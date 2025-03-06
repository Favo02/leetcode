class Solution {
public:
    void print(vector<int> &a) {
        for (auto n : a) cout << n << " ";
        cout << endl;
    }

    vector<int> constructDistancedSequence(int n) {
        auto res = vector<int>((n-1)*2 + 1, 0);

        set<int> to_place;
        for (int i = 1; i <= n; i++) to_place.insert(i);

        solve(res, 0, to_place);

        return res;
    }

    bool solve(vector<int> &sol, int index, set<int> to_place) {
        if (to_place.empty() || index >= sol.size()) return true;
        if (sol[index] > 0) return solve(sol, index+1, to_place);

        for (auto n = to_place.rbegin(); n != to_place.rend(); n++) {
            auto nn = *n;

            if (nn == 1) {
                sol[index] = nn;
                to_place.erase(nn);
                if (solve(sol, index+1, to_place)) {
                    return true;
                }
                to_place.insert(nn);
                sol[index] = 0;
                continue;
            }

            if (index+nn >= sol.size() || sol[index+nn] > 0) continue;
            sol[index] = nn;
            sol[index+nn] = nn;
            to_place.erase(nn);
            if (solve(sol, index+1, to_place)) {
                return true;
            }
            to_place.insert(nn);
            sol[index+nn] = 0;
            sol[index] = 0;
        }

        return false;
    }
};
