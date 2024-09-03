impl Solution {
    pub fn get_lucky(s: String, mut k: i32) -> i32 {
        let mut num: String = s.chars()
            .map(|s| s as u32 - 'a' as u32 + 1)
            .map(|s| s.to_string())
            .collect::<Vec<String>>()
            .join("");

        while k > 0 {
            num = num.chars()
                .map(|c| c as u32 - '0' as u32)
                .sum::<u32>()
                .to_string();
            k -= 1;
        }
        num.parse().unwrap()
    }
}
