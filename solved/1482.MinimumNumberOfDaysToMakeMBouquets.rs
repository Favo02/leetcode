impl Solution {
    pub fn min_days(bloom_day: Vec<i32>, buq: i32, size: i32) -> i32 {
        let mut min = *bloom_day.iter().min().unwrap();
        let mut max = *bloom_day.iter().max().unwrap()+1;

        while min < max {
            let mid = min + ((max - min) / 2);
            match is_valid(mid, &bloom_day, buq, size) {
                true => max = mid,
                false => min = mid+1
            }
        }

        if max == (*bloom_day.iter().max().unwrap())+1 ?
            -1
        } else {
            max
        }
    }
}

fn is_valid(day: i32, bloom_day: &Vec<i32>, buq: i32, size: i32) -> bool {
    let mut found = 0;
    let mut cur = 0;

    for b in bloom_day {
        if &day >= b {
            cur += 1;
        }
        else {
            cur = 0;
        }

        if cur == size {
            found += 1;
            cur = 0;
        }

        if found == buq {
            return true
        }
    }

    found >= buq
}
