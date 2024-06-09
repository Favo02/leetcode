impl Solution {
    pub fn replace_words(mut dictionary: Vec<String>, sentence: String) -> String {

        let sentence = sentence.split(" ");
        dictionary.sort_by(|a, b| {
            a.len().cmp(&b.len())
        });

        let mut res: Vec<String> = Vec::new();
        for word in sentence {
            let mut root_found: Option<String> = None;

            for root in &dictionary {
                if word.len() < root.len() {
                    continue
                }
                if *root == word[..root.len()] {
                    root_found = Some(root.to_string());
                    break
                }
            }

            match root_found {
                Some(root) => res.push(root),
                None => res.push(word.to_string())
            }
        }

        res.join(" ")
    }
}
