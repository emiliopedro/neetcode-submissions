class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool: 
        inf, sup = 0, len(matrix)*len(matrix[0]) - 1

        while inf <= sup:
            mid = (inf + sup) // 2
            r, c = mid // len(matrix[0]), mid % len(matrix[0])


            if matrix[r][c] == target:
                return True
            
            if matrix[r][c] < target:
                inf = mid + 1
            elif matrix[r][c] > target:
                sup = mid - 1
        
        return False
        