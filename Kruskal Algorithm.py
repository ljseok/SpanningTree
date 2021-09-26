def find_parent(parent, x): # 특정 원소가 속한 집합 찾기
    if parent[x] !=x: # 루트노드가 아니라면
        parent[x] = find_parent(parent, parent[x]) # 루트 노드를 찾을 때 까지 재귀적으로 호출
    return parent[x]

def union_parent(parent, a, b) : # 두 원소 합치기
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b: # a보다 b의 루트값이 더 크다면
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split()) # v = 노드의 갯수 , e = 간선의 갯수 입력 받기
parent = [0] * (v+1) # 부모 테이블 초기화

edges = [] # 간선리스트
result = 0 # 최종비용을 0으로 초기화

for i in range(1, v+1): # 부모 테이블에서
    parent[i] = i # 자기자신으로 초기화

for _ in range(e):
    a,b,cost = map(int,input().split()) # 모든 간선의 정보를 입력받기
    edges.append((cost,a,b)) # 비용순으로 정렬하기 위해서 첫 번재 원소를 비용으로 설정한다

edges.sort() # 간선을 비용순으로 정렬

for edge in edges: # 간선을 확인한다
    cost, a, b = edge

    if find_parent(parent,a) != find_parent(parent, b): # 사이클이 발생하지 않는 경우
        union_parent(parent, a, b) # 집합에 포함
        result+= cost

print(result)



