impl Solution {
    pub fn shuffle(nums: Vec<i32>, n: i32) -> Vec<i32> {
        nums.clone()
            .into_iter()
            .take(n as usize)
            .zip(nums.into_iter().skip(n as usize))
            .flat_map(|(a, b)| vec![a, b])
            .collect()
    }
}

struct Solution;
fn main() {
    println!("{:?}", Solution::shuffle(vec![2, 5, 1, 3, 4, 7], 3));
}
