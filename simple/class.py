# 클래스
# 캡슐화 상속 다형성

# private
__a = 10            # 일반변수
def getA() :        # 일반함수
    return __a
print( getA() )

class P :
    __a = 10        # private
    b = 20
    def getA( self ) :
        return self.__a
    def getB( self ) :
        return self.b
    def setA( self, a ) :
        self.__a = a
p = P()
# print( p.__a )
print( p.b )
print( p.getA() )
print( p._P__a )    # private 멤버 접근 방법을 제공. 완벽한 캡슐화는 불가능.
# p.__a = 100
p.setA( 100 )
print( p.getA() )

print()
# 캡슐화
class Person :
    __name = ""
    __age = 0
    __height = 0.0
    def setName(self, name) :
        if len( name ) > 10 or name == "" :
            print( "이름을 바르게 입력하세요" )
        else :
            self.__name = name
    def setAge(self, age) :
        if age < 1 or age > 140 :
            print( "나이를 바르게 입력하세요" )
        else :
            self.__age = age
    def setHeight(self, height) :
        if height < 40 or height > 200 :
            print( "키를 바르게 입력하세요" )
        else :
            self.__height = height
    def getName(self) :
        return self.__name
    def getAge(self) :
        return self.__age
    def getHeight(self) :
        return self.__height
kim = Person()
kim.setName( "홍길동홍길동홍길동홍길동홍길동" )
kim.setAge( 150 )
kim.setHeight( 300 )
print( "이름 :", kim.getName() )
print( "나이 :", kim.getAge() )
print( "키 :", kim.getHeight() )          

lee = Person()
lee.setName( "이순신" )
lee.setAge( 30 )
lee.setHeight( 180 )
print( "이름 :", lee.getName() )
print( "나이 :", lee.getAge() )
print( "키 :", lee.getHeight() )     

# 생성자 - 객체초기화 / 소멸자 - 메모리 정리
# C++        Person() / ~Person()
# Java       Person()
# Python     __init__ / __del__

class User :
    def __init__(self, name="", age=0, tel="" ) :
        print( "생성자" )
        self.name = name
        self.age = age
        self.tel = tel
    def getName(self) :
        return self.name
    def getAge(self) :
        return self.age
    def getTel(self) :
        return self.tel
    # def __del__(self) :
    #     print( "소멸자" )
kim = User()
lee = User("이순신")
hong = User( age=20, tel="1111-2222" )
print( "이름 :", hong.getName() )
print( "나이 :", hong.getAge() )
print( "전화번호 :", hong.getTel() )

# static
# 모든 객체가 공유
# 메모리 영역중에 static 영역에 할당
# 메모리는 하나만 할당된다.
# 먼저할당 된다.
# 파이썬은 static 을 명시할 필요가 없다. 

print()
class Member :    
    name = "홍길동"                           # 멤버변수 클래스변수 static변수
    count = 0
    def __init__( self, age=0, cnt=0 ) :    # 지역변수    
        self.age = age
        self.cnt = cnt
        Member.count += 1
        self.cnt += 1;
    def getCnt(self) : 
        return self.cnt
    def getCount(self) :
        return Member.count

print( Member.name )           # 클래스명.멤버 
# print( Member.age )       

Member.name = "이순신" 

lee = Member()
print( lee.name )
print( lee.getCount() )
print( lee.getCnt() )

hong = Member()
print( hong.name )
print( hong.getCount() )
print( hong.getCnt() )

park = Member()
print( park.name )
print( park.getCount() )
print( park.getCnt() )
             
class Customer :
    name = "홍길동"
    def setName( self, name ) :
        self.name = name
    def getName(self) :
        return self.name
    @staticmethod
    def dispName() :            # static 함수
        return Customer.name
    # dispName = staticmethod( dispName )

kim = Customer()
kim.setName( "김유신" )
print( kim.getName() )          # 김유신
print( Customer.dispName() )    # 홍길동    
    
