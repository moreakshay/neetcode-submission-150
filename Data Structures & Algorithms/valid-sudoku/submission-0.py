class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = set()
        col_set = set()
        box_set = set()

        for row_idx, row in enumerate(board):
            for col_idx, col in enumerate(row):
                if col == ".":
                    continue
                row_element = f"row-{row_idx}|val-{col}|"
                col_element = f"col-{col_idx}|val-{col}|"
                box_element = f"box-{int(row_idx/3)},{int(col_idx/3)}|val-{col}|"
                
                if row_element in row_set or col_element in col_set or box_element in box_set:
                    return False

                row_set.add(row_element)
                col_set.add(col_element)
                box_set.add(box_element)
        
        return True

        