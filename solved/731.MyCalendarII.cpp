class MyCalendarTwo {

    multiset<pair<int, bool>> events;

public:

    MyCalendarTwo() {}

    bool book(int start, int end) {
        events.insert(pair<int, bool>(start, true));
        events.insert(pair<int, bool>(end, false));

        int cur = 0;
        for (auto e : events) {
            if (e.second) {
                cur++;
            } else {
                cur--;
            }
            if (cur >= 3) {
                events.erase(events.lower_bound(pair<int, bool>(start, true)));
                events.erase(events.lower_bound(pair<int, bool>(end, false)));
                return false;
            }
        }
        return true;
    }
};

/**
 * Your MyCalendarTwo object will be instantiated and called as such:
 * MyCalendarTwo* obj = new MyCalendarTwo();
 * bool param_1 = obj->book(start,end);
 */
