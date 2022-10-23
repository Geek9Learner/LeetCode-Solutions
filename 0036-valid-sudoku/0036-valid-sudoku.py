class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
        checking raw
        '''
        for list_in_list in board:
            seen=set()
            dupes=[]
            for val in list_in_list:
                if val=='.':continue
                if val in seen:dupes.append(val)
                else:seen.add(val)
            if len(dupes)>0:return False
        '''
        checking column
        '''    
        j=0
        while  j<9:
            column=[]
            seen=set()
            dupes=[]
            for list_in_list in board:column.append(list_in_list[j])

            for val in column:
                if val=='.':continue
                if val in seen:dupes.append(val)
                else: seen.add(val)
            if len(dupes)>0:  return False
            j+=1
        del j
        '''
        checking blocks
        '''
        i=0
        while i<9:
            k=0
            while k<9:
                block=[]
                seen=set()
                dupes=[]
                for j in range(0+k,3+k):
                    block.append(board[0+i][j])
                    block.append(board[1+i][j])
                    block.append(board[2+i][j])
                for val in block:
                    if val=='.':continue
                    if val in seen:dupes.append(val)
                    else:seen.add(val)
                if len(dupes)>0:  return False
                k+=3
            i+=3    
        return True