print()
class Car :
    cc = "2000cc"
    @staticmethod
    def getStatic() :
        return Car()
    @classmethod
    def getClass(cls) :     # cls 클래스를 매개변수로 전달
        return cls()
    def getcc(self) :
        return self.cc
class Truck( Car ) :
    cc = "3000cc"
a = Car.getStatic()         # Car
b = Car.getClass()          # Car
print( a.getcc() )          # 2000cc
print( b.getcc() )          # 2000cc

c = Truck.getStatic()       # Car
d = Truck.getClass()        # Truck
print( c.getcc() )          # 2000cc
print( d.getcc() )          # 3000cc
          
print()
# 상속
# 코드 재활용
# 부모 것은 내 것
# class Animal :
#     def __init__(self, name="") :    
#         self.name = name
#         print( "Animal 생성자" )
#     def getName(self) :
#         return self.name
# class Cat(Animal) :
#     def __init__(self, name="") :        
#         Animal.__init__(self, name)
#         print( "Cat 생성자" )        
# class Dog(Animal) :
#     None
# dog = Dog( "멍멍이" )
# print( dog.getName() )
# cat = Cat( "나비" )
# print( cat.getName() )
        
# 다중상속
# C++        구현 O 사용 X
# Java       구현 X 사용 O (인터페이스)
# Python     구현 O 사용 O 

class Animal :
    def __init__(self, name ) :
        self.name = name
    def getName(self) :
        return self.name
class Pet :
    def __init__(self, kind ) :
        self.kind = kind  
    def getKind(self) :
        return self.kind 
class Dog( Animal, Pet ) :
    def __init__(self, name, kind, color ) :  
        Animal.__init__( self, name )
        Pet.__init__( self, kind )      
        self.color = color 
    def getColor(self) :
        return self.color
    def getName(self) :                 # 재정의. 오버라이드
        return "이름 : " + self.name
    def getKind(self):
        return "품종 : " + self.kind
dog = Dog( "멍멍이", "잡종", "누런색" )
print( dog.getName() )
print( dog.getKind() )
print( dog.getColor() )    
    
# 다형성
class Bread :
    def __init__(self, name="" ) :
        self.name = name
    def getName(self) :
        return "Bread : " + self.name
    @classmethod
    def getClass(cls, msg ) :
        return cls( msg )
class Toast( Bread ) :
    def getName(self) :   
        return "Toast : " + self.name
class Cake( Bread ) :
    def getName(self) :
        return "Cake : " + self.name
class Redbean( Bread ) :
    def getName(self) :
        return "Redbean : " + self.name

# Bread bread = new Toast(); bread.getName();
# Bread bread = new Cake(); bread.getName();
# Bread bread = new Redbean(); bread.getName();     
toast = Toast( "토스트" )
print( toast.getName() )
cake = Cake( "케이크" )
print( cake.getName() )
redbean = Redbean( "팥빵" )
print( redbean.getName() )
print()

toast = Toast.getClass( "토스트" )
print( toast.getName() )
cake = Cake.getClass( "케이크" )
print( cake.getName() )
redbean = Redbean.getClass( "팥빵" )
print( redbean.getName() )

# @property / property()
class Gamer :
    __name = ""
    __age = 0
    @property
    def setName(self, name) :
        self.__name = name
    @property
    def setAge(self, age) :
        self.__age = age
    @property
    def getName(self) :
        return self.__name
    @property
    def getAge(self) :
        return self.__age
    # name = property( getName, setName )
    # age = property( getAge, setAge )
    
gamer = Gamer()
# gamer.setName( "홍길동" )
# gamer.setAge( 30 )
# print( gamer.getName() )
# print( gamer.getAge() )    

# print( gamer.__name )
gamer.name = "이순신"
gamer.age = 40
print( gamer.name )
print( gamer.age )




    















    
    
    
    














    