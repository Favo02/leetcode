impl Solution {
    pub fn max_area(h: i32, w: i32, mut horizontal_cuts: Vec<i32>, mut vertical_cuts: Vec<i32>) -> i32 {
        let maxh = max_diff(horizontal_cuts, h);
        let maxw = max_diff(vertical_cuts, w);

        (maxh as i64 * maxw as i64 % (10_i64.pow(9) + 7)) as i32
    }
}

fn max_diff(mut nums: Vec<i32>, end: i32) -> i32 {
    nums.push(0);
    nums.push(end);
    nums.sort();

    nums.iter()
        .zip(&nums[1..])
        .map(|(a,b)| b-a)
        .max()
        .unwrap()
}
