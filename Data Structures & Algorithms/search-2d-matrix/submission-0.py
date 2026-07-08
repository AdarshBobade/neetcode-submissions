class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        high = (len(matrix) - 1) # 2
        flag = False
        while low <= high :
            mid = ( high + low)//2
            if matrix[mid][len(matrix)] == target:
                flag = True
                return flag
            elif matrix[mid][len(matrix)] > target :
                high = mid - 1
            else :
                low = mid + 1
        
        if not flag :
            row = low
            high = (len(matrix[0]) - 1)
            low = 0
            while low <= high :
                mid = (high + low)//2
                if matrix[row][mid] == target :
                    flag = True
                    return flag
                elif matrix[row][mid] > target :
                    high = mid - 1
                else :
                    low = mid + 1
        return flag

            



        