#include <bits/stdc++.h>
using namespace std;

#define ll long long

class Solution {

    ll key(int r, int c, int COLS) {
        return r*COLS + c;
    }

public:
    int minimumObstacles(vector<vector<int>>& grid) {

        vector<pair<int, int>> DIRS = {{0,1}, {0,-1}, {1,0}, {-1,0}};

        int COLS = grid[0].size();
        int ROWS = grid.size();

        deque<pair<int, int>> queue;
        queue.push_back({0, 0});

        vector<int> dist(ROWS * COLS, 1e9);
        dist[0] = 0;

        while (!queue.empty()) {
            auto [r, c] = queue.front();
            queue.pop_front();

            int cur_dist = dist[key(r, c, COLS)];

            for (auto dir : DIRS) {
                auto [dr, dc] = dir;
                int nr = r + dr, nc = c + dc;

                if (!(0 <= nc && nc < COLS)) continue;
                if (!(0 <= nr && nr < ROWS)) continue;

                if (cur_dist + grid[nr][nc] < dist[key(nr, nc, COLS)]) {
                    dist[key(nr, nc, COLS)] = cur_dist + grid[nr][nc];
                    queue.push_back({nr, nc});
                }
            }
        }

        return dist[ROWS * COLS - 1];
    }
};
