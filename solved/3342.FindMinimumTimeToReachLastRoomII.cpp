class Solution {
public:
    int minTimeToReach(vector<vector<int>>& moveTime) {
        int X = moveTime[0].size();
        int Y = moveTime.size();

        vector<vector<vector<int>>> time(2, vector<vector<int>>(Y, vector<int>(X, 1e9 + 5000)));
        time[1][0][0] = 0;

        // time, last_move, y*X+x
        priority_queue<tuple<int,int,int>> queue;
        queue.push({0, 1, 0});

        while (!queue.empty()) {
            auto [t, move, cur] = queue.top();
            queue.pop();

            int x = cur % X;
            int y = cur / X;

            if (-t != time[move][y][x]) continue;

            if (x == X-1 && y == Y-1) {
                return time[move][y][x];
            }

            for (int dx = -1; dx <= 1; dx++) {
                for (int dy = -1; dy <= 1; dy++) {
                    if (abs(dx) + abs(dy) != 1) continue;

                    int nx = x + dx, ny = y + dy;
                    if (!(0 <= nx && nx < X)) continue;
                    if (!(0 <= ny && ny < Y)) continue;

                    int newmove = (move+1) % 2;
                    int newtime = max(moveTime[ny][nx], time[move][y][x]) + newmove + 1;

                    if (newtime >= time[newmove][ny][nx]) continue;
                    time[newmove][ny][nx] = newtime;

                    queue.push({-newtime, newmove, ny*X+nx});
                }
            }
        }

        cout << "Assertion error: bottom right not reached" << endl;
        return -1;

    }
};
