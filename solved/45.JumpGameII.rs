impl Solution {
    pub fn jump(nums: Vec<i32>) -> i32 {

        let mut jumps: Vec<Option<i32>> = vec![None; nums.len()];
        jumps[0] = Some(0);

        for (i, n) in nums.iter().enumerate() {
            let cur = jumps[i].unwrap() + 1;
            for j in i+1..usize::min(i + 1 + *n as usize, nums.len()) {
                match jumps[j] {
                    None => jumps[j] = Some(cur),
                    Some(ju) if ju > cur => jumps[j] = Some(cur),
                    _ => ()
                }
            }
        }

        jumps[nums.len()-1].unwrap()
    }
}
