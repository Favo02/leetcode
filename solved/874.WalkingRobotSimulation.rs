use std::collections::HashSet;

impl Solution {
    pub fn robot_sim(commands: Vec<i32>, obstacles: Vec<Vec<i32>>) -> i32 {

        let obs: HashSet<(i32, i32)> = HashSet::from_iter(obstacles.iter().map(|o| (o[0], o[1])));

        let dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)];
        let mut curdir: i8 = 0;

        let (mut x, mut y) = (0, 0);
        let mut res = 0;

        for c in commands {
            match c {
                -2 => curdir = (curdir-1).rem_euclid(4),
                -1 => curdir = (curdir+1).rem_euclid(4),
                n => {
                    for i in 0..n {
                        (x, y) = (x + (dirs[curdir as usize].0), y + (dirs[curdir as usize].1));
                        if obs.contains(&(x,y)) {
                            (x, y) = (x + (dirs[curdir as usize].0 * -1), y + (dirs[curdir as usize].1 * -1));
                            break;
                        }
                    }
                }
            }

            res = res.max(x.pow(2) + y.pow(2));
        }

        res
    }
}
