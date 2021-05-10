from linked_list import LinkedList


def merge_sort(linked_list):
    """
    Sorts a linked list into ascending order
        - recursively divide the linked list into sublists containing a single node
        - repeatedly merge the sublists to produce sorted sublists until one remains

        Returns a sorted linked list
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