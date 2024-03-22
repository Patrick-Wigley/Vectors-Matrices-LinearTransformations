import math

CLOCKWISE = 0
ANTI_CLOCKWISE = 1

class DataStructure:
    """ Parent Class - Vector & Matrix have some similarities such as how two vecs or two
     mats are multiplied together or subtracted, added etc """
    def __init__(self, values):
        self.__values = values # TODO: Put similar functions from Matrix & Vector here and use parent class



class Vector():
    def __init__(self, values):
        self.__values = values
        
    def __str__(self):
        ret = ""
        for row in self.__values:
            ret += "| " + str(row).strip("[").strip("]") + " | \n"
        return ret

    def get_values(self):
        return self.__values

    def multiply_by(self, other, change_state=True):
        new_vec = []
        
        if isinstance(other, Matrix):
            for row_index in range(len(self.__values)):
                mat_columns = other.get_values()[row_index]
                result = sum( [mat_val*self.__values[i] for i, mat_val in enumerate(mat_columns)] )
                new_vec.append(result)
        elif isinstance(other, Vector):
            for index, val in enumerate(self.__values):
                new_vec.append(val * other.get_values()[index])
        else:
            print("Not vector or matrix?")
            return None

        if change_state:
            self.__values = new_vec
        else:
            return new_vec    
        
    def multiply_by_scalar(self, scalar, change_state=True):
        new_vec = []
        for val in self.__values:
            new_vec.append(val * scalar)

        if change_state:
            self.__values = new_vec
        else:
            return new_vec

    def angle(self, other):
        if isinstance(other, Vector):
            a_magnitude = self.get_magnitude()
            b_magnitude = other.get_magnitude()
            # Multiply vectors

    def rotate_clockwise(self, angle, change_state=True):
        ret = self.__rotate(angle, CLOCKWISE)
        if not change_state:
            return ret

    def rotate_anticlockwise(self, angle, change_state=True):
        ret = self.__rotate(angle, ANTI_CLOCKWISE)
        if not change_state:
            return ret

    def __rotate(self, angle, direction, change_state=True):
        rotation_matrix = None
        angle = degree_to_radian(angle)
        if direction == CLOCKWISE:
            rotation_matrix = Matrix([
                [math.cos(angle), math.sin(angle)],
                [-math.sin(angle), math.cos(angle)]
            ])
        elif direction == ANTI_CLOCKWISE:
            # Anti Clockwise
            rotation_matrix = Matrix([
                [math.cos(angle), -math.sin(angle)],
                [math.sin(angle), math.cos(angle)]
            ])
        else:
            print("[ERROR]: 'direction' parameter must be a representive value")
            return

        if change_state:
            self.multiply_by(rotation_matrix)
        else:
            return self.multiply_by(rotation_matrix, change_state=change_state)

    def get_magnitude(self):
        """ Pythagorean theorem """
        return math.sqrt( sum( [(val*val) for val in self.__values] ) )

    def reflect_x_axis(self):
        if len(self.__values) == 2:
            self.__values = [self.__values[0], -self.__values[1]]
    def reflect_y_axis(self):
        if len(self.__values) == 2:
            self.__values = [-self.__values[0], self.__values[1]]
    def reflect_x_line(self):
        if len(self.__values) == 2:
            self.__values = [self.__values[1], self.__values[0]]
    def reflect_negative_x_line(self):
        if len(self.__values) == 2:
            self.__values = [-self.__values[1], -self.__values[0]]

    def __mul__(self, other):
        if isinstance(other, (Vector, Matrix)):
            return Vector(self.multiply_by(other, change_state=False))
        elif isinstance(other, (float, int)):
            return Vector(self.multiply_by_scalar(other, change_state=False))




