# 관통 프로젝트

**📆 2021.11.17~25**



### 1. 목표

* 영화 정보 기반 추천 서비스 구성
* 커뮤니티 서비스 구성
* HTML, CSS, JavaScript, Vue.js, Django, REST API, DataBase 등을 활용한 실제 서비스 설계
* 서비스 관리 및 유지보수



### 2. 개발환경

#### A. 언어

i. Python 3.8+

ii. Django 3.x

#### B. 도구

i. VSCode

ii. Chrome Browser

#### C. 아키텍처

Django & Vanilla JS



### 3. 서비스 개요

#### 1. 프로젝트 구조

![image-20211124233058071](C:\Users\itrep\AppData\Roaming\Typora\typora-user-images\image-20211124233058071.png)

django & Vanilla JS의 조합으로, accounts, community, movies 3개의 앱으로 구성되어 있습니다.

#### 2. 영화 커뮤니티



#### 3. 영화 추천

사용자는 3가지 방식으로 영화를 추천받을 수 있습니다.

첫째, 무작위로 추천받을 수 있습니다. 초기화면(movies/index.html)에서 버튼 클릭을 통해 인기작을 기본적으로 4개의 영화를 추천받습니다. 원한다면 하단의 버튼을 클릭해 4개씩 더 추천받을 수 있습니다.

![image-20211124203314795](C:\Users\itrep\AppData\Roaming\Typora\typora-user-images\image-20211124203314795.png)

![image-20211124203330166](C:\Users\itrep\AppData\Roaming\Typora\typora-user-images\image-20211124203330166.png)

둘째, 크리스마스에 당신은? 이라는 질문을 기반으로한 추천을 받을 수 있습니다. 혼자서 보낸다면 코미디를, 연인과 보낸다면 로맨스, 친구와 보낸다면 SF, 가족끼리 보낸다면 가족영화를 추천받습니다.

![image-20211124203434488](C:\Users\itrep\AppData\Roaming\Typora\typora-user-images\image-20211124203434488.png)

![image-20211124232841428](C:\Users\itrep\AppData\Roaming\Typora\typora-user-images\image-20211124232841428.png)

셋째, 유저가 팔로우한 사용자가 좋아요한 영화를 추천받을 수 있습니다. 

💻 사진 1: 유저가 추천받은 영화

![image-20211124204519121](C:\Users\itrep\AppData\Roaming\Typora\typora-user-images\image-20211124204519121.png)

💻 사진 2 : 유저가 팔로우한 사용자 bobo가 좋아하는 영화

![image-20211124215137923](C:\Users\itrep\AppData\Roaming\Typora\typora-user-images\image-20211124215137923.png)





프로젝트 구조에 대한 설명을 반드시 명시해야 합니다

영화 커뮤니티에 필요한 기능을 구성하여야 합니다.

