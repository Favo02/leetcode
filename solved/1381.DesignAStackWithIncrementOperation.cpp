class CustomStack {

    vector<int> arr;
    int next;

public:

    CustomStack(int maxSize) {
        arr = vector<int>(maxSize, -1);
        next = 0;
    }

    void push(int x) {
        if (next < arr.size()) {
            arr[next] = x;
            next++;
        }
    }

    int pop() {
        int res = -1;
        if (next > 0) {
            res = arr[next-1];
            next--;
        }
        return res;
    }

    void increment(int k, int val) {
        for (int i = 0; i < min((int)arr.size(), k); i++) {
            arr[i] += val;
        }
    }
};

/**
 * Your CustomStack object will be instantiated and called as such:
 * CustomStack* obj = new CustomStack(maxSize);
 * obj->push(x);
 * int param_2 = obj->pop();
 * obj->increment(k,val);
 */
