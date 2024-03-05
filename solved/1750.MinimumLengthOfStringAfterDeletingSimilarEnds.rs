impl Solution {
  pub fn minimum_length(s: String) -> i32 {
    let mut last = match s.chars().nth(0) {
      Some(c) => c,
      None => panic!()
    };
    let mut count = 1;
    let mut chars = Vec::new();

    for c in s.chars().skip(1).take(s.len()-1) {
      if c == last {
        count += 1;
      }
      else {
        chars.push((last, count));
        last = c;
        count = 1;
      }
    }
    chars.push((last, count));

    if chars.len() == 1 {
      return if chars[0].1 > 1 {0} else {1};
    }

    let mut start = 0;
    let mut end = chars.len()-1;
    let mut res = s.len() as i32;

    loop {
      if chars[start].0 == chars[end].0 && end > 0 {
        res -= chars[start].1;
        res -= chars[end].1;
        start += 1;
        end -= 1;
      }
      else {
        break;
      }
      if start >= end {
        if start == end && chars[start].1 > 1 {
          res = 0;
        }
        break;
      }
    }

    res
  }
}

struct Solution;

fn main() {
  println!("{}", Solution::minimum_length("ca".to_string()));
  println!("{}", Solution::minimum_length("cabaabac".to_string()));
  println!("{}", Solution::minimum_length("aabccabba".to_string()));
  println!("{}", Solution::minimum_length("bbbbbbbbbbbbbbbbbbbbbbbbbbbabbbbbbbbbbbbbbbccbcbcbccbbabbb".to_string()));
  println!("{}", Solution::minimum_length("c".to_string()));
  println!("{}", Solution::minimum_length("bbbbbbbbbbbbbbbbbbb".to_string()));
}
