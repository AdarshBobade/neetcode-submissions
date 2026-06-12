class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hash_rows = [set() for _ in range(9)]
        hash_columns = [set() for _ in range(9)]
        hash_boxes = [set() for _ in range(9)]
        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num == ".":
                    continue
                if num in hash_rows[r]:
                    return False
                hash_rows[r].add(num)
                
                if num in hash_columns[c]:
                    return False
                hash_columns[c].add(num)

                box_i  = (r//3)*3 + c//3
                if num in hash_boxes[box_i]:
                    return False
                hash_boxes[box_i].add(num)
        return True



        