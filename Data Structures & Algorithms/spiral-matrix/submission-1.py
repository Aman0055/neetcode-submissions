class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        top , buttom = 0 , len(matrix) -1
        left , right = 0, len(matrix[0]) -1
        result : list[int] = []

        while top <= buttom and left <= right:
            for j in range(left, right +1):
                result.append(matrix[top][j])
            top += 1

            for i in range(top , buttom + 1):
                result.append(matrix[i][right])
            right -= 1

            if top <= buttom:
                for j in range(right, left -1 , -1):
                    result.append(matrix[buttom][j])
                buttom -= 1
            
            if left <= right:
                for i in range(buttom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1
            
        return result
