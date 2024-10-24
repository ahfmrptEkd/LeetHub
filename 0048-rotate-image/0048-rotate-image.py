class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # 모든 원소를 temp 배열에 저장
        temp = []
        for i in range(n):
            for j in range(n):
                temp.append(matrix[i][j])
        
        # matrix[i][j] = matrix[n-1-j][i] 공식을 사용해서 한번에 변환
        for i in range(n):
            for j in range(n):
                idx = (n-1-j)*n + i  # temp 배열에서의 위치 계산
                matrix[i][j] = temp[idx]