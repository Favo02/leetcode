impl Solution {
    pub fn score_of_string(s: String) -> i32 {
        s.chars()
        .zip(s.chars().skip(1))
        .fold(0, |acc, (a, b)| acc + i32::abs(a as i32 - b as i32))
    }
}
