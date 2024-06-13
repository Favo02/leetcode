impl Solution {
    pub fn climb_stairs(n: i32) -> i32 {
        let mut last_two = (1, 1);
        let mut cur = 1;

        for i in 0..n-1 {
            cur = last_two.0 + last_two.1;
            last_two.0 = last_two.1;
            last_two.1 = cur;
        }

        cur
    }
}
