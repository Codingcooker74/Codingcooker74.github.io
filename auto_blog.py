from google import genai
from git import Repo
import datetime
import os

# ==========================================
# 1. 기본 설정 
# ==========================================
# (주의) 아래 빈칸에 실제 발급받은 API 키를 넣어주세요.
GEMINI_API_KEY = "AIzaSyDNp2XQe8o8KMgQ6jMQSnRUFJ5CCy0Etv4"

# 경로 앞에 'r'을 붙여서 윈도우 경로 오류(\)를 해결했습니다.
BLOG_REPO_PATH = r"G:\다른 컴퓨터\내 노트북\Workspaces\Codingcooker74.github.io\posts" 

# ==========================================
# 2. Gemini를 이용해 블로그 글(Markdown) 생성 (최신 문법)
# ==========================================
# 최신 genai 클라이언트로 연결합니다.
client = genai.Client(api_key=GEMINI_API_KEY)

print("Gemini가 글을 작성 중입니다...")
prompt = """
당신은 IT 전문 블로거입니다. 
오늘의 최신 AI 기술 트렌드 1가지에 대해 블로그 포스트를 작성해 주세요.
반드시 Markdown 형식으로 작성하고, 제목은 # 로 시작해 주세요.
"""

try:
    # 최신 모델인 gemini-2.5-flash를 사용합니다.
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt
    )
    blog_content = response.text

    # ==========================================
    # 3. 작성된 글을 .md 파일로 컴퓨터에 저장
    # ==========================================
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    file_name = f"{today}-ai-trend.md"
    file_path = os.path.join(BLOG_REPO_PATH, file_name)

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(blog_content)
    print(f"파일 저장 완료: {file_name}")

    # ==========================================
    # 4. GitHub로 자동 Push (블로그에 실제 발행)
    # ==========================================
    print("GitHub에 글을 업로드합니다...")
    repo = Repo(BLOG_REPO_PATH)
    
    # 변경된 파일을 장바구니에 담고, 이름표(커밋 메시지)를 붙여 전송합니다.
    repo.git.add(all=True) 
    repo.index.commit(f"Auto-post: {today} 블로그 자동 업데이트") 
    
    origin = repo.remote(name='origin')
    origin.push()
    print("성공적으로 블로그에 글이 발행되었습니다! 🎉")

except Exception as e:
    print(f"오류가 발생했습니다: {e}")