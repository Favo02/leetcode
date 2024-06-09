use std::collections::HashMap;

impl Solution {
    pub fn is_n_straight_hand(mut hand: Vec<i32>, group_size: i32) -> bool {
        let mut nums: HashMap<i32, i32> = hand
            .iter()
            .fold(HashMap::new(), |mut map, n| {
                *map.entry(*n).or_insert(0) += 1;
                map
            });

        let mut keys: Vec<i32> = nums.keys().cloned().collect();
        keys.sort_unstable();

        'nextkey: for k in keys {
            let mut qty: i32 = 0;

            for incr in 0..group_size {
                match (incr, nums.get_mut(&(k + incr))) {
                    (0, None) | (0, Some(0)) => continue 'nextkey,
                    (0, Some(available)) => qty = *available,

                    (_, None) | (_, Some(0)) => return false,
                    (_, Some(available)) if available < &mut qty => return false,

                    (_, Some(available)) => *available -= qty
                }
            }
        }

        true
    }
}
