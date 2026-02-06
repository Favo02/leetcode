impl Solution {
    pub fn get_concatenation(mut nums: Vec<i32>) -> Vec<i32> {
        nums.append(&mut nums.clone());
        nums
    }
}

struct Solution;
fn main() {
    println!("{:?}", Solution::get_concatenation(vec![1, 2, 3]));
}
