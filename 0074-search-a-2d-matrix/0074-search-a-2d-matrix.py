class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l=0
        for item in matrix:
            if(target in item):
                return True
            if(target not in item and target<item[len(item)-1]):
                return False
        return False