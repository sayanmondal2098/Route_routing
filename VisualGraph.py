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
        self._data = [None]*10
        # self._size = 0
        self._font = 0
        self._sourcepos = 0
        self._destination = 0
    
    def _addNode(self,w,x,y,z):
        # if (self._size)==len(self._data):
        #     self._resize(2*len(self.data))
        # avail = (self._font + self._size)%len(self._data)
        # avail = self._size
        self._data[0] = self._Node(w,x,y,z)
        self._size += 1

    def _getLength(self):
        return self._size

    def _resize(self,cap):
        old = self._data
        self._data = [None]*cap
        walk = self._font
        for k in range(self._size):
            self._data[k]=old[walk]
            walk = (1+walk)%len(old)
            self._font = 0


Graph._addNode(1,1,1,1,1)

Graph._addNode(1,1,1,1,1)

print(Graph._getLength())