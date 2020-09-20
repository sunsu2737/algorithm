from collections import MutableMapping
import math, random

class SkipList(MutableMapping):
    __slots__ = '_head', '_tail', '_n', '_height'

    #------------------------------- nested _Node class -------------------------------
    class _Node:
        __slots__ = '_key', '_value', '_next'

        """Lightweight composite to store key-value pairs as map items."""
        def __init__(self, k, v, height):
            self._key = k
            self._value = v
            self._next = [None] * (height)

        def __eq__(self, other):               
            if other == None:
                return False
            return self._key == other._key   # compare items based on their keys

        def __ne__(self, other):
            return not (self == other)       # opposite of __eq__

        def __lt__(self, other):               
            return self._key < other._key    # compare items based on their keys

    def __init__(self):
        """Create an empty map."""
        self._head = self._Node(-math.inf, None, 1)   # Head: the first node in a skip list
        self._tail = self._Node(math.inf, None, 1)    # Tail: the last node in a skip list
        self._head._next[0] = self._tail         # Initially, there's no item -> head is directly linked to the tail
        self._n = 0                              # Initially, there's no item, so _n = 0
        self._height = 1                         # Initially, the height of a skip list is 1
  
    def __getitem__(self, k, update=None):
        """Return value associated with key k (raise KeyError if not found)."""
   
    def __setitem__(self, k, v):
        """Assign value v to key k, overwriting existing value if present."""
        
    def __delitem__(self, k):
        """Remove item associated with key k (raise KeyError if not found)."""


    def __len__(self):
        """Return number of items in the map."""
        return self._n

    def __iter__(self):                             
        """Generate iteration of the map's keys."""
        # iterate over the base height (=> height = 0)
        node = self._head._next[0]
        while not node is self._tail:
            yield node._key
            node = node._next[0]

    def print_tree(self):
        print('^^^^^^^^^^^^^^^^^^^^^^^^^^')
        node = self._head
        while node != None:
            print('#', end='\t')
            for i in range(self._height):
                lnk = node._next[i]
                
                if node is self._tail:
                    print_val = '+'
                elif lnk == None:
                    print_val = '.'
                elif node._key == -math.inf:
                    print_val = '-'
                elif node._key == math.inf:
                    print_val = '+'
                else:
                    print_val = node._key
                
                print(print_val, end ='\t')
            print()
            node = node._next[0]

        for h in reversed(range(self._height)):
            print(f"At height #{h}, ", end='')
            node = self._head
            while node != None:
                print(node._key, end=' -> ')
                node = node._next[h]
            print()
        print('vvvvvvvvvvvvvvvvvvvvvvvvvv')