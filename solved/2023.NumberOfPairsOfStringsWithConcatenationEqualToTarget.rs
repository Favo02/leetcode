impl Solution {
    pub fn num_of_pairs(nums: Vec<String>, target: String) -> i32 {
        let mut res = 0;

        for (i, n1) in nums
            .iter()
            .enumerate()
            .filter(|(.., s)| s.len() < target.len())
            .filter(|(.., s)| s == &&target[..s.len()]) {

            let b = &target[n1.len()..];

            res += nums
                .iter()
                .enumerate()
                .filter(|(j, ..)| j != &i)
                .filter(|(.., s)| s == &b)
                .count();
        }

        res as i32
    }
}
