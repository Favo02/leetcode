use std::collections::HashSet;

#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
  pub val: i32,
  pub next: Option<Box<ListNode>>
}

impl ListNode {
  #[inline]
  fn new(val: i32) -> Self {
    ListNode {
      next: None,
      val
    }
  }
}

impl Solution {
    pub fn modified_list(nums: Vec<i32>, head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        if let None = head {
            return None
        }

        let nums: HashSet<i32> = HashSet::from_iter(nums.into_iter());

        let mut newhead = ListNode { val: -1, next: head };
        let mut cur = &mut newhead;

        while let Some(ref mut next) = cur.next {

            if nums.contains(&next.val) {
                cur.next = next.next.take();
            } else {
                cur = cur.next.as_mut().unwrap();
            }

        }

        newhead.next
    }
}
