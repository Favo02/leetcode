use std::collections::{HashSet, VecDeque};

impl Solution {
    pub fn count_sub_islands(grid1: Vec<Vec<i32>>, grid2: Vec<Vec<i32>>) -> i32 {

        fn bfs(grid1: &Vec<Vec<i32>>, grid2: &Vec<Vec<i32>>, x: usize, y: usize) -> (bool, HashSet<(usize, usize)>) {
            let mut queue = VecDeque::from([(x, y)]);
            let mut island: HashSet<(usize, usize)> = HashSet::new();

            let DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)];

            while let Some((x, y)) = queue.pop_front() {
                for (dx, dy) in DIRS.iter() {
                    let (xx, yy) = (x as i32 + dx, y as i32 + dy);
                    if xx < 0 || xx >= grid1[0].len() as i32 {
                        continue;
                    }
                    if yy < 0 || yy >= grid1.len() as i32 {
                        continue;
                    }
                    let (xx, yy) = (xx as usize, yy as usize);

                    if grid2[yy][xx] == 0 || island.contains(&(xx, yy)) {
                        continue
                    }
                    island.insert((xx, yy));

                    if grid1[yy][xx] == 1 {
                        queue.push_back((xx, yy));
                    } else {
                        return (false, island)
                    }
                }

            }

            (true, island)
        }

        let mut used: HashSet<(usize, usize)> = HashSet::new();
        let mut res: i32 = 0;

        for y in 0..grid2.len() {
            for x in 0..grid2[0].len() {

                if used.contains(&(x, y)) {
                    continue;
                }

                if grid2[y][x] == 1 && grid1[y][x] == 1 {
                    let (valid, island) = bfs(&grid1, &grid2, x, y);
                    if valid {
                        res += 1;
                    }
                    used.extend(island);
                }

            }
        }

        res
    }
}
