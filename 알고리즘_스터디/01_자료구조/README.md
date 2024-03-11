# 자료구조
> - Array
> - Stack
> - Queue
> - Priority_Queue
> - Map
> - Set
## 배열(Array)

### 시간복잡도

- 삽입/삭제 : O(N)
- 탐색 : O(1)

→ 탐색이 더 빠르다

```python
# 탐색

arr = [1, 2, 3, 4, 5]
arr[2] = 5
# arr + 2*4byte(int) => 메모리 주소값을 계산하여 바로 탐색
# 이를 임의접근 : random access 이라 함 
# arr[n]를 찾기위해 [0], [1], ... [n]을 거치는 것이 아님
```

```python
# 삽입

arr = [1, 2, 3, 4, 5]
# 2와 3 사이에 6을 넣고 싶은 경우
# 2 뒤의 3, 4, 5의 값을 하나씩 뒤로 미뤄야함
# 즉 최소 0개~N개까지의 미루어야 하는 값이 생김 : O(N)
```

## 백터(Vector)

- 삽입/삭제 : O(N)
- 탐색 : O(1)
- 동적배열

주로 C++에 사용, python에서는 numpy 를 통해 벡터를 나타냄 

## 연결 리스트(Linked List)

배열과 성격이 반대 (삽입/삭제가 빠르다)

- 삽입/삭제 : O(1)
- 탐색 : O(N)
- PS(알고리즘풀이)에서는 별로 안쓰이지만 다른 자료구조 구현시 사용

여러개의 노드로 구성, 노드는 데이터와 링크로 구성

- 데이터 : 자신이 가진 값
- 링크 : 다음 노드의 위치 값

## 스택(Stack)

- FILO, LIFO구조 (first in last out, last in first out)
    - 첫 번째 들어온 데이터가 가장 마지막에 나옴
    - 마지막에 들어온 데이터가 가장 먼저 나옴
- 삽입/삭제 : O(N)

stack 구현 : 웹 브라우저의 뒤로가기 

## 큐(Queue)

스택과 반대

- FIFO, LILO구조 (선입선출, 후입후출)
- 삽입/삭제 : O(1)
    - 연결리스트를 사용하여 구현

```python
# 큐 역할을 수행할 수 있는 모듈 deque
from collections import deque

dq = deque()
dq.append(123) # 마지막에 추가 
dq.appendleft(456) # 맨 앞에 추가

dq.pop() # 마지막 값 출력
dq.popleft() # 맨 앞값 출력 
```

## 우선순위 큐(Priority Queue : Heap)

우선순위가 높은 데이터가 먼저 나가는 형태 : Heap을 이용하여 구현

- 삽입/삭제 : O(logN)

### Heap

완전 이진트리로 구성, 부모-서브 노드간의 대소관계 성립

- 루트노드에 가장 큰 값이 위치(max heap) : C++
    ![alt text](image.png)
    
- 루트노드에 가장 큰 작은이 위치(min heap) : Python
    ![alt text](image-1.png)
    

```python
import heapq

pq = []
heapq.heappush(pq, 1)
heapq.heappush(pq, 5)
heapq.heappush(pq, 3)

print(pq)
# 1, 3, 5 -> 자동으로 작은순으로 출력
while pq:
	heapq.heappop(pq) # 작은값 부터 출력 
```

## 맵 Map(Dictionary)

- Key, Value 로 이루어짐
    - Key는 중복이 불가능
- 삽입/삭제 : O(1)

## 집합 Set

map과 유사 

- 중복x
- 삽입/삭제 : O(1)

```python
# set함수 사용
s = set()
s.add(1)
s.add(2) 
s.add(2) 
print(s) # {1, 2} : 값 중복 x

s.pop() # 임의의 랜덤 값이 제거됨 (잘 사용하지 않음)
s.remove(1) # 원하는 값이 제거
```