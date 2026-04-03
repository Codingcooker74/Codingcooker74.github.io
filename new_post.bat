@echo off
setlocal

:: 오늘 날짜 가져오기 (YYYY-MM-DD 형식)
for /f "tokens=2 delims==" %%I in ('wmic os get localdatetime /value') do set datetime=%%I
set YYYY=%datetime:~0,4%
set MM=%datetime:~4,2%
set DD=%datetime:~6,2%
set TODAY=%YYYY%-%MM%-%DD%

:: 사용자로부터 파일명 (제목) 입력받기
set /p POST_TITLE="새 포스트의 영문 제목을 입력하세요 (예: my-new-post): "

:: 파일 이름 생성
set FILE_NAME=_posts\%TODAY%-%POST_TITLE%.md

:: 디렉토리가 없으면 생성
if not exist _posts mkdir _posts

:: Markdown 템플릿 작성
echo --- > "%FILE_NAME%"
echo layout: post >> "%FILE_NAME%"
echo title: "새로운 포스트 제목" >> "%FILE_NAME%"
echo date: %TODAY% 12:00:00 +0900 >> "%FILE_NAME%"
echo categories: update >> "%FILE_NAME%"
echo --- >> "%FILE_NAME%"
echo. >> "%FILE_NAME%"
echo 이곳에 마크다운으로 글을 작성하세요. >> "%FILE_NAME%"

echo.
echo 새 포스트 파일이 생성되었습니다: %FILE_NAME%
echo 해당 파일을 열어 글을 작성하세요.
pause
