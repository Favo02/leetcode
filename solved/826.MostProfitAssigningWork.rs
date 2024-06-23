impl Solution {
    pub fn max_profit_assignment(difficulty: Vec<i32>, profit: Vec<i32>, mut worker: Vec<i32>) -> i32 {
        let mut jobs: Vec<(i32, i32)> = difficulty
            .into_iter()
            .zip(profit.into_iter())
            .collect();

        jobs.sort_by_key(|(d, p)| *d);
        worker.sort();

        let mut res = 0;
        let mut max = 0;
        let mut fine = 0;

        for w in worker {
            while fine < jobs.len() && w >= jobs[fine].0 {
                max = max.max(jobs[fine].1);
                fine += 1;
            }

            res += max;
        }

        res
    }
}
