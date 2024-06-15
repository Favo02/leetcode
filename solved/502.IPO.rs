use std::collections::VecDeque;
use std::collections::BinaryHeap;

impl Solution {
    pub fn find_maximized_capital(k: i32, mut w: i32, profits: Vec<i32>, capital: Vec<i32>) -> i32 {
        let mut projects: Vec<(i32, i32)> = profits
            .into_iter()
            .zip(capital.into_iter())
            .collect();

        projects.sort_by_key(|(.., req)| *req);

        let mut not_available = VecDeque::from(projects);
        let mut available: BinaryHeap<i32> = BinaryHeap::new();

        for _ in 0..k {
            while let Some(req) = not_available.front() {
                if req.1 > w {
                    break
                }
                available.push(not_available.pop_front().unwrap().0)
            }

            match available.pop() {
                Some(cap) => w += cap,
                None => break
            }
        }

        w
    }
}
