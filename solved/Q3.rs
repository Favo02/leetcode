impl Solution {
    pub fn find_max_consecutive_ones(nums: Vec<i32>) -> i32 {
        nums.split(|&n| n == 0)
            .map(|chunk| chunk.len() as i32)
            .max()
            .unwrap_or(0)
    }
}

struct Solution;
fn main() {
    println!(
        "{:?}",
        Solution::find_max_consecutive_ones(vec![1, 1, 0, 1, 1, 1])
    );
}
