use std::collections::HashMap;

impl Solution {
    pub fn subarrays_div_by_k(nums: Vec<i32>, k: i32) -> i32 {

        let mut sum: i32 = 0;
        let mut res = 0;

        let mut occs = vec![0; k as usize];
        occs[0] = 1;

        for n in nums {
            sum += n;
            res += occs[sum.rem_euclid(k) as usize];
            occs[sum.rem_euclid(k) as usize] += 1;
        }

        res
    }
}
