impl Solution {
    pub fn missing_rolls(rolls: Vec<i32>, mean: i32, n: i32) -> Vec<i32> {

        let sum: i32 = rolls.iter().sum();
        let size = rolls.len() as i32 + n;
        let missing_sum = (mean * size) - sum;

        if (missing_sum < n) {
            return Vec::new()
        }

        let avg: i32 = missing_sum / n;
        let mut rem = missing_sum - (avg*n);

        if (avg > 6) {
            return Vec::new()
        }

        let mut res = vec![avg; n as usize];
        let mut i = 0;
        while (rem > 0) {
            if res[i % n as usize] >= 6 {
                return Vec::new()
            }
            res[i % n as usize] += 1;
            i += 1;
            rem -= 1;
        }

        Vec::from(res)
    }
}
