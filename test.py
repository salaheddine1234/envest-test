class Matrix(object):
    """
    Classe pour représenter une matrice et réaliser les opérations de base :
    addition, soustraction, multiplication et calcul du déterminant.
    """
    def __init__(self, matrice):
        self.matrice = matrice
        self.rows = len(matrice)
        self.cols = len(matrice[0])
    
    def addition(self, mat2):
        addition = []
        for i in range(self.rows):
            rows = []
            for j in range(self.cols):
                rows.append(self.matrice[i][j] + mat2.matrice[i][j])
                addition.append(rows)
                return Matrix(addition)
            
    def soustraction(self, mat2):
        addition = []
        for i in range(self.rows):
            rows = []
            for j in range(self.cols):
                rows.append(self.matrice[i][j] - mat2.matrice[i][j])
                addition.append(rows)
                return Matrix(addition)
            
    
    def multiplication(self, mat2):
        l=[]
        multiplication = []
        for i in range(self.rows):
            for j in range(mat2.cols):
                s = 0
                for k in range(self.cols):
                    s += self.matrice[i][k] * mat2.matrice[k][j]
                    l.append(s)
                    multiplication.append(l)
        return Matrix(multiplication)
    
    def determinant(self, mat):
        n = len(mat)
        if n==1:
            return mat[0][0]
        if n == 2:
            return mat[0][0]* mat[1][1] - mat[0][1]*mat[1][0]
        det = 0
        for col in range(n):
            signe = (-1)**col
            tranque = self.tranc(mat, 0, col)
            det += signe*mat[0][col] * self.determinant(tranque)
        return det
        
    
    def tranc(self, mat, row, col):
        tranc = []
        for i in range(len(mat)):
            if i != row:
                new_row = []
                for j in range(len(mat[i])):
                    if j!= col:
                        new_row.append(mat[i][j])

                tranc.append(new_row)
        return tranc
        
    def det(self):
        return self.determinant(self.matrice)

    def show(self):
        for row in self.matrice:
            print(row)



    # 1. initialize a matrix: ex.mat = Matrix([[1,2,3],[1,2,3]])

    # 2. realize the basic operation add: ex. mat1 + mat2 = mat3

    # 3. calculate the determinant of a matrix: ex. mat.det


if __name__ == '__main__':
    # Example

    # Test for #1
    mat1 = Matrix([[1,2,3],[1,4,3],[1,4,4]])

    # Test for #2
    mat2 = Matrix([[1,2,3],[1,4,3],[1,4,4]])
    mat3 = mat1.addition(mat2).show()

    mat4 = mat1.soustraction(mat2).show()
    

    #mat5= mat1.multiplication(mat2).show()


    # Test for #3
    mat1.det()
    # print(mat3)
    
