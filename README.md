# auto_kakao_channel
셀레니움을 이용한 카카오채널 자동화Python Code 매뉴얼

목차
1.	개요
2.	구성
3.	빠른시작
4.	DOCs
5.	개선방향


### 1.개요
카카오채널 자동화 모듈은 셀레니움을 이용하여 카카오톡 채널에 사진을 업로드하고 업로드한 사진들을 카카오톡 채널의 봇을 이용하여 간편하게 열람할 수 있도록 한다.

카카오채널 자동화 모듈이 제공하는 기능
*	크롬 브라우저를 통해 카카오채널 사이트에 로그인
*	여러 개의 채널을 하나의 모듈에서 관리
*	로컬의 이미지를 채널에 업로드하고 업로드한 이미지 링크를 저장
*	로컬의 이미지 확장자의 선택
*	로컬의 이미지 파일명의 선택
*	봇을 이용한 카카오톡 스킬의 구현

  


#### 1.git구성
selenium_auto.py : 카카오채널 자동화 모듈
flask_skill.py : 카카오 챗봇 모듈
3.빠른시작(카카오채널자동화)
1.Git과 최신 버전의 크롬드라이버의 설치가 필요하다.
(크롬드라이버 설치 https://chromedriver.chromium.org/downloads )
(git 설치 https://gitforwindows.org )

#### 2.카카오채널 자동화 모듈 다운로드
git clone https://github.com/vhehduatks/auto_kakao_channel.git 쉘 명령어를 입력하여 python코드를 다운받는다.
Clone 한 폴더에 크롬드라이버를 넣어준다.

#### 3.크롬 드라이버가 있는 폴더에 log폴더를 생성.
이는 추후 자동화 모듈이 예상치 못한 상황에서 종료되었을 경우 어디에서 문제가 생겼는지 확인 할 수 있도록 하는 역할을 한다.

#### 4.selenium_auto.py를 편집기로 열어 모듈에 필요한 변수를 입력
모듈에서 초기화에 필요한 변수는 다음과 같은
1.	카카오톡 ID(이메일 주소를 포함한)
2.	카카오톡 PASS
3.	카카오톡 채널의 고유 값
4.	이미지 폴더의 경로
5.	이미지 조건문에 사용될 시간범위(컴퓨터의 시간과 비교)
6.	이미지 조건문에 사용될 확장자
7.	이미지 링크를 저장할 텍스트문서의 이름
것들이 있다.
각각의 변수를 입력한 후 해당 클래스의 생성 매개변수를 입력하는 곳에 연결시켜주면 된다.

예시)

1).카카오톡 ID : ‘AAAAA@BB.com’

2).카카오톡 PASS : ‘12345’

3).카카오톡 채널의 고유 값 : ‘/_XXXXXXXX’
아래 사진을 예시로 들면 test_api채널의 고유값은 /_xcKxebxb 가 된다.
![그림1](https://user-images.githubusercontent.com/64114699/98361021-27bb2680-206e-11eb-9255-4acfa1b759ad.png)

4).자신의 이미지 파일들이 있는 로컬 경로 : “C:\Users\홍길동\data”

5).이미지 파일의 시간의 범위를 설정 
%Y :  년도, %M : 월, %D : 일, %H : 시, %M : 분

예시)
![그림2](https://user-images.githubusercontent.com/64114699/98361172-68b33b00-206e-11eb-8223-5ae0c6fdce9f.png)

위 사진의 파일명이 2020(년)11(월)05(일)-18(시)30(분)XXX…jpg 처럼 되어있는데 이때 자신이 올릴 파일과 시간을 시간단위로 대조 하고싶으면 ‘%Y%M%D-%H’ 라고 입력하면 된다.
일별로 대조하고 싶으면 ‘%Y%M%D’ 라고 입력하면 된다.

6).이미지 파일의 확장자 : ‘.jpg’
‘.jpg’나’.png’ 등 크롬이 인식할 수 있는 이미지 파일의 확장자를 입력

7).포스팅 된 이미지 파일의 링크를 저장하는 txt파일의 이름 : ~.txt
나중에 카카오톡 봇에서 사용하므로 기억해둘 것

7.다음 순서대로 클래스함수를 실행시켜서 자동화 완료
LOGIN() ->SET_CHANNEL() ->Check_File(‘시간범위’,’확장자’) ->SET_POST() ->STOR_SOURCE(‘~.txt) ->CLOSE_DRIVER()
