impl Solution {
    pub fn chalk_replacer(chalk: Vec<i32>, mut k: i32) -> i32 {

        let sum = chalk.iter().map(|e| *e as i64).sum::<i64>();
        k = (k as i64 % sum) as i32;

        let mut i = 0;
        while k >= 0 {
            k -= chalk[i % chalk.len()];
            i += 1;
        }

        ((i-1) % chalk.len()) as i32
    }
}
