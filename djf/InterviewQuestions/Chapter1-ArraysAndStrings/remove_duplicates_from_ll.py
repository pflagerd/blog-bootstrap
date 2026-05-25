'''
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	
'''
class Solution:
    #Function to remove duplicates from unsorted linked list.
    # def removeDuplicates(self, head):
    #     # code here
    #     # return head after editing list
        
    #     # Remove duplicates of current node, then move current to the next node.
    #     current = head
    #     while current is not None:
    #         # Move a runner down the list to check for duplicates.
    #         runner = current
    #         while runner is not None and runner.next is not None:
    #             if runner.next.data == current.data:
    #                 # Remove the nodes
    #                 runner.next = runner.next.next
    #             runner = runner.next
    #         current = current.next
        
    #     return head
    
    def removeDuplicates( self, head ):
        if head is None:
            return head
            
        index = {}
        current = head
        index[ current.data ] = True
        while current.next is not None:
            # The first time we see each value, record it in the index.
            # If we see it again, checking the index, delete it.
            if index.get( current.next.data, False ):
                current.next = current.next.next
            else:
                index[ current.next.data ] = True
                current = current.next
        return head
                
