def probability(num,den): 
    return num/den
def matrixEdges(matrx,n):
    edges = dict()
    for i in range(n):
        for j in range(n):
            var = matrix[i][j]
            if var not in edges: edges[var] = []
            if j+1<n: edges[var].append(matrix[i][j+1])
            if i+1<n: edges[var].append(matrix[i+1][j])
    for pt1 in edges:
        den = len(edges[pt1])
        for pt2 in edges[pt1]:
            print(pt1,"-",pt2,"Probability: ", probability(1,den))
    #print(edges)
n = int(input())
matrix = []
val = 1
for i in range(n):
    matrix.append([])
    for _ in range(n):
        matrix[i].append(val)
        val += 1 
matrixEdges(matrix,n)