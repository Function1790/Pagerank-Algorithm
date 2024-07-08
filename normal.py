import numpy as np
import matplotlib.pyplot as plt

def probabilityMatrix(martix: np.array):
    A = martix.copy()
    length = len(A)
    for i in range(length):
        total = 0
        # 다른 노드로 갈 수 있는 링크의 갯수 합하기
        for j in range(length):
            total += A[j][i]

        # 확률값 = 1 / (다른 노드로 연결된 링크의 갯수)
        value = 1 / total
        if total == 0: # irrducible 조건 만족
            # 한 노드에서 다른 노드로 갈 수 없다면
            # 가중치가 그 노드에 집중되는 현상이 일어남
            # -> 열의 모든 값 = 1 / 전체노드 갯수
            value = 1 / length
            for j in range(length):
                A[j][i] = value
                continue
        for j in range(length):
            # 현재 노드(i)에서 j노드로 갔을때만 확률값 대입
            if A[j][i]!=0:
                A[j][i] = value

    return A


def convergeRankscore(martix: np.array, count):
    length = len(martix)
    X = 1 / length * np.ones((length, 1))
    #record = []
    for i in range(count):
        X = martix @ X
    #    record.append(sum(X))
    #plt.plot(record)
    #plt.show()
    return X


# 열 -> 행
# 인접행렬(adjacency matrix)
A = np.array(
    [  # A  B  C  D  E
        [0, 1, 1, 1, 0],
        [1, 0, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0.0],
    ]
)

# 확률행렬
H = probabilityMatrix(A)

# Google 행렬
# 값이 수렴하지 않고 진동할 수 있음
# -> Random web surfer 적용
# -> 제동 계수를 활용하여 낮은 가중치로 연결
length = len(A)
d = 0.85  # 제동계수
lowWeights = np.ones((length, length))
G = d * H + (1 - d) / length * lowWeights

# 한 값으로 rankscore 수렴시키기
X = convergeRankscore(G, 100)
result={"ABCDE"[i]:X[i][0] for i in range(length)}
result=sorted(result.items(), key = lambda item: item[1], reverse = True)
[print(result[i][0],result[i][1]) for i in range(length)]