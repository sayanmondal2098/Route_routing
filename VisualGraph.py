import math
import numpy
import random 


class Node():
    "This is a node creator with 4 probability in w,x,y and z dir ."
    # w ,x,y,z is the probability in each direction connected in graph node
    def __init__(self,nodename,w,x,y,z):
        
        self.w = w
        self.x = x
        self.y = y
        self.z = z
    
    def PrintNode(self):   #print the probability of each dir
        print(self.w,self.x,self.y,self.z)

    def GetW(self):      #Get Probalastic Value of W
        return self.w

    def GetX(self):     #Get Probalastic Value of W
        return self.x

    def GetY(self):    #Get Probalastic Value of W
        return self.y

    def GetZ(self):     #Get Probalastic Value of W
        return self.z

    def SetW(self,W):      #Get Probalastic Value of W
        self.w = W
    
    def SetX(self,X):      #Get Probalastic Value of X
        self.x = X

    def SetY(self,Y):      #Get Probalastic Value of Y
        self.y = Y

    def SetZ(self,Z):      #Get Probalastic Value of Z
        self.z = Z


class Graph:
    #Initilize the each node with 0 probability
    W = 'LOL'
    X = 'LOL'
    Y = 'LOL'
    Z = 'LOL'
    def __init__(self ,nodename=None):
        self.nodename = nodename or []

    def PrintNode(self):   #print the probability of each dir
        print(self.node.w,self.node.x,self.node.y,self.node.z)
        
    def SetW(W):      #Get Probalastic Value of W
        Graph.W = W
              # return self.node.w

    def GetW(self):      #Get Probalastic Value of W
        return self.node.w
    # def PrintNode(self):
    #     print(self.)

Node('Nodename',2,3,4,5).PrintNode()
# print(Node(1,1,1,1).__doc__)


