from Matrix import IdentityMatrix, Matrix, Vector, \
ANTI_CLOCKWISE, CLOCKWISE



a = Vector([1,2,3])
b = Vector([1,1,1])
c = Vector([1,1,2])
print((a * 3) - (b*2) + (c * 4))




T = Matrix([
    [1,
    -1]
])
T2 = Matrix([
    [1,
    -2]
])

print(T*T2)




a = Vector([
    3,
    1
])

print(a*T)

A = Matrix([
    [1,-2],
    [4,3]
])

B = Matrix([
    [3,0],
    [0,2]
])

x = Vector([
    -1,
    2
])
x.multiply_by_matrix(B)
x.reflect_x_axis()
x.rotate(ANTI_CLOCKWISE, 90)

print(x)





# C = Matrix([
#     [2,1],
#     [3,-2]
# ])
# D = Matrix([
#     [-1,2],
#     [3,-4]
# ])

#print((A * -2) - (C*3) + (D * 2))


###############
