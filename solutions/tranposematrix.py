import numpy as np
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        new_matrix =  np.array(matrix)
        return new_matrix.transpose()
