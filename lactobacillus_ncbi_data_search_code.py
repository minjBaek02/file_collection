# --- 필수 패키지 ---
from Bio import Entrez
import pandas as pd
from tqdm import tqdm

# --- 본인 이메일로 변경 (필수) ---
Entrez.email = "qoralswl159@gmail.com"

# --- 검색 대상: NCBI Nucleotide DB ---
search_term = "Lactobacillus[Organism] AND (genome OR gene OR sequence)"
max_records = 100000  # 검색 상한 (최대 10만 건까지 조회 가능)

# --- 데이터 검색 ---
print("🔍 NCBI에서 Lactobacillus 관련 유전자 검색 중...")
handle = Entrez.esearch(db="nucleotide", term=search_term, retmax=max_records)
record = Entrez.read(handle)
handle.close()

total_count = int(record["Count"])  # 전체 검색 결과 수
print(f"\n✅ NCBI 등록된 Lactobacillus 유전자 총 {total_count:,}건")

# --- annotation 여부 통계 (metadata 기반) ---
# 실제 서열은 다운로드하지 않음, 요약 정보만
annotated = 0

for start in tqdm(range(0, total_count, 1000), desc="Annotation 상태 확인 중"):
    handle = Entrez.esearch(db="nucleotide", term=search_term, retstart=start, retmax=1000)
    record = Entrez.read(handle)
    ids = record["IdList"]
    
    if not ids:
        continue

    summary_handle = Entrez.esummary(db="nucleotide", id=",".join(ids))
    summaries = Entrez.read(summary_handle)
    summary_handle.close()

    for entry in summaries:
        title = entry.get("Title", "").lower()
        if "cds" in title or "gene" in title or "annotated" in title:
            annotated += 1

print(f"\n📊 총 유전자 수: {total_count:,}")
print(f"🧬 Annotation 정보가 포함된 서열 수: {annotated:,}")
print(f"📈 비율: {annotated / total_count * 100:.2f}%")

# --- 결과 CSV 저장 ---
summary_df = pd.DataFrame([{
    "Total_sequences": total_count,
    "Annotated_sequences": annotated,
    "Annotation_ratio(%)": round(annotated / total_count * 100, 2)
}])
summary_df.to_csv("Lactobacillus_annotation_summary.csv", index=False)

print("\n💾 결과 파일 저장됨: Lactobacillus_annotation_summary.csv")
