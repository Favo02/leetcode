class AllOne {

    unordered_map<int, unordered_set<string>> keys;
    unordered_map<string, int> count;
    set<int> values;

public:

    AllOne() {}

    void inc(string key) {
        if (count.contains(key)) {
            int cur_count = count[key];

            // remove old
            keys[cur_count].erase(key);
            if (keys[cur_count].size() == 0) {
                values.erase(cur_count);
            }

            // insert new
            count[key]++;
            keys[cur_count+1].insert(key);
            values.insert(cur_count+1);

        } else {
            count[key] = 1;
            keys[1].insert(key);
            values.insert(1);
        }
    }

    void dec(string key) {
        if (count.contains(key)) {
            int cur_count = count[key];

            // remove old
            keys[cur_count].erase(key);
            if (keys[cur_count].size() == 0) {
                values.erase(cur_count);
            }

            // insert new
            if (cur_count-1 > 0) {
                count[key]--;
                keys[cur_count-1].insert(key);
                values.insert(cur_count-1);
            } else {
                count.erase(key);
            }
        }
    }

    string getMaxKey() {
        if (values.empty()) {
            return "";
        }
        auto max = *--values.end();
        return *keys[max].begin();
    }

    string getMinKey() {
        if (values.empty()) {
            return "";
        }
        auto min = *values.begin();
        return *keys[min].begin();
    }
};

/**
 * Your AllOne object will be instantiated and called as such:
 * AllOne* obj = new AllOne();
 * obj->inc(key);
 * obj->dec(key);
 * string param_3 = obj->getMaxKey();
 * string param_4 = obj->getMinKey();
 */
