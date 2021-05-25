from models import(
    TriangleSemantic,
    Network
)
'''
a: [3][j] alpha: [0][j] height_c: [7][j]
b: [4][j] beta : [1][j] square  : [6][j]
c: [5][j] delta: [2][j]
'''
# Test create
triangle_semantic = TriangleSemantic()

triangle_semantic.a = 4.0
triangle_semantic.b = 8.0
triangle_semantic.alpha = 30.0

print(triangle_semantic)

# Test Calculate

network = [[0.0 for i in range(5)] for j in range(8)]
network[4][0] = -1
network[1][1], network[2][1], network[4][1], network[5][1] = [-1] * 4
network[3][2], network[4][2], network[5][2], network[6][2] = [-1] * 4
network[0][3], network[1][3], network[2][3] = [-1] * 3
network[5][4], network[6][4], network[7][4] = [-1] * 3
network[0][0], network[1][0], network[3][0] = [1] * 3
