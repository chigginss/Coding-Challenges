  
""" Check to see if a linkedlist is a palindrome """

  def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        new_list = []
        current = head
        while current is not None:
            new_list.append(current.val)
            current = current.next

        if new_list == new_list[::-1]:
            return True
        else:
            return False