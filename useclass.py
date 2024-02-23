# ----- 코드 정의 ------
import hashlib

#Member클래스 정의
class Member:
    def __init__(self, name, username, password):
        #속성
        self.name = name
        self.username = username
        self.password = password
    #메소드
    def display(self):
        print(f'회원정보는 이름 : {self.name}, 아이디 : {self.username} 이다')

#Post 클래스 정의
class Post:
    def __init__(self, title, content, author):
        #속성
        self.title = title
        self.content = content
        self.author = author


# ----- 코드 실행 ------
#빈 리스트 초기화
members = []
posts = []
hash_object=[]
hex_dig=[]

#인스턴스 & 리스트 추가
p1 = Member(name='박', username='박', password=1234)
p2 = Member(name='성', username='성', password=1235)
p3 = Member(name='현', username='현', password=1236)
members.append(p1)
members.append(p2)
members.append(p3)
post1=Post(title='이름1',content='행복',author=p1.username)
post2=Post(title='생각1',content='나눔',author=p1.username)
post3=Post(title='취미1',content='행복',author=p1.username)
post4=Post(title='이름2',content='나눔',author=p2.username)
post5=Post(title='생각2',content='행복',author=p2.username)
post6=Post(title='취미2',content='나눔',author=p2.username)
post7=Post(title='이름3',content='행북',author=p3.username)
post8=Post(title='생각3',content='나놈',author=p3.username)
post9=Post(title='취미3',content='니놈',author=p3.username)
posts.append(post1)
posts.append(post2)
posts.append(post3)
posts.append(post4)
posts.append(post5)
posts.append(post6)
posts.append(post7)
posts.append(post8)
posts.append(post9)

#해시함수로 비밀번호 해시화 한 것 보여주기
for member in members:
    hash_object.append(hashlib.sha256(str(member.password).encode()))
for ob in hash_object:
    hex_dig.append(ob.hexdigest())
    print(hex_dig)

#Member 터미널 추가하기
print('-----------------------')
pn=input('이름 별명 패스워드를 입력해주세요 : ')
pn_s=pn.split(' ')
pnn = Member(name=pn_s[0], username=pn_s[1], password=pn_s[2])
members.append(pnn)

#메소드 display활용하기 & 리스트 돌며 회원 이름 프린트
for member in members:
    print(member.name)
    member.display()
    
#Post 터미널 추가하기 // 인생 행복 박을 추천 드립니다
print('-----------------------')
postbox=input('제목 내용 작가를 입력해주세요 : ')
postbox_s=postbox.split(' ')
pon = Post(title=postbox_s[0], content=postbox_s[1], author=postbox_s[2])
posts.append(pon)

#특정 유저의 제목 출력
print('-----------------------')
for post in posts:
    if(post.author=='박'):
        print(f'제목 : {post.title}')

#내용의 특정 단어 있는 제목 출력
print('-----------------------')
for post in posts:
    if('행복' in post.content):
        print(f'제목 : {post.title}')













