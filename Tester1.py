def probability(num,den): 
    return num/den
def matrixEdges(matrx,n):
    edges = dict()
    mylist = []
    for i in range(n):
        for j in range(n):
            var = matrix[i][j]
            if var not in edges: edges[var] = []
            if i-1>=0: edges[var].append(matrix[i-1][j])
            if i+1<n: edges[var].append(matrix[i+1][j])
            if j-1>=0: edges[var].append(matrix[i][j-1])
            if j+1<n: edges[var].append(matrix[i][j+1])
    for pt1 in edges:
        den = len(edges[pt1])
        
        for pt2 in edges[pt1]:
            print(pt1,"-",pt2,"Probability: ", probability(1,den))
            pp = (pt1,pt2)
            mylist.append(pp)
            
    # print(edges)
    print(mylist)

n = int(input())
matrix = []
val = 1
for i in range(n):
    matrix.append([])
    for _ in range(n):
        matrix[i].append(val)
        val += 1 
matrixEdges(matrix,n)