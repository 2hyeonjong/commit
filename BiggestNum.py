def solution(numbers):
    #using lambda
    numbers = list(map(lambda x: str(x), numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    triple =lambda x: x*3
    print(triple(numbers))

    return int(''.join(numbers))

num = [3,34,30,9,5]
print(solution(num))