class Matrix():
    def __init__(self, values):
        self.__values = values
     

    def __str__(self):
        ret = f"{len(self.__values)}x{1 if isinstance(self.__values[0], (int, float)) else len(self.__values[0]) }:\n" # NOTE: Fix sizing issue/inconsistency (error if calling len(self.__values[0]) with matrices that are size n by 1)
        for row in self.__values:
            ret += "| " + (str(row).strip("[").strip("]") + " | \n")
        return ret
    
    def get_values(self):
        return self.__values

    def get_size(self):
        """ Col x Row """
        return [ len(self.__values), len(self.__values[0]) ]


    def transpose(self, change_state=True):
        values_t = []

        for i in range(len(self.__values[0])):
            row = []
            for j in range(len(self.__values)):
                row.append(self.__values[j][i])
            values_t.append(row)
        
        if change_state:
            self.__values = values_t
        else:
            return Matrix(values_t)
        
    def is_symmetric(self) -> bool:
        values_t = self.transpose(change_state=False)
        return values_t == self.__values

    def subtract(self, other_matrix):
        self.__sequentially_update_components(lambda a, b: a - b, other_matrix)

    def add(self, other_matrix):
        self.__sequentially_update_components(lambda a, b: a + b, other_matrix)
        
    def multiply(self,
                 other_matrix = None, 
                 scalar = None):
        """ Multiply Matrix by another matrix or a scalar """
        if other_matrix:
            self.__dot_product(other_matrix)
        elif scalar:
            self.__sequentially_update_components_scalar(lambda a, s: a * s, scalar)
    
    def invert(self, change_state=True):
        """ Set matrix to its inversed value """
        # |self| = det(self)
        # [a, b] -> [d, -b] -> (1 / |self|) * [d, -b]
        # [c, d] -> [-c, a] ->                [-c, a]
        
        # Simple 2D invert for now
        distrubutive_val = 1 / self.get_determinant()
        new_mat = [
            [distrubutive_val * self.__values[1][1], distrubutive_val * -self.__values[0][1]],
            [distrubutive_val * -self.__values[1][0], distrubutive_val * self.__values[0][0]]
            ]
        if change_state:
            self.__values = new_mat
        else:
            return Matrix(new_mat)

    def get_determinant(self) -> int:
        """ Must be a square matrix """
        if self.is_square():
            if len(self.__values[0]) % 2 != 0:
                # Using sarrus rule for 3D Matrices (Uneven)
                # for i in range(2):
                #     for col in range(self.__values[0]): 
                
                values_1 = [] 
                values_2 = []
                for col in range(len(self.__values[0])): 
                    values_1.append(self.__determinant_recursive(lambda a: a+1, col))
                
                for col in reversed(range(len(self.__values[0]))):
                    values_2.append(self.__determinant_recursive(lambda a: a-1, col))
                
                return sum(values_1) - sum(values_2)
            else:
                # Simple method for 2D Matrices
                a = self.__determinant_recursive(lambda a: a+1, 0)
                b = self.__determinant_recursive(lambda a: a-1, len(self.__values[0])-1) 
                return a - b
        else:
            print("Must be a square Matrix to calculate determinant!")
    
    def get_eigenvalues(self) -> int:
        pass # Complete

    def __determinant_recursive(self, traverse_method, col_index, row_index=0, counter=0):
        """ Returns product of values across diagonal axis for each column - (Following the Sarrus example) """
        if counter == len(self.__values)-1:
            return self.__values[row_index][col_index % len(self.__values[0])]
        
        # col_index % len(values) will allow for the overflow values which are required with sarrus rule
        return self.__values[row_index][col_index % len(self.__values[0])] * self.__determinant_recursive(traverse_method, col_index+1, traverse_method(row_index), counter=counter+1)

    def __dot_product(self, other, change_state=True):
        # Makes computation simpler when B transpose (Personally I found this to be the case)
        other = other.transpose(change_state=False)
        if len(self.__values[0]) == len(other.get_values()[0]):
            new_mat = []
            # Dot Product Method (Multiplying Matrices)
            #     Other [2 4]
            #           [1 3] 
            # self [1 2][4 10]   [1*2+2*1, 1*4+2*3]
            #      [3 1][7 15]   [3*2+1*1, 3*4+1*3]

            other_matrix_values = other.get_values()
            for row in range(len(self.__values)):
                columns = []
                for col in range(len(other_matrix_values)):
                    columns.append(self.__multiply_recursive(a_row = self.__values[row],  b_col = other_matrix_values[col]))
                new_mat.append(columns)

            if change_state:
                self.__values = new_mat
            else:
                return new_mat
            
        else:
            print("[ERROR]: Matrices are not suitable size for multiplication!")

    def __multiply_recursive(self, a_row, b_col):
        return a_row[0]*b_col[0] + self.__multiply_recursive(a_row[1:], b_col[1:]) \
        if len(a_row) != 0 \
        else 0

    def __sequentially_update_components(self, method, other_matrix, change_state=True):
        """ Called inside class for addition & subtraction like behaviour """
        new_matrix = []

        for row in range(self.get_size()):
            columns = []
            for col in range(self.get_size()):
                columns.append(method(self.__values[row][col], other_matrix.get_values()[row][col]))
            new_matrix.append(columns)
        if change_state:
            self.__values = new_matrix
        else:
            return new_matrix

    def __sequentially_update_components_scalar(self, method, scalar, change_state=True):
        """ Called inside class for addition & subtraction like behaviour """
        new_matrix = []

        for row in range(self.get_size()):
            columns = []
            for col in range(self.get_size()):
                columns.append(method(self.__values[row][col], scalar))
            new_matrix.append(columns)
 
        if change_state:
            self.__values = new_matrix
        else:
            return new_matrix

    def __eq__(self, other) -> bool:
        if isinstance(other, Matrix):
            return self.__values == other.get_values() 

    def __mul__(self, other):
        if isinstance(other, Matrix):
            return Matrix(self.__dot_product(other, change_state=False))
        elif isinstance(other, (int, float)):
            return Matrix(self.__sequentially_update_components_scalar(lambda a, s: a * s, other, change_state=False))
        elif isinstance(other, Vector):
            pass

    def __add__(self, other):
        return Matrix(self.__sequentially_update_components(lambda a, b: a + b, other, change_state=False))

    def __sub__(self, other):
        return Matrix(self.__sequentially_update_components(lambda a, b: a - b, other, change_state=False))

    def is_square(self) -> bool:
        """ Determines if matrix is equal in rows & columns e.g. 2x2 """
        return len(self.__values) == len(self.__values[0])

class IdentityMatrix(Matrix):
    def __init__(self, size):
        values = []
        for row in range(size):
            columns = [0 for _ in range(size)]
            columns[row] = 1
            values.append( columns )

        super().__init__(values)



def radian_to_degree(radian) -> float:
    return radian * (180/math.pi)
def degree_to_radian(degree) -> float:
    return degree * (math.pi/180)