# n진법으로 표기된 string을 10진법 숫자로 변환하기 - int 함수
  
진법 변환 문제는 알고리즘 문제나 숙제로 자주 나오는 유형이지요. 이번 시간에는 n 진법으로 표기된 문자열을 10진법 숫자로 변환하는 방법을 배워봅시다.

예시) 5진법으로 적힌 문자열 '3212'를 10진법으로 바꾸기

### my code
```python
num, base = map(int, input().strip().split(' '))
# 3212, 10

num = list(map(int, str(num)))
result = 0
index = base **(len(num))
for i in range(len(num)):
    index /= base
    result += num[i]* int(index)
print(result)
```

### better
```python
num = '3212'
base = 5

answer = 0
for idx, i in enumerate(num[::-1]):
    answer += int(i) * ( base ** idx )
```

### best
```python
num = '3212'
base = 5
answer = int(num, base)
```
