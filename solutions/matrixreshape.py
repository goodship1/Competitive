import numpy as np
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        new_mat = np.array(mat)
        try:
            new_mat = new_mat.reshape(r,c)
            return new_mat
        except ValueError:
            return mat
        
