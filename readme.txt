# AI 클라우드 RAG 파이프라인

## 개요

이 프로젝트는 RAG(Retrieval-Augmented Generation) 파이프라인을 사용하여 도커화된 AI 클라우드 환경을 구축하는 예제입니다. 주요 서비스로는 프레임워크, 임베딩 모델, 벡터 데이터베이스(Qdrant), vLLM 서비스가 포함됩니다. 프레임워크는 사용자의 질의를 받아 임베딩 모델과 벡터 DB를 통해 컨텍스트를 검색하고, 최종적으로 LLM을 통해 응답을 생성하여 웹 화면에 출력합니다.

## 서비스 흐름

1. **프레임워크**: 사용자의 질의를 받아 임베딩 모델 및 벡터 DB와 통신하여 관련 컨텍스트를 검색하고, 이를 기반으로 LLM에 요청을 전달하여 응답을 생성합니다.
2. **임베딩 모델**: 입력된 텍스트를 임베딩 벡터로 변환하여 프레임워크에 제공합니다.
3. **벡터 데이터베이스(Qdrant)**: 임베딩 모델에서 받은 벡터를 이용해 유사한 컨텍스트를 검색합니다.
4. **vLLM**: 컨텍스트와 사용자의 질의를 바탕으로 최종 텍스트 응답을 생성합니다.

## 소스 코드 구조

ai-cloud-240826/ 
├── docker-compose.yml # 전체 서비스 도커 설정 파일 
├── framework/ # 프레임워크 서비스 디렉토리 │ 
├── Dockerfile # 프레임워크 서비스 Dockerfile │ ├── app.py # 프레임워크 서비스 앱 코드 │ └── requirements.txt # 프레임워크 서비스 종속성 파일 ├── embedding_model/ # 임베딩 모델 서비스 디렉토리 │ ├── Dockerfile # 임베딩 모델 Dockerfile │ ├── app.py # 임베딩 모델 앱 코드 │ └── requirements.txt # 임베딩 모델 종속성 파일 ├── vector_db/ # 벡터 DB 서비스 디렉토리 │ ├── init_db.py # 초기 데이터베이스 설정 스크립트 │ └── Dockerfile # 벡터 DB Dockerfile └── llm/ # vLLM 서비스 디렉토리 ├── Dockerfile # LLM 서비스 Dockerfile ├── app.py # LLM 서비스 앱 코드 └── requirements.txt # LLM 서비스 종속성 파일



## 빌드 및 실행 방법

1. **프로젝트 클론**: 
   ```bash
   git clone https://github.com/lausiv7/ai-cloud-240826.git
   cd ai-cloud-240826



