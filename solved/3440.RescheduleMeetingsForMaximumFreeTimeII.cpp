class Solution {
public:
    int maxFreeTime(int eventTime, vector<int>& startTime, vector<int>& endTime) {
        sort(startTime.begin(), startTime.end());
        sort(endTime.begin(), endTime.end());

        int E = startTime.size();

        vector<pair<int, int>> gaps;

        for (int i = 0; i < E+1; i++) {
            int gap;
            if (i == 0) gap = startTime[0];
            else if (i == E) gap = eventTime - endTime[E-1];
            else gap = startTime[i] - endTime[i-1];
            gaps.push_back({-gap, i});
            sort(gaps.begin(), gaps.end());
            if (gaps.size() > 3) gaps.pop_back();
        }

        if (gaps[0].first == 0) return 0;

        int res = 0;
        for (int i = 0; i < E; i++) {
            int without = 0;
            if (i == 0) without = startTime[1];
            else if (i == E-1) without = eventTime - endTime[E-2];
            else without = startTime[i+1] - endTime[i-1];

            int size = endTime[i] - startTime[i];
            bool canmove = false;

            for (int g = 0; !canmove && g < gaps.size(); g++) {
                if (-gaps[g].first < size) break;
                if (gaps[g].second == i || gaps[g].second == i+1) continue;
                canmove = true;
            }

            if (!canmove) without -= size;
            res = max(res, without);
        }

        return res;
    }
};
