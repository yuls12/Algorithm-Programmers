def solution(numbers):
    number = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine"
    ]
    for i, n in enumerate(number):
        numbers = numbers.replace(n, str(i))

    return int(numbers)