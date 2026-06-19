# 1. 첫 번째 3x3 배열 입력받기
arr1 = [list(map(int, input().split())) for _ in range(3)]

# 2. 중간에 있는 빈 줄 건너뛰기 (이게 핵심입니다!)
input()

# 3. 두 번째 3x3 배열 입력받기
arr2 = [list(map(int, input().split())) for _ in range(3)]

# 4. 같은 위치의 값끼리 곱해서 출력하기
for i in range(3):
    for j in range(3):
        # arr1과 arr2의 같은 행(i), 같은 열(j)의 값을 곱하고 공백(" ")을 두고 출력
        print(arr1[i][j] * arr2[i][j], end=" ")
    
    # 한 줄(행)의 출력이 끝나면 줄바꿈을 해줍니다.
    print()