impl Solution {
    pub fn append_characters(source: String, target: String) -> i32 {
        let target: Vec<char> = target.chars().collect();
        let mut max = 0;
        for s in source.chars() {
            if s == target[max] {
                max += 1;
            }
            if max == target.len() {
                return 0
            }
        }
        (target.len() - max) as i32
    }
}
