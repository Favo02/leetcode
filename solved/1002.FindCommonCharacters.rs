use std::collections::hash_map::HashMap;

impl Solution {
    pub fn common_chars(words: Vec<String>) -> Vec<String> {
        let mut counts: Vec<Vec<u32>> = Vec::new();
        for w in words {
            counts.push(
                w.chars().fold(vec![0; 26], |mut count: Vec<u32>, c| {
                    count[c as usize - 'a' as usize] += 1;
                    count
                })
            );
        }

        let mut res: Vec<String> = Vec::new();
        for k in 0..26 {
            let mut amount: u32 = counts[0][k];
            for c in &counts {
                amount = u32::min(amount, *c.get(k).unwrap_or(&0));
            }
            for _ in 0..amount {
                res.push(String::from(char::from((k + 97) as u8)));
            }
        }

        res
    }
}
