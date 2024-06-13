impl Solution {
    pub fn sort_colors(nums: &mut Vec<i32>) {
        for i in 0..nums.len() {
            for j in i+1..nums.len() {
                if nums[j] < nums[i] {
                    nums.swap(i, j);
                }
            }
        }
    }
}
