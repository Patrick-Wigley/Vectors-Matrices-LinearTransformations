from CMLibrary import IdentityMatrix, Matrix, Vector




# Linear Systems
print("# Linear Systems #")
# What is (x, y) if 2x + y = 10 & -2x + 4y = 10?
t = Matrix([
    [2, 1],
    [-2,4]
])
x = Vector([
    10,
    10
])

t.invert()
x *= t
print(x)



# Matrix Checks
print("\n\n# Matrix Checks #")
t1 = Matrix([
    [4,3],
    [3,2]
])

t2 = Matrix([
    [4,3],
    [3,1]
])

t_symmetric = Matrix([
    [2,1],
    [1,2]
])

print(f"{t1} {t2}")
print("t1 equals t1 " if t1 == t2 else "t1 does NOT equal t2")
print("t_symmetric", "is symmetric" if t_symmetric.is_symmetric() else "is NOT symmetric")
print("t1", "is square" if t1.is_square() else "is NOT square")
print("t1 determinant =", t1.get_determinant())



# Matrix Computation
A = Matrix([
    [1,2,1],
    [3,1,1]
])
B = Matrix([
    [2, 4],
    [1, 3],
    [1, 1]
])
D = Matrix([
    [2, 1],
    [-2, 4],
])

# m = A + BT (B Transposed)
print("m =", A + B.transpose(change_state=False)) # NOTE change_state changes instances values by default (if True), otherwise will return value (if False)
# m = A * B-1 (D Inverse)
print("m = ", B * D.invert(change_state=False))


# Vector Check
v1 = Vector([
    1,
    5
])
v2 = Vector([
    3,
    -6
])
print("θ of v1 & v2 (angle) =", v1.get_angle(v2))


# Vector Manipulation
point = Vector([
    -1,
    2
]) 

t = Matrix([
    [3, 0],
    [0, 2]
])

point.multiply_by(t)
point.reflect_x_axis()
point.rotate_anticlockwise(90, False)

print("X* =\n", point)