use std::collections::HashMap;
use core::cmp::Ordering;

impl Solution {
    pub fn relative_sort_array(mut arr1: Vec<i32>, arr2: Vec<i32>) -> Vec<i32> {

        let indexes: HashMap<i32, usize> = arr2
            .iter()
            .enumerate()
            .fold(HashMap::new(), |mut map, (i, n)| {
                map.insert(*n, i);
                map
            });

        arr1.sort_by(|a, b| {
            match (indexes.get(a), indexes.get(b)) {
                (Some(i1), Some(i2)) => i1.partial_cmp(i2).unwrap(),
                (Some(_), None) => Ordering::Less,
                (None, Some(_)) => Ordering::Greater,
                _ => a.partial_cmp(b).unwrap()
            }
        });
        arr1
    }
}
