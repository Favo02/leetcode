impl Solution {
    pub fn max_distance(mut position: Vec<i32>, qty: i32) -> i32 {
        position.sort();
        let max = position[position.len()-1]+1;
        let min = position[0];

        let mut low = 1;
        let mut high = (max - min) / (qty - 1);;

        while low < high {
            let mid = low + ((high+1) - low) / 2;
            if is_valid(&position, qty, mid) {
                low = mid;
            }
            else {
                high = mid-1;
            }
        }

        low
    }
}

fn is_valid(position: &Vec<i32>, mut qty: i32, cur: i32) -> bool {

    let mut last = position[0];
    for p in position {
        if p - last >= cur {
            last = *p;
            qty -= 1;
        }

        if qty == 1 {
            return true
        }
    }

    false
}
