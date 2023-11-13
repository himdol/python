# Calculate
import collections.abc as co



if __name__ == '__main__':

    test_list = ['one', 'two', 'three']
    for i in range(test_list.__len__()):
        print(i, test_list[i])

    a = ['파이썬', '프로그램은', '빅데이터분석을', '위한', '필수적인', '도구이다.']
    print(a[-1])    # 마지막 첫번째 값
    print(a[-2:])   # 뒤로 두번째부터 마지막까지
    print(a[:2])    # 0부터 2직전 까지 요소값
    print(a[1:3])

    zoo = ('python', 'elephant', 'penguin')
    print(zoo)
    len(zoo) # 튜플의 길이

    for i in range(zoo):
        print(i)



