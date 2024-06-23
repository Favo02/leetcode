impl Solution {
    pub fn judge_square_sum(c: i32) -> bool {

        for a in 0..=((c as f64).sqrt() as i32 + 1) {

            let b = ((c - a.pow(2)) as f64).sqrt();
            if b == (b as u32) as f64 {
                return true
            }

        }
        false
    }
}
