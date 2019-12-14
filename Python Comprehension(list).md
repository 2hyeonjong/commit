## 1. Python Comprehension
Python의 Comprehension은 한 Sequence가 다른 Sequence (Iterable Object)로부터 (변형되어) 구축될 수 있게한 기능이다.  
Python 2 에서는 List Comprehension (리스트 내포)만을 지원하며, 
Python 3 에서는 Dictionary Comprehension과 Set Comprehension을 추가로 지원하고 있다.  
또한, 종종 Generator Comprehension이라고 일컫어 지는 Generator Expression이 있는데, 이는 다음 아티클에서 Generator와 함께 설명한다.

## 2. List Comprehension
List Comprehension (리스트 내포)는 입력 Sequence로부터 지정된 표현식에 따라 새로운 리스트 컬렉션을 빌드하는 것으로, 아래와 같은 문법을 갖는다.

#### <b>[출력표현식 for 요소 in 입력Sequence [if 조건식]]</b>
여기서 입력 Sequence는 입력으로 사용되는 Iteration이 가능한 데이타 Sequence 혹은 컬렉션이다.  
입력 Sequence는 for 루프를 돌며 각각의 요소를 하나씩 가져오게 되고, if 조건식이 있으면 해당 요소가 조건에 맞는지 체크하게 된다.  
만약 조건에 맞으면 출력 표현식(Output Expression)에 각 요소를 대입하여 출력 결과를 얻게 된다.  
이러한 과정을 모든 요소에 대해 실행하여 결과를 리스트로 리턴하게 된다.   
쉽게 설명하면 for 루프를 돌면 특정 조건에 있는 입력데이타를 변형하여 리스트로 출력하는 코드를 간단한 문법으로 표현한 것이다.
아래 예제에서 입력 Sequence (oldlist)는 숫자, 문자 그리고 Boolean 요소를 모두 갖는 리스트이다.   
List Comprehension 문장을 보면 이 입력 Sequence "oldlist"로부터 요소 i 를 하나씩 가져와 이 i의 타입이 정수형인지 체크하고,  
만약 그렇다면 표현식 "i * i" 를 실행하여 i의 제곱을 계산한다. 이렇게 모든 요소에 대해 계산하면 [1, 4, 9] 라는 결과 리스트(newlist)를 얻게 된다.
```python
oldlist = [1, 2, 'A', False, 3]
 
newlist = [i*i for i in oldlist if type(i)==int]
 
print(newlist)
# 출력: [1, 4, 9]
```
