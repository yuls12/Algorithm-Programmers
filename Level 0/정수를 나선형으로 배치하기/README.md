[![programmers](https://user-images.githubusercontent.com/69426184/209522553-bab40080-50ba-4743-86a3-f6198bff3974.png)](https://school.programmers.co.kr/learn/courses/30/lessons/181832)

<br/>

## 문제 설명

양의 정수 n이 매개변수로 주어집니다. n × n 배열에 1부터 n2 까지 정수를 인덱스 [0][0]부터 시계방향 나선형으로 배치한 이차원 배열을 return 하는 solution 함수를 작성해 주세요.

<br/>

## 제한사항

-   1 ≤ n ≤ 30

<br/>

## 입출력 예

| n   | result                                                                                                |
| --- | ----------------------------------------------------------------------------------------------------- |
| 4   | [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]                                       |
| 5   | [[1, 2, 3, 4, 5], [16, 17, 18, 19, 6], [15, 24, 25, 20, 7], [14, 23, 22, 21, 8], [13, 12, 11, 10, 9]] |

<br/>

## 입출력 예 설명

### 입출력 예 #1

예제 1번의 n의 값은 4로 4 × 4 배열에 다음과 같이 1부터 16까지 숫자를 채울 수 있습니다.

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbIQybY%2FbtscUvGCxnJ%2Fmg7rbk8kXYl0eKg34wrOIk%2Fimg.png)

-   따라서 [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]를 return 합니다.

### 입출력 예 #2

예제 2번의 n의 값은 5로 5 × 5 배열에 다음과 같이 1부터 25까지 숫자를 채울 수 있습니다.

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FS6pbK%2FbtscQQZnXcq%2FM5ksZAnbwjKCN8VSBvGEH0%2Fimg.png)

-   따라서 [[1, 2, 3, 4, 5], [16, 17, 18, 19, 6], [15, 24, 25, 20, 7], [14, 23, 22, 21, 8], [13, 12, 11, 10, 9]]를 return 합니다.
