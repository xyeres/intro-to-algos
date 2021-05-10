from linked_list import LinkedList


def merge_sort(linked_list):
    """
    Sorts a linked list into ascending order
        - recursively divide the linked list into sublists containing a single node
        - repeatedly merge the sublists to produce sorted sublists until one remains
        Returns a sorted linked list
        Time: O(kn log n)
    """

    if linked_list.size() == 1:
        return linked_list
    elif linked_list.head is None:
        return linked_list

    left_half, right_half = split(linked_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def split(linked_list):
    """
    Divide the unsorted list at midpoint into sublists
    Time: O(k log n)
    """

    if linked_list is None or linked_list.head is None:
        left_half = linked_list # if list has 1 item asign it to left half
        right_half = None # asign right to none becuase there was only 1 item

        return left_half, right_half
    else:
        size = linked_list.size()
        mid = size // 2
        mid_node = linked_list.node_at_index(mid - 1)

        left_half = linked_list
        right_half = LinkedList()
        right_half.head = mid_node.next_node
        mid_node.next_node = None # disconnect the left half from the right

        return left_half, right_half

def merge(left, right):
    """
    Merges two ll, sorting by data in nodes
    Returns new, merged, ll
    Time: O(n)
    """
    # Create a new ll that contains nodes from
    # merging left and right
    merged = LinkedList()
    # Add fake head that is discarded later
    merged.add(0)
    # Set current to the head of the ll
    current = merged.head
    #obtain head noes for left and right ll
    left_head = left.head
    right_head = right.head
    # iterate over left and right, until we reach 
    # tail of either
    while left_head or right_head:
        # If the head node of left is None, we're past the tail
        # Add the node from the right to merged LinkedList
        if left_head is None:
            current.next_node = right_head
            # Call next on right to set loop condition to False
            right_head = right_head.next_node
        # If the head node of right is None, we're past the tail
        # Add the tail node from left to merged linked list
        elif right_head is None:
            current.next_node = left_head
            # Call next on left to set loop condition to False
            left_head = left_head.next_node
        else:
            # Not at either tail node
            # Obtain node data to perform comparison operations
            left_data = left_head.data
            right_data = right_head.data
            # If data on left is less than right, set current to left node
            if left_data < right_data:
                current.next_node = left_head
                # move left head to next node
                left_head = left_head.next_node
            # If data on left is greater than right, set urrent to right node
            else:
                current.next_node = right_head
                # move right head to next node
                right_head = right_head.next_node
        # Move current to next node
        current = current.next_node

    # Discard fake head and set first merged node as head
    head = merged.head.next_node
    merged.head = head
    return merged

l = LinkedList()
l.add(0)
l.add(342)
l.add(24)
l.add(450)

print(l)
sorted_ll = merge_sort(l)
print(sorted_ll)