class Graph :
    class _Node:
        __slots__ = '_w','_x','_y','_z'

        def __init__(self,w=None,x=None,y=None,z=None):
            self._w = w
            self._x = x
            self._y = y
            self._z = z

    # ,_data=None,_size=None,_font=None,_sourcepos=None,_destination=None
    _size = 0
    def __init__(self):
        self._data = []
    
    def _addNode(self,w,x,y,z):
        # if (self._size)==len(self._data):
        #     self._resize(2*len(self.data))
        # avail = (self._font + self._size)%len(self._data)
        # avail = self._size
        self._data.append(self._Node(w,x,y,z))
        self._size += 1

    def _getLength(self):
        return self._size


G = Graph()
G._addNode(1,1,1,1)

G._addNode(1,1,1,1)

print(G._getLength())