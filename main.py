from Matrix import IdentityMatrix, Matrix, Vector




# Linear Systems
# What is (x, y) if 2x + y = 10 & -2x + 4y = 10?
mat = Matrix([
    [2, 1],
    [-2,4]
])
results = Vector([
    10,
    10
])

mat.invert()
results *= mat
print(results)

mat = Matrix([
    [0.4, 0.4],
    [0.6, -.8]
])
results = Vector([
    3.6,
    -1.6
])

mat.invert()
results *= mat
print(results)



a = Matrix([
    [4,3],
    [3,2]
])

b = Matrix([
    [4,3],
    [3,1]
])

d = Matrix([
    [2,1],
    [-2,4]
])
d.invert()
print(d)


print("a equals b " if a == b else "a doesn't equal b")



mat4 = Matrix([
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ])

det_example = Matrix([
    [2,3,1],
    [1,1,1],
    [2,2,1]
])

det_example2 = Matrix([
    [1,0,0],
    [0,2,-2],
    [0,4,7]
])

det_example3 = Matrix([
    [2,3],
    [1,4]
])

det_test_2d = Matrix([
    [2,1],
    [-2,4],
    [2,2]
])

print(det_test_2d.get_determinant())


symmetric_mat = Matrix([
    [0,1],
    [1,0]
])
print(symmetric_mat.is_symmetric())


A = Matrix([
    [1,2,1],
    [3,1,1]
])
B = Matrix([
    [2, 4],
    [1, 3],
    [1, 1]
])

A *= B
print(A)