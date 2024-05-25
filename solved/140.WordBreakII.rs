impl Solution {
    pub fn word_break(s: String, word_dict: Vec<String>) -> Vec<String> {
        match solve(s, &word_dict) {
            Some(vec) => vec,
            None => Vec::new(),
        }
    }
}

fn solve(s: String, word_dict: &Vec<String>) -> Option<Vec<String>> {
    let mut res = Vec::new();

    for i in 0..s.len() {
        if word_dict.contains(&String::from(&s[..i + 1])) {
            if i + 1 == s.len() {
                res.push(String::from(&s[..i + 1]));
            }

            if let Some(words) = solve(String::from(&s[i + 1..]), word_dict) {
                let mut w = words
                    .iter()
                    .map(|w| String::from(&s[..i + 1]) + " " + w)
                    .collect();
                res.append(&mut w);
            }
        }
    }

    if res.is_empty() {
        None
    } else {
        Some(res)
    }
}

// ---
struct Solution;
fn s(s: &str) -> String {
    String::from(s)
}
fn main() {
    Solution::word_break(
        s("catsanddog"),
        [s("cat"), s("cats"), s("and"), s("sand"), s("dog")].to_vec(),
    );

    Solution::word_break(
        s("catsanddog"),
        [s("cat"), s("cats"), s("and"), s("dog")].to_vec(),
    );

    Solution::word_break(s("aaaaaaa"), [s("aaaa"), s("aa"), s("a")].to_vec());
}
