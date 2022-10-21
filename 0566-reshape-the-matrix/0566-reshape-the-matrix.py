class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        row=len(mat)
        col=len(mat[0])
        reshaped_mat=[]
        if(row*col)==(r*c):
            temp_1D=[]
            for i in range(row):
                for j in range(col):
                    temp_1D.append(mat[i][j])
            
            m=0;n=0;row_1D=[]
            
            for item in temp_1D:
                if(m<c and m<r*c):
                    row_1D.append(item)
                    m=m+1
                if(m==c):
                    reshaped_mat.append(row_1D)
                    m=0;row_1D=[]
            return reshaped_mat
        return mat
        