#!python


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        Running time: O(N) because it will go through all of the notes everytime meaning a linear time complexity"""
        #start at head 
        node = self.head
        count = 0
        #loop until no more references
        while node is not None:
            count += 1
            #advance to next node
            node = node.next

        return count


    def append(self, item):
        """Insert the given item at the tail of this linked list.
        Running time: O(1) Should be because we are keeping track of the tail so it should be a constant operation"""
        new_node = Node(item)

        if self.tail is not None:
            #set the current tails pointer to this new node
            self.tail.next = new_node
            #point tail to new node
            self.tail = new_node
        #no node in list so set tail and head
        else:
            self.head = new_node
            self.tail = new_node

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        Running time: O(1) Should also be constant time for insertion since we keep track of the head node"""
        new_node = Node(item)
        #check is head exists
        if self.head is not None:
            #set new node to point to current head
            new_node.next = self.head
            #change head pointer
            self.head = new_node
        #no nodes in list
        else:
            self.head = new_node
            self.tail = new_node

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        Best case running time: O(1) Item is the first item in the list will be a since look up?
        Worst case running time: O(N) Item is last in list or not in list at all. Has to traverse entire linkedlist"""
        node = self.head

        while node is not None:
            if quality(node.data) == True:
                return node.data
            else:
                node = node.next

        return None

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        Best case running time: O(1) First item is deleted
        Worst case running time: O(N) Last item is deleted. Entire list must be traversed"""
        #set starting points
        current_node = self.head
        prev_node = None

        #while there are more nodes in list
        while current_node is not None:

            #node with item has been found
            if item == current_node.data:

                #item we want to remove is at head
                if prev_node is None:
                    #make head next node
                    self.head = current_node.next

                    #head is also tail
                    if current_node.next is None:
                        self.tail = prev_node
                #item we want to remove is at tail
                elif current_node.next is None:
                    prev_node.next = None
                    self.tail = prev_node

                #item we want to remove is not an edge case
                else:
                    #make previous node point to next node
                    prev_node.next = current_node.next

                return
            #item has not been found yet advance pointers
            else:
                prev_node = current_node
                current_node = current_node.next

        raise ValueError(f'Item not found: {item}')


def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

#---------------------- Test Prepend
    ll2 = LinkedList()
    print('list: {}'.format(ll2))

    print('\nTesting prepend:')
    for item in ['A', 'B', 'C']:
        print('prepend({!r})'.format(item))
        ll2.prepend(item)
        print('list: {}'.format(ll2))

    print('head: {}'.format(ll2.head))
    print('tail: {}'.format(ll2.tail))
    print('length: {}'.format(ll2.length()))

#----------------------- Test Delete
    delete_implemented = True
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
