import java.util.Queue;
import java.util.LinkedList;

// allowed operations for queue:
// push to back, peek/pop from front, size, is empty

class MyStack {

  Queue<Integer> queue;

  public MyStack() {
    queue = new LinkedList<>();  
  }
  
  public void push(int x) {
    queue.add(x);
  }
  
  // move old queue into new one (except for last one) to iterate over elements
  public int pop() {
    Queue<Integer> newQ = new LinkedList<>();
    while(queue.size() > 1) {
      newQ.add(queue.poll());
    }
    int retValue = queue.poll();
    queue = newQ;
    return retValue;
  }
  
  // move old queue into new one to iterate over elements
  public int top() {
    Queue<Integer> newQ = new LinkedList<>();
    int last = 0;
    while(!queue.isEmpty()) {
      last = queue.poll();
      newQ.add(last);
    }
    queue = newQ;
    return last;
  }
  
  public boolean empty() {
    return queue.isEmpty();
  }
}
