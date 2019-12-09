# QUEUE

<ui>
  <li>줄을 서는 행위와 비슷</li>
  <li>가장 먼저 넣은 데이터를 가장 먼저 꺼낼 수 있는 구조</li> 
</ui><br />  
<ui>
  <li>Enqueue : 큐에 데이터를 넣는 기능 </li>
  <li>Dequeue : 큐에서 데이터를 꺼내는 기능</li>
</ui>

## 파이썬 queue 라이브러리 활용해서 큐 자료 구조 사용하기
<li>Queue(): 가장 일반적인 큐 자료 구조</li>
<li>LifoQueue(): 나중에 입력된 데이터가 먼저 출력되는 구조 (스택과 유사 방식)</li>
<li>PriorityQueue(): 데이터마다 우선순위를 넣어서, 우선순위가 높은 순으로 데이터 출력</li>

### Queue()로 큐 만들기 (가장 일반적인 큐, FIFO(First-In, First-Out))

```python
# 큐 만들기
import queue  
data_queue = queue.Queue()

# 데이터 넣기
data_queue.put("korea")  
data_queue.put(1)

# 큐 사이즈 확인하기
data_queue.qsize()  
2

# 데이터 꺼내기
data_queue.get()
'korea'

# 데이터 꺼내지면 큐 사이즈도 줄어듬
data_queue.qsize()
1

data_queue.get()
1
```

### LifoQueue()로 큐 만들기 (LILO(Last-In, Last-Out))
```python
# LifoQueue 만들기
import queue
data_queue = queue.LifoQueue()

# 데이터 넣기
data_queue.put("korea")
data_queue.put(1)

# 데이터 꺼내기
data_queue.get()
1
```

### PriorityQueue()로 큐 만들기
```python
# LifoQueue 만들기
import queue
data_queue = queue.PriorityQueue()

# 데이터 넣기
data_queue.put((10, "korea"))           # <-- (우선순위, 데이터) 형식의 튜플로 넣어야 함
data_queue.put((5, 1))                  # <-- (우선순위, 데이터) 형식의 튜플로 넣어야 함 
data_queue.put((15, "china"))           # <-- (우선순위, 데이터) 형식의 튜플로 넣어야 함

# 데이터 꺼내기 
data_queue.get()                        # <-- 우선순위값이 가장 낮은 데이터 순으로 출력 (1순위가 2순위보다 우선순위가 높죠!)
(5, 1)

# 데이터 꺼내기
data_queue.get()
(10, 'korea')

```
