# 🧰 Python 개발 환경 구축 가이드

- [🧰 Python 개발 환경 구축 가이드](#-python-개발-환경-구축-가이드)
  - [개요](#개요)
  - [🐍 Python Tutorial Summary](#-python-tutorial-summary)
  - [📌 1. Python 소개](#-1-python-소개)
  - [📌 2. Python 설치](#-2-python-설치)
  - [📌 3. 가상환경(Virtual Environment) 설정](#-3-가상환경virtual-environment-설정)
    - [✔ 가상환경 생성](#-가상환경-생성)
    - [✔ 가상환경 활성화](#-가상환경-활성화)
    - [✔ 가상환경 종료](#-가상환경-종료)
  - [📌 4. 필수 패키지 관리(PIP)](#-4-필수-패키지-관리pip)
    - [✔ 패키지 설치](#-패키지-설치)
    - [✔ 패키지 목록 저장](#-패키지-목록-저장)
    - [✔ requirements 설치](#-requirements-설치)
  - [📌 5. Python 개발 환경 종류](#-5-python-개발-환경-종류)
  - [📌 6. Jupyter Notebook 환경](#-6-jupyter-notebook-환경)
    - [✔ 설치](#-설치)
    - [✔ 실행](#-실행)
  - [📌 7. Jupyter Notebook 특징](#-7-jupyter-notebook-특징)
    - [✔ 셀 단위 실행](#-셀-단위-실행)
    - [✔ 실행 결과가 즉시 표시](#-실행-결과가-즉시-표시)
    - [✔ Markdown 지원](#-markdown-지원)
    - [✔ 변수 상태 유지](#-변수-상태-유지)
  - [📌 8. .py 파일 vs Jupyter Notebook 차이](#-8-py-파일-vs-jupyter-notebook-차이)

<br/>

## 개요

이 문서는 **Python 개발 환경 구축**을 위한 핵심 내용을 정리한
가이드입니다.\
특히 Jupyter Notebook 기반 실습 환경과 `.ipynb` 파일 기반 개발 환경의
차이를 중심으로 설명합니다.

<br/>

## 🐍 Python Tutorial Summary

**Reference:** <https://www.w3schools.com/python/default.asp>  

W3Schools Python Tutorial을 기반으로 작성된 Python 입문용 정리
문서입니다.

<br/>

## 📌 1. Python 소개

- 파이썬(Python)은 배우기 쉽고 읽기 쉬운 고수준 프로그래밍 언어입니다.
- 다양한 용도에 사용됨  
  → 웹 개발, 데이터 분석, 머신러닝, 자동화, DevOps 스크립트 등  
- 인터프리터 언어로, 코드를 바로 실행하여 확인 가능함

<br/>

## 📌 2. Python 설치

- Python.org 다운로드: <https://www.python.org/downloads/>
- 설치 시 반드시 **Add Python to PATH** 체크  
- 설치 확인:

    ```bash
    python --version
    ```

<br/>

## 📌 3. 가상환경(Virtual Environment) 설정

파이썬 프로젝트는 라이브러리 버전 충돌을 막기 위해 프로젝트별 가상환경 사용을 권장합니다.

### ✔ 가상환경 생성

``` bash
python -m venv venv
```

### ✔ 가상환경 활성화

- Windows (PowerShell):
  
  ```bash
  .\venv\Scripts\Activate.ps1
  ```

- Windows (CMD):

    ``` bash
    venv\Scripts\activate.bat
    ```

- macOS / Linux:

    ``` bash
    source venv/bin/activate
    ```

### ✔ 가상환경 종료

``` bash
deactivate
```

<br/>

## 📌 4. 필수 패키지 관리(PIP)

### ✔ 패키지 설치

``` bash
pip install 패키지명
```

### ✔ 패키지 목록 저장

``` bash
pip freeze > requirements.txt
```

### ✔ requirements 설치

``` bash
pip install -r requirements.txt
```

<br/>

## 📌 5. Python 개발 환경 종류

파이썬은 크게 아래 두 방식으로 개발할 수 있습니다.

| 환경                              | 설명                  | 장점                                   | 단점                  |
| ------------------------------- | ------------------- | ------------------------------------ | ------------------- |
| **Python Script (.py 파일)**    | 일반 텍스트 기반 코드 파일     | 실행 속도 빠름 / Git 관리 용이 / 실제 서비스 개발에 적합 | 시각화/데이터 분석 시 불편     |
| **Jupyter Notebook (.ipynb)** | 블록 단위 실행 가능한 대화형 환경 | 데이터 분석/실험에 최적 / 실행 결과가 바로 아래 표시      | 프로젝트 규모가 커지면 관리 어려움 |

<br/>

## 📌 6. Jupyter Notebook 환경

### ✔ 설치

가상환경 활성화 후:

``` bash
pip install jupyter
```

### ✔ 실행

``` bash
jupyter notebook
```

브라우저가 자동으로 열리며 Notebook 인터페이스가 나타납니다.

<br/>

## 📌 7. Jupyter Notebook 특징

### ✔ 셀 단위 실행

코드를 블록 단위로 실행할 수 있어 실험에 매우 적합함.

### ✔ 실행 결과가 즉시 표시

그래프/출력 결과가 코드 바로 아래 표시됨.

### ✔ Markdown 지원

문서 + 코드 + 결과를 한 파일 안에서 관리할 수 있음.

### ✔ 변수 상태 유지

한 셀에서 생성한 변수를 다른 셀에서도 사용 가능.

→ 이러한 특성 덕분에 데이터 분석, 머신러닝 실험에 매우 많이 사용됨.

<br/>

## 📌 8. .py 파일 vs Jupyter Notebook 차이

| 항목     | Python Script (.py)    | Jupyter Notebook (.ipynb) |
| ------ | ---------------------- | ------------------------- |
| 실행 방식  | 전체 실행                  | 셀 단위 실행                   |
| 목적     | 서버 개발, 자동화 스크립트, 실 서비스 | 데이터 분석, ML 실험             |
| 속도     | 빠름                     | 상대적으로 느릴 수 있음             |
| 구조     | 체계적 개발에 적합             | 작은 단위 실험에 적합              |
| 시각화    | 설정 필요                  | 기본적으로 즉시 시각화              |
| 문서화    | 별도 README 필요           | Markdown 내장               |
| Git 관리 | Diff 보기 쉬움             | JSON 구조라 Diff 관리 어려움      |
