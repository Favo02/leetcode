impl Solution {
    pub fn height_checker(heights: Vec<i32>) -> i32 {
        let mut sorted = heights.clone();
        sorted.sort();
        heights.into_iter().zip(sorted).fold(0, |acc, (h, s)| {
            match h == s {
                true => acc,
                false => acc + 1
            }
        })
    }
}
