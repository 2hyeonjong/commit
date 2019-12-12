# ZIP

### my code
```python
def solution(mylist):
    new_list = [[]*len(mylist) for i in range(len(mylist))]
    print(len(mylist))
    for i in range(len(mylist)):
        for j in range(len(mylist)):
            new_list[i].append( mylist[j][i] )
    return new_list
```

python에서는  
파이썬의 zip과 unpacking 을 이용하면 코드 한 줄로 리스트를 뒤집을 수 있습니다.

```python
mylist = [ [1,2,3], [4,5,6], [7,8,9] ]
new_list = list(map(list, zip(*mylist)))
```
### zip 함수에 대해  
<a href = 'https://docs.python.org/ko/3/library/functions.html?highlight=built%20function'>파이썬 3 한글 번역 - zip</a>에 따르면

zip(*iterables)는 각 iterables 의 요소들을 모으는 이터레이터를 만듭니다.
튜플의 이터레이터를 돌려주는데, i 번째 튜플은 각 인자로 전달된 시퀀스나 이터러블의 i 번째 요소를 포함합니다.

영어 원문:  

Returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables.
```python
mylist = [ 1,2,3 ]
new_list = [ 40, 50, 60 ]
for i in zip(mylist, new_list):
    print (i)

(1, 40)
(2, 50)
(3, 60)
```
### 사용 예 #1 - 여러 개의 Iterable 동시에 순회할 때 사용
```python3
list1 = [1, 2, 3, 4]
list2 = [100, 120, 30, 300]
list3 = [392, 2, 33, 1]
answer = []
for i, j, k in zip(list1, list2, list3):
   print( i + j + k )
```

### 사용 예 #2 - Key 리스트와 Value 리스트로 딕셔너리 생성하기
파이썬의 zip 함수와 dict 생성자를 이용하면 코드 단 한 줄로, 두 리스트를 합쳐 딕셔너리로 만들 수 있습니다.
```python3
animals = ['cat', 'dog', 'lion']
sounds = ['meow', 'woof', 'roar']
answer = dict(zip(animals, sounds)) # {'cat': 'meow', 'dog': 'woof', 'lion': 'roar'}
```

