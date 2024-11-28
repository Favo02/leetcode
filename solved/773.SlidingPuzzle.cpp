#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    string key(vector<vector<int>>& board) {
        int res = 0;
        for (int i = 0; i < 3; i++) res += pow(10, i) * (board[0][i]+1);
        for (int i = 0; i < 3; i++) res += pow(10, i+3) * (board[1][i]+1);
        return to_string(res);
    }

    int slidingPuzzle(vector<vector<int>>& board) {
        vector<vector<int>> swaps = {{1,3}, {0,2,4}, {1,5}, {0,4}, {1,3,5}, {2,4}};

        unordered_set<string> seen;

        deque<pair<string, int>> queue;
        queue.push_back({key(board), 0});

        while (!queue.empty()) {
            auto [cur, dist] = queue.front();
            queue.pop_front();

            if (cur == "165432") return dist;

            for (int i = 0; i < 6; i++) {
                if (cur[i] == '1') {
                    for (auto sw : swaps[i]) {
                        string adj = cur;
                        swap(adj[i], adj[sw]);
                        if (seen.contains(adj)) continue;
                        seen.insert(adj);
                        queue.push_back({adj, dist+1});
                    }
                    break;
                }
            }
        }

        return -1;
    }
};

int main(int argc, char const *argv[]) {

    Solution s;

    vector<vector<int>> board;

    board = {{1, 2, 3}, {4, 5, 0}};
    cout << s.slidingPuzzle(board) << endl;

    board = {{1, 2, 3}, {4, 0, 5}};
    cout << s.slidingPuzzle(board) << endl;

    board = {{1, 2, 3}, {5, 4, 0}};
    cout << s.slidingPuzzle(board) << endl;

    board = {{4, 1, 2}, {5, 0, 3}};
    cout << s.slidingPuzzle(board) << endl;
}
