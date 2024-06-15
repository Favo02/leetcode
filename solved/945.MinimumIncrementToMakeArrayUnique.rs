use std::collections::HashSet;

impl Solution {
    pub fn min_increment_for_unique(mut nums: Vec<i32>) -> i32 {

        nums.sort();
        let mut max = -1;
        let mut res = 0;

        for n in nums {
            match max < n {
                true => max = n,
                false => {
                    res += (max-n)+1;
                    max += 1;
                }
            }
        }

        res
    }
}
