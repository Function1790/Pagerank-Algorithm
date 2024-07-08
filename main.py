import numpy as np
import matplotlib.pyplot as plt

def probabilityMatrix(matrix: np.array):
    A = matrix.copy()
    length = len(A)
    for i in range(length):
        total = 0
        for j in range(length):
            total += A[j][i]

        value = 1 / total
        if total == 0:
            value = 1 / length
            for j in range(length):
                A[j][i] = value
                continue
        for j in range(length):
            if A[j][i] != 0:
                A[j][i] = value

    return A

def convergeRankscore(matrix: np.array, count):
    length = len(matrix)
    X = 1 / length * np.ones((length, 1))
    record = []
    for i in range(count):
        X = matrix @ X
        record.append(sum(X[0]))
    return X

def create_adjacency_matrix(products, connections):
    length = len(products)
    A = np.zeros((length, length))
    for (i, j) in connections:
        A[i][j] = 1
    return A

def get_product_index(products, product_name):
    if product_name in products:
        return products.index(product_name)
    else:
        products.append(product_name)
        return len(products) - 1

# 사용자 입력을 통한 상품 및 연결 추가
products = ["A", "B", "C", "D"]
connections = []

while True:
    print("상품을 추가하려면 'A', 연결을 추가하려면 'C', 계산을 시작하려면 'S', 종료하려면 'Q'를 입력하세요:")
    user_input = input().strip().upper()
    
    if user_input == 'A':
        product_name = input("추가할 상품 이름을 입력하세요: ").strip()
        get_product_index(products, product_name)
        print(f"상품 '{product_name}'이(가) 추가되었습니다.")
    
    elif user_input == 'C':
        product1 = input("첫 번째 상품 이름을 입력하세요: ").strip()
        product2 = input("연결할 두 번째 상품 이름을 입력하세요: ").strip()
        
        index1 = get_product_index(products, product1)
        index2 = get_product_index(products, product2)
        
        connections.append((index1, index2))
        print(f"상품 '{product1}'와(과) '{product2}'의 연결이 추가되었습니다.")
    
    elif user_input == 'S':
        if len(products) == 0:
            print("계산할 상품이 없습니다. 상품을 추가해주세요.")
            continue
        A = create_adjacency_matrix(products, connections)
        H = probabilityMatrix(A)
        length = len(A)
        d = 0.85
        E = np.ones((length, length)) / length
        G = d * H + (1 - d) * E
        X = convergeRankscore(G, 100)
        result = {products[i]: X[i][0] for i in range(length)}
        result = sorted(result.items(), key=lambda item: item[1], reverse=True)
        print("상품 추천 점수:")
        for item in result:
            print(f"{item[0]}: {item[1]:.4f}")
    
    elif user_input == 'Q':
        print("프로그램을 종료합니다.")
        break
    
    elif user_input == "P":
        print(create_adjacency_matrix(products, connections))
    
    else:
        print("잘못된 입력입니다. 다시 시도해주세요.")
    print("")