class Graph :
    class _Node:
        __slots__ = '_w','_x','_y','_z'

        def __init__(self,w=None,x=None,y=None,z=None):
            self._w = w
            self._x = x
            self._y = y
            self._z = z

        def _getallNodeAttributes(self):
            return (self._w,self._x,self._y,self._z)

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

    def _getFirst(self):
        return self._data[0]
    
    def _getAllNodes(self):
        for i in range(0,2):
            print(self._data[i]._getallNodeAttributes())


G = Graph()              
G._addNode(1,1,1,1)

G._addNode(1,1,1,1)

print(G._getLength())
print(G._getAllNodes())