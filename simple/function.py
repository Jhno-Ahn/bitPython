# 함수 Function

# 문서로 만들어진 주석
# 나중에 꺼내서 씀
"""
    C          일반함수, 멤버함수(클래스 내에 선언)
    
    # 일반함수
    반환형 함수명( 매개변수) {
        실행문
        return;
    }
    
    # 맴버함수
    public :
        반환형 함수명( 매개변수) {
            실행문
            return;
        }
    
    ----------------------------------------
    # javaScript 일반함수, 맴버함수(클래스 내에 선언)
    
    # 일반함수
    function 함수명(매게변수) {
        실행무니
        return;
    }
    
    # 맴버함수
    # 함수를 일회용(익명함수)로 구현
    함수명 = function (매개변수) {
        실행문;
        return;
    }
    
    --------------------------------------
    Java                 맴버함수
    
    # 맴버함수
    public 반환형 함수명(매개변수) {
        싱행문;
        return;
    }
    
    --------------------------------------
    Python            일반함수, 멤버함수
    
    # 일반함수
    def 함수명(매개변수) :
        실행문
        return
    
    
    # 맴버함수
    def 함수명(self, 매개변수) : # self를 꼭 명시해 주어야함, java의 this와 같은 개념임
        실행문
        return
    

"""

# 함수를 사용하는이유
# 반복되는 내용을 묶어서 처리한다.
# 선언하고, 구현하고, 호출해서 사용
# 함수는 반드시 호출한 자리로 돌아온다.
# 모든 함수는 리턴이 있다.
# 리턴은 하나밖에 줄 수 없다. 여러게 사용할 수 없다.

print("Hello Python")
print("Hello Python")
print("Hello Python")

def hello() :               # 선언    함수를 알려준다
    print("Hello Python")   # 구현    함수가 할 일을 정의한다.
    # return                # 생략되어있음
hello()                     # 호출    함수를 사용한다.
hello()
hello()

# def max(a, b):
#     if a> b :
#         return a
#     elif b > a :
#         return b
#     else : # elif로 사용해도 에러는 없음 # elif a == b :
#         return "같다"
# print(max(2, 2))


"""
    오버로드
    함수의 이름은 같아도 매개변수 자료향이 다르거나 개수가 다르거나 순서가 다를 경우 다른 함수로 취급
    
    C            오버로드 X , 매개변수 초기값 O
    int hap(int a, int b) {return a+b}
    int hap(double a, double b) {return a+b}
    
    # int hap(int a, int b) {}
    int hap(int a=0, int b=0, int c=0) {} # 이렇게는 가능
    hap(2, 5)
    hap(2, 5, 7)
    
    
    C++                오버로드 O, 초기값 O
    int hap(int a, int b) {return a+b}
    int hap(double a, double b) {return a+b}
    
    
    Java            오버로드 O, 초기값 X
    public int hap(int a, int b) {return a + b}
    public int hap(double a, double b){return a + b}
    
    # 갯수가 다른경우 오버로드를 다해주어야함
    # 그것을 방지하기위해
    # 초기값 대신에 이것을 사용함
    public int hap(int ... args) {
        for (int a : args) {
        }
    
    Python        오버로드 X, 초기값 O, VarArgs O
"""

# 변수는 덮어쓸 수 있지만
# 함수는 덮어쓸 수 없다.
def hap(a, b) :
    return a + b
# def hap(c, d) : # 같은이름으로 구현하면 안된다.
#     return c + d
print(hap(5, 2))
print(hap(5.5, 2.7))

# 초기값 주기
def cha(a, b, c=0) :
    return a - b - c
# print(cha(5, 1, 2)) # 매개변수의 갯수를 맞춰주어라
print(cha(5, 1))# 하지만 초기값을 준다면 에러는 나지 않는다

# def gop(a, b=0, c): # 주기 시작했으면 뒤는 모두 주어야한다.
def gop(a, b=0, c=0) :
    return a * b * c
print(gop(2, 5)) # c가 0이기에 0출력
print(gop(2))
# print(gop()) # 사용불가

# VarArg
# 튜플 형식으로 출력
def avg(*args) :
    # print(args)
    # print(type(args))
    sum = 0
    for a in args :
        sum += a
        print(sum / len(args))
avg(1, 2, 3)
avg(10, 20, 30, 40, 50)

def sum(a, b, *args) :
# def sum(a, *args, b) : # 에러남
# def sum(a, *args, *argss) : # args를 두개를 못줌
    print(a, b, args)
sum(10, 20, 30, 40, 50) # 10, 20은 그냥출력 30부터는 튜플로 출력



