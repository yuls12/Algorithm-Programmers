# 문자열 밀기

[![programmers](https://user-images.githubusercontent.com/69426184/209522553-bab40080-50ba-4743-86a3-f6198bff3974.png)](https://school.programmers.co.kr/learn/courses/30/lessons/120921)

<br/>

## 문제 설명

문자열 "hello"에서 각 문자를 오른쪽으로 한 칸씩 밀고 마지막 문자는 맨 앞으로 이동시키면 "ohell"이 됩니다.

이것을 문자열을 민다고 정의한다면 문자열 A와 B가 매개변수로 주어질 때, A를 밀어서 B가 될 수 있다면 몇 번 밀어야 하는지 횟수를 return하고 밀어서 B가 될 수 없으면 -1을 return 하도록 solution 함수를 완성해보세요.

<br/>

## 제한사항

-   0 < A의 길이 = B의 길이 < 100
-   A, B는 알파벳 소문자로 이루어져 있습니다.

<br/>

## 입출력 예

| A       | B       | result |
| ------- | ------- | ------ |
| "hello" | "ohell" | 1      |
| "apple" | "elppa" | -1     |

<br/>

## 입출력 예 설명

### 입출력 예 #1

"hello"를 오른쪽으로 한 칸 밀면 "ohell"가 됩니다.

<br/>

### 입출력 예 #2

"apple"은 몇 번을 밀어도 "elppa"가 될 수 없습니다.
