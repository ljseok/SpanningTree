def find_parent(parent, x): # 특정 원소가 속한 집합 찾기
    if parent[x] !=x: # 루트노드가 아니라면
        parent[x] = find_parent(parent, parent[x]) # 루트 노드를 찾을 때 까지 재귀적으로 호출

def union_parent(parent, a, b) : # 두 원소 합치기
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b: # a보다 b의 루트값이 더 크다면
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split()) # v = 노드의 갯수 , e = 간선의 갯수 입력 받기



