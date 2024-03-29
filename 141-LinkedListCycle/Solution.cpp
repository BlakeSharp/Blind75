/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
        unordered_map<ListNode*,int> visited;
        while(head){
            if(visited.count(head)>0)
                return true;
            else
                visited[head]=1;
            head=head->next;
        }
        return false;
        }
};
