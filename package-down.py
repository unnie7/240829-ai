import os
import subprocess

# 모델 및 패키지 다운로드 경로
package_path = "./package"
embedding_model_path = os.path.join(package_path, "ko-sentence-bert-model")
llm_model_path = os.path.join(package_path, "kogpt2-model")

# 필요한 디렉토리 생성
os.makedirs(package_path, exist_ok=True)
os.makedirs(embedding_model_path, exist_ok=True)
os.makedirs(llm_model_path, exist_ok=True)

def run_command(command):
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")

print("Downloading embedding model...")
# 임베딩 모델 다운로드 (예: Ko-SentenceBERT)
run_command([
    "git",
    "clone",
    "https://huggingface.co/sentence-transformers/xlm-r-100langs-bert-base-nli-stsb-mean-tokens",
    embedding_model_path
])

print("Downloading LLM model...")
# LLM 모델 다운로드 (예: KoGPT2)
run_command([
    "git",
    "clone",
    "https://huggingface.co/taeminlee/kogpt2",
    llm_model_path
])

print("Downloading PyTorch package...")
# 필요한 패키지 다운로드
run_command([
    "wget",
    "https://download.pytorch.org/whl/cu113/torch-1.10.0+cu113-cp39-cp39-linux_x86_64.whl",
    "-O",
    f"{package_path}/torch-1.10.0+cu113-cp39-cp39-linux_x86_64.whl"
])

print("Downloading Transformers package...")
run_command([
    "wget",
    "https://files.pythonhosted.org/packages/5c/26/7b6c5eb3db37e4dfb7e2a78aafe1432d8a9c6a2c0832e55d94e5d45a4a8d/transformers-4.10.0-py3-none-any.whl",
    "-O",
    f"{package_path}/transformers-4.10.0-py3-none-any.whl"
])

print("All models and packages are downloaded.")
