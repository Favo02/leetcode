class MyCalendarThree {

    multiset<pair<int, bool>> events;

public:

    MyCalendarThree() {}

    int book(int start, int end) {
        events.insert(pair<int, bool>(start, true));
        events.insert(pair<int, bool>(end, false));

        int cur = 0;
        int res = 0;
        for (auto e : events) {
            if (e.second) {
                cur++;
            } else {
                cur--;
            }
            res = max(res, cur);
        }
        return res;
    }
};

/**
 * Your MyCalendarThree object will be instantiated and called as such:
 * MyCalendarThree* obj = new MyCalendarThree();
 * int param_1 = obj->book(startTime,endTime);
 */
