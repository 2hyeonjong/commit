```python
# try-excepytion 사용 예
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 7, 9, 1, 2, 3, 3, 5, 2, 6, 8, 9, 0, 1, 1, 4, 7, 0]
answer = {}
for number in my_list:
    try:
        answer[number] += 1
    except KeyError:
        answer[number] = 1
print(answer)

print(answer[1]) # = 4
print(answer[3])  # = 3

#if 문 사용예

answer = {}
for number in my_list:
    if number in answer:
      answer[number] +=1
    else:
      answer[number] =1
print(answer)

print(answer[1]) # = 4
print(answer[3])  # = 3
```
