# 이진탐색 Binary Search

1차원 배열에서 for문을 통해 찾고자 하는 값을 찾을 때.  
- 모든 요소를 확인해야함.
- 이때 **이진탐색**을 통해 빠르게 찾을 수 있다.  

정렬된 배열을 반씩 나누어 찾고자하는 값의 알파벳과 비교.
- 범위를 나누어 찾기때문에 시간이 절약

## 이진탐색 구현
- 탐색 전에 반드시 **정렬**되어 있어야 한다.
- 살펴보는 범위를 **절반 씩 줄여가며** 답을 찾는다.  
- 정렬$O(NlogN)$ + 이진탐색$O(logN)$ : 결과적으로 $O(NlogN)$
- 미리 정렬된 경우 : 이진탐색만 하면 되므로 $O(logN)$
```python
# 배열에서 특정 수의 갯수를 출력

from bisect import bisect_left, bisect_right
#bisect_left : 배열에서 찾는 값 이상인 위치를 반환
#bisect_right : 배열에서 찾는 값 초과인 위치를 반환

v = (0, 1, 3, 3, 6, 6, 6, 7, 8, 8, 9)
three = bisect_right(v, 3) - bisect_left(v, 3) # 4 - 2
four = bisect_right(v, 4) - bisect_left(v, 4) # 4 - 4
six = bisect_right(v, 6) - bisect_left(v, 6) # 7 - 4

print(f'number of 3: {three}') # 2
print(f'number of 4: {four}') # 0
print(f'number of 6: {six}') # 3
```

# 매개변수 탐색 Parametric Search

- **최적화 문제**를 **결정 문제**로 바꿔 이진탐색으로 푸는 방법

    - 최적화 문제 : 문제 상황을 만족하는 변수의 최소, 최대를 구하는 문제
    - 결정문제 : Yes/No problem