use std::collections::VecDeque;

impl Solution {
    pub fn min_patches(mut nums: Vec<i32>, target: i32) -> i32 {

        let mut nums = VecDeque::from(nums);
        let mut next: i64 = 1;
        let mut res = 0;

        while next <= target as i64 {

            if !nums.is_empty() && nums.front().unwrap() <= &(next as i32) {
                next += nums.pop_front().unwrap() as i64;
            }
            else {
                res += 1;
                next += next;
            }
        }

        res
    }
}
