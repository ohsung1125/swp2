

# 파일에 있는 문자를 처리하는 예제
# 파일에 있는 문자의 비도수를 처리하는 예제

def process(filename):
    with open(filename, "r") as f: # 특정한 파일을  읽기 모드로 읽음
        # 각 문자의 빈도수를 추출하기 위하여 사전 데이터를 만들어주자
        # dict는 key와 value, 키와 값으로 구성되어 있기 때문에
        # 키:알파벳, 값: 빈도수
        dict={}
        data=f.read()
        for i in data: # 각 문자열을 방문하면서 하나씩 체크한다
            if i in dict: # 자료형에 키로 문자 알파벳이 포함되어 있다면
                dict[i] +=1 # 빈도수를 1씩 증가, 특정한 알바벳이 여러 번 나오는 경우, 1씩 증가
            else:
                dict[i]=1 # 그렇지 않으면 1로 설정, 특정한 알파벳을 처음 발견했한 경우.


    return dict # 해당 자료형을 리턴한다.


dict=process("input1.txt")
# 빈도수를 기준으로 내림차순 정렬을 수행
dict =sorted(dict.items(), key= lambda a:a[1], reverse=True)
# a={'H': 2} a[0]='H', a[1]=2 가 들어가 있는 상황이다.
# dict.items()는 키와 값(빈도수)을 가지는 한 개의 쌍이다.
# 이 때 정렬 기준은 dict.items()에서 얻은 a라는 키와 값의 쌍에서 a[0]는 키를 의미하고
# a[1]은 값(빈도수)을 의미한다.
# reverse=True는 값(빈도수)을 내림차순 정렬

# dict는 가장 많은 빈도수를 가진 문자를 먼저 출력해준다.

# dict는 리스트 형태를 가진다.
# [(' ', 10), ('e', 7), ('o', 6), ('a', 5), ('t', 4), ('i', 3), ('\n', 3), ('m', 3), ('s', 3), ('u', 3), ('d', 3), ('c', 3), ('H', 2), ('l', 2), ('n', 2), ('I', 2), ('h', 2), ('.', 2), ('r', 2), ('y', 2), ('J', 1), ('!', 1), ("'", 1), ('w', 1), ('?', 1), ('v', 1), ('p', 1)]
# 각 원소에 접근해 보면,  (' ', 10) 튜플형태를 가지고 있는 것을 확인할 수 있다.
# 튜플의 첫 번째 원소를 data로 받고, 튜플의 두 번째 원소를 count로 받는다
# 첫 번째 원소는 ' ', 'e'등으로 문자, data 가 되며, 두 번재 원소는 빈도수 count가 된다.
# 문자, 데이터 중에서 '\n' : 줄바꿈기호, 혹은 ' ':공백문자 일때는 출력하지 않고 무시하고 넘아간다.
# continue는 반복문을 무시하고 넘어간다
# 즉, 알파벳만 출력한다.
# 각 문자별 출현횟수를 출력한다.

for data, count in dict:
    if data == '\n' or data == ' ':
        continue
    print("%d 번 출현: [%c]" %(count, data))













