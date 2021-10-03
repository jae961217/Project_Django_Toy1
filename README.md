Django Framework 기반 Web Page 구현

- 커뮤니티 서비스의 게시판 기능 개발을 목적으로 함
- 영화 데이터의 생성, 조회, 수정, 삭제가 가능하도록 구현

1. Admin

   - 관리자 설정
   - DB 테이블 확인

2. Index

   - DB 전체 조회
   - html 표시

3. New + Create

   - form으로 새로운 내용 입력
   - request.POST를 이용해서 데이터 받아오기
   - save()를 통해서 저장

4. Edit + Update

   - New + Create 와 비슷한 형태로 사용

5. Delete

   - POST 방식으로 들어오는지 확인

   - delete()로 데이터 삭제