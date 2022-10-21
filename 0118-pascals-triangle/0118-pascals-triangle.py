class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal_triangle=[]
        for row in range(1,numRows+1):
            temp=[];adding=[]
            if(row==1):
                pascal_triangle.append([1])
            elif(row==2):
                pascal_triangle.append([1,1])
                
            else:
                adding=pascal_triangle[len(pascal_triangle)-1]
                n=row-2
                temp.append(1)
                for j in range(n):
                    temp.append(adding[j]+adding[j+1])
                temp.append(1)
                pascal_triangle.append(temp)
        return pascal_triangle