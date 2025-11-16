# 🐍 Python Study – W3Schools 기반 개인 학습 저장소

이 저장소는 **W3Schools Python Tutorial**을 기반으로  
파이썬 기본 문법을 개인적으로 학습하고 정리하는 공간입니다.

🔗 튜토리얼: https://www.w3schools.com/python/default.asp

---

## 📚 1. 학습 목적 (Goals)

- Python 기초 문법을 체계적으로 학습하기  
- 모든 예제를 직접 타이핑하고 실행하며 이해하기  
- 각 주제별로 정리 파일(.py 또는 .ipynb)을 작성  
- 결과 + 개념 요약 + 메모를 기록하여 깊이 있게 학습  
- GitHub를 학습 노트처럼 사용하여 성장 기록 남기기  

---

## 🗂 2. 저장소 구조 (Structure)

python-study/
├── 01_Intro.py
├── 02_Syntax.py
├── 03_Comments.py
├── 04_Variables.py
├── ...
├── notes/ # 학습 메모/기록
│ └── 2025-11-15.md
├── template/
│ └── template.ipynb # 선택사항: Notebook 학습 템플릿
└── README.md

---

## 🧪 3. 학습 방법 (How I Study)

1. W3Schools에서 학습할 챕터 선택  
2. 예제 코드를 직접 입력해 실행  
3. 이해한 내용을 **주제별 파일**에 정리 (`00_주제.py` 또는 `.ipynb`)  
4. 주요 개념 요약 및 예제 실행 결과 포함  
5. 추가 메모는 `notes/` 폴더에 기록  
6. GitHub에 커밋 → 학습 흔적 남기기  

---

## 📝 4. 예제 파일 구성 예시

```python
# 📌 Python Syntax
# 설명: 들여쓰기, 기본 출력 문법

# 출력 예제
print("Hello, World!")

# 들여쓰기 예제
if 5 > 2:
    print("Five is greater than two!")

"""
메모
- Python은 들여쓰기가 문법
- 블록은 반드시 4 spaces 사용 (권장)
- Java의 { } 와 비교됨
"""
▶️ 5. 실행 방법 (Run)
Windows
bash
코드 복사
python 파일명.py
macOS
bash
코드 복사
python3 파일명.py
기본 문법 학습만 진행하므로 가상환경은 필요하지 않습니다.

📒 6. 학습 기록 (Daily Notes)
학습 중 느낀 점, 정리하고 싶은 내용, 메모는 notes/ 폴더에 날짜별로 작성합니다.

예시:

# 2025-11-16
- Python Comments 학습
- # 단일 라인, """ """ 여러 줄 문자열 사용 가능
- Java와 주석 방식 비교해 이해함
🎯 7. 향후 확장 계획 (Optional)
튜토리얼 학습 이후에는 아래 분야로 확장할 수 있습니다.

Python 기본 알고리즘/자료구조

간단한 미니 프로젝트 제작

크롤링(BeautifulSoup / Selenium)

FastAPI로 REST API 만들기

NumPy / Pandas 데이터 분석