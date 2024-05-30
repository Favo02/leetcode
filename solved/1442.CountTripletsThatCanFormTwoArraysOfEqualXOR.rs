impl Solution {
    pub fn count_triplets(arr: Vec<i32>) -> i32 {
        let mut res: i32 = 0;
        for i in 0..arr.len() {
            let mut xor: i32 = arr[i];
            for j in i + 1..arr.len() {
                xor ^= arr[j];
                if xor == 0 {
                    res += (j - i) as i32;
                }
            }
        }
        res
    }
}
