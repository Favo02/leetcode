impl Solution {
    pub fn convert(s: String, num_rows: i32) -> String {
        let s: Vec<char> = s.chars().collect();
        let mut res = String::new();

        for row in 0..num_rows {
            let mut i = row as usize;
            let mut goingdown = true;

            while i < s.len() {
                let gap = match (row, goingdown) {
                    (0, _) => 2*(num_rows -1),
                    (val, _) if val == num_rows - 1 => 2*(num_rows -1),
                    (_, true) => {
                        goingdown = !goingdown;
                        2*(num_rows-1 - row)
                    }
                    (_, false) => {
                        goingdown = !goingdown;
                        2*row
                    }
                };

                res.push(s[i]);
                i += i32::max(1, gap) as usize;
            }
        }

        res
    }
}
