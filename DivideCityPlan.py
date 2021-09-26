def find_parent(parent, x): # 특정원소 집합을 찾기
    if parent[x] != x: # 루트노드가 아니면
        parent[x] = find_parent(parent, parent[x]) # 루트노드를 찾을 때 까지 재귀적으로 호출
    return parent[x]

def union_parent(parent, a, b): # 두 원소의 합
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b : # a < b 루트값이 작으면
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split()) # 노드및 간선의 정보를 입력
parent = [0] * (v+1) # 부모 테이블 초기화

edges = [] # 모든 간선을 담을 리스트
result = 0 # 최종비용 결과값

for i in range(1, v+1): # 부모 테이블에서
    parent[i] = i # 자기자신으로 초기화

for _ in range(e): # 모든 간선의 정보를 입력
    a, b, cost = map(int, input().split())
    edges.append((cost,a,b)) # 비용값으로 정렬하기 위해서 튜플중 첫번째 원소를 비용값으로 설정

edges.sort() # 비용순으로 정렬
last = 0 # 최소 신장트리를 만족하는 것 중에서 가장 큰 간선

for edge in edges: # 모든 간선을 하나씩 확인하면서
    cost, a, b = edge

    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        last = cost

print(result-last)