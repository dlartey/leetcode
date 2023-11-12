/**
 * // This is the ImmutableListNode's API interface.
 * // You should not implement it, or speculate about its implementation.
 * interface ImmutableListNode {
 *     public void printValue(); // print the value of this node.
 *     public ImmutableListNode getNext(); // return the next node.
 * };
 */

class Solution {
    public void printLinkedListInReverse(ImmutableListNode head) {
        
        Stack<ImmutableListNode> stk = new Stack<>();
        
        while (head != null){
            stk.push(head);
            head = head.getNext();
        }
        
        while (!stk.isEmpty()){
            stk.pop().printValue();
        }
        
        
    }
}