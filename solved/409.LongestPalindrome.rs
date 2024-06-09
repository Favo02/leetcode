use std::collections::hash_map::HashMap;

impl Solution {
    pub fn longest_palindrome(s: String) -> i32 {
        let mut count: HashMap<char, i32> = HashMap::new();
        for c in s.chars() {
            *count.entry(c).or_insert(0) += 1;
        }

        let mut res = 0;
        let mut first_odd = true;
        for (_, val) in count {
            match (val % 2 == 0, first_odd) {
                (true, _) => res += val,
                (false, true) => {
                    res += val;
                    first_odd = false;
                }
                _ => res += (val-1)
            }
        }
        res
    }
}