# 키워드 인수
def add ( a, b, c=0 ):
    print(a+b+c)
add(2, 5, 7)
add(2, 5)
add(a=5, b=7) # 그 인수의 이름을 가지고 넘기는것 그것이 키워드 인수 이렇게 하면 순서를 거꾸로 해도됨
add(b=7, a=5)
add(5, b=2, c=10) # 한번 주면 마지막까지 주어야한다.
add(10, b=20)

# 키워드 인수로 넘어온것만 가능
def insert(a, **params): # 딕셔너리로 넘어옴
    # print(type(params))
    print(a, end=" ")
    for key, value in params.items() :
        print(key, value, end=" ")
    print()
insert(10, b=10)
insert(10, b=20, c=30)
insert(a=10, b=20, c=30)
# insert(b=20, 10, c=30) # 순서가 틀려 에러남, a를 맨앞으로 받기로 했기 때문에
insert(b=20, c=30, a=10) # 단 이렇게는 가능함


# 섞어써보기
def hap1(a=10, *args, **params):
    print("a :",a, end=" ")
    # 튜플
    for i in args :
        print(i, end=" ")
    
    # 딕셔너리
    for key, value in params.items() :
        print(key, value, end=" ")
    print()

# 이런경우는 섞어? 쓰는것이 가능함!
# 값을 꼭 줘야하는것이 아님
# 딕셔너리만 주고 튜플을 안주어도 에러안남
# 단 일반 변수들은 값을 주어야함
hap1(10, "A", "B", "C")
hap1(20, "A", "B", b=20, c=30)
hap1(20, b=20, c=30)
hap1(20, 20, 30) # 순서때문에 하나는 a에게 들어감
hap1(b=20, c=30, d=40)
# hap1("A", "B", "C", a=20) # a라는 방에 값이 2개 들어가기에 에러가남


print()

# 지역변수, 전역번수
b = 10
b = 100
print(b)

a = 10                  # 전역변수 모든 영역에서 사용
def disp():
    a = 100             # 지역변수 할당 영역에서만 사용
    print("a :",a)
    print("b :",b)
disp()
    
def disp1():
    global a            # global 사용하면 그 안에 있는게 전역변수로 바뀜, 중간에 못들어감
    a = 1000
    print("a :",a) # a : 1000

disp1()    
print(a) # 1000
############지역변수 사칙##################
def ha():
    a = 5
    b = 2
    return a+b

def ch():
    a = 5
    b = 2
    return a-b

def go():
    a = 5
    b = 2
    return a*b

def mo():
    a = 5
    b = 2
    return a/b

print(ha())
print(ch())
print(go())
print(mo())

############전역변수 사칙##################
a , b = 5 , 2
def ha1():
    return a+b

def ch1():
    return a-b

def go1():
    return a*b

def mo1():
    return a/b

print(ha1())
print(ch1())
print(go1())
print(mo1())


# 내장함수

print(abs(10))
print(abs(-10))

print(all([1,2,3]))
print(all([1,2,0]))
print(any([0,"",False]))
print(any([1]))

print(dir())
aaaa = 10
print(dir())
del aaaa
print(dir())

import sys # sys모듈안에 있는
print(dir(sys)) # 사용가능한 목록출력

print(divmod(7, 3)) # 몫 나머지
print("1+2")
print(eval("1+2"))    

a = 10
print(id(a))
print(id(10))
b = a
print(id(b))

print(min("python"))
print(max("python"))
print(min([1,3,5,7,9]))
    
m = [50,10,40,30,20] #list
m.sort() #list.sort
print(m) #원본순서 정렬되어있음
m = sorted(m) 

print(list(zip([1,2,3], [4,5,6])))
    
    
# 람다함수
def add1(a, b):
    return a+b
print(add1(3,7))
add2 = lambda a,b : a+b # lambda 매개변수 : 리턴값
print(add2(4,9))
print((lambda a,b : a+b)(5,20)) # (lambda 매개변수형식 : 리턴값)(매개변수)

# filter(function, list) #리스트로 감싸야 출력가능
def even(a):
    return a%2==0
print(even(10))

print(list(filter(even, range(10)))) #even함수 만들어서 사용
print(list(filter(lambda x : x%2==0, range(10)))) #람다함수로 바로 사용

# map(function, list) #리스트로 감싸야 출력가능
print(list(map(lambda x : x*2, range(10))))

# reduce(function, list) #얘는 결과 합산해서 출력이라 리스트로 감쌀 필요없음
from functools import reduce
print(reduce(lambda x,y : x+y, range(10)))

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    