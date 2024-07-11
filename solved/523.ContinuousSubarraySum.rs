use std::collections::HashMap;

impl Solution {
    pub fn check_subarray_sum(nums: Vec<i32>, k: i32) -> bool {

        let mut val: i32 = 0;
        let mut rem: HashMap<i32, i32> = HashMap::new();
        rem.insert(0, -1);

        for (i, n) in nums.iter().enumerate() {
            val += n;

            match rem.get(&(val % k)) {
                Some(index) if i as i32 - index >= 2 => return true,
                Some(_) => (),
                None => {
                    rem.insert(val % k, i as i32);
                }
            }
        }

        false
    }
}
