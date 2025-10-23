import subprocess
from pathlib import Path
import sys

def get_desktop_path():
    # 사용자별 바탕화면 경로 반환
    return Path.home() / "Desktop"

def check_ncbi_cli():
    try:
        subprocess.run(["datasets", "--version"], check=True)
        print("✅ NCBI datasets CLI 설치 확인 완료.\n")
    except FileNotFoundError:
        print("⚠️ datasets CLI가 없습니다. 설치 후 다시 시도해주세요.")
        print("예: conda install -c conda-forge ncbi-datasets-cli -y")
        sys.exit(1)

def main():
    desktop_path = get_desktop_path()
    zip_path = desktop_path / "lactobacillus_genomes.zip"

    print(f"\n📁 저장 경로: {zip_path}\n")
    check_ncbi_cli()
    print("⬇️ Lactobacillus genome assembly(유전체 어셈블리 단위) 다운로드 시작...")
    cmd = [
        "datasets", "download", "genome", "taxon", "Lactobacillus",
        "--include", "genome,gff3",
        "--filename", str(zip_path)
    ]
    subprocess.run(cmd, check=True)

    print("\n✅ 다운로드 완료!")
    print(f"📂 주요 파일 위치: {zip_path}")

if __name__ == "__main__":
    main()
