# def recursive_function():
#     print("recursive~~")
#     recursive_function()


# recursive_function()

def recursive_function(i):
    # 100번째 출력했을 때 종료되도록 종료 조건 명시
    if i == 100:
        return
    print(i, "번째 재귀 함수에서", i+1, "번째 재귀 함수를 호출합니다.")
    recursive_function(i+1)
    print(i, "번째 재귀 함수를 종료합니다.")


recursive_function(70)

# 스택 자료구조를 이용한다.
# 함수를 계속 호출했을 때 가장 마지막에 호출한 함수가 먼저 수행을 끝내야 그 앞의 함수 호출이 종료된다.
# 컴퓨터 구조 측면에서 연속해서 호출하는 함수는 메인 메모리의 스택 공간에 적재되므로 스택 자료구조와 같다고 할 수 있다.
