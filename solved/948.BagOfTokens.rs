impl Solution {
  pub fn bag_of_tokens_score(mut tokens: Vec<i32>, mut power: i32) -> i32 {
    let mut score = 0;
    let mut res = 0;

    tokens.sort();

    let mut start = 0;
    let mut end = tokens.len();

    loop {
      while start < end && power >= tokens[start] {
        score += 1;
        power -= tokens[start];
        start += 1;
      }
      res = std::cmp::max(res, score);

      if score > 0 {
        end -= 1;
        score -= 1;
        power += tokens[end];
      }
      else {
        break
      }
    }

    res
  }
}

struct Solution;

fn main() {
  println!("{}", Solution::bag_of_tokens_score(vec![100], 50));
  println!("{}", Solution::bag_of_tokens_score(vec![200,100], 150));
  println!("{}", Solution::bag_of_tokens_score(vec![100,200,300,400], 200));
  println!("{}", Solution::bag_of_tokens_score(vec![26], 51));
  println!("{}", Solution::bag_of_tokens_score(vec![71,55,82], 54));
}
