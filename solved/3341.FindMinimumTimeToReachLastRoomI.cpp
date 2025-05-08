class Solution {
public:
    int minTimeToReach(vector<vector<int>>& moveTime) {
        int X = moveTime[0].size();
        int Y = moveTime.size();

        vector<vector<int>> time(Y, vector<int>(X, 1e9 + 500));
        time[0][0] = 0;

        priority_queue<pair<int,int>> queue;
        queue.push({0, 0});

        while (!queue.empty()) {
            auto [t, cur] = queue.top();
            queue.pop();

            int x = cur % X;
            int y = cur / X;

            if (-t != time[y][x]) continue;

            if (x == X-1 && y == Y-1) {
                return time[y][x];
            }

            for (int dx = -1; dx <= 1; dx++) {
                for (int dy = -1; dy <= 1; dy++) {
                    if (abs(dx) + abs(dy) != 1) continue;

                    int nx = x + dx, ny = y + dy;
                    if (!(0 <= nx && nx < X)) continue;
                    if (!(0 <= ny && ny < Y)) continue;

                    int newtime = max(moveTime[ny][nx], time[y][x]) + 1;
                    if (newtime >= time[ny][nx]) continue;
                    time[ny][nx] = newtime;

                    queue.push({-newtime, ny*X+nx});
                }
            }
        }

        cout << "Assertion error: bottom right not reached" << endl;
        return -1;
    }
};
