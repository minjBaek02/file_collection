# 🧬 Promoter Feature Analyzer

이 코드는 **yeast 프로모터 서열**로부터  
- 전사 개시 관련 motif (-35 box, -10 box),  
- 번역 개시 관련 motif (Shine–Dalgarno, start codon),  
- AU-rich enhancer, 퓨린 풍부도(purine content)  
등을 분석하여  
**전사 효율, 번역 효율, 그리고 전사된 서열 중 번역될 확률**을 추정합니다.

---

## ⚙️ 코드 개요

### 1️⃣ 주요 함수

#### `similarity(region, motif), 이전 코드와 달라진 점`
- 특정 DNA 서열(`region`)과 motif(`motif`)의 **일치율(0~1)** 계산  
- 예: `region = "TATAAT"`, `motif = "TATGAT"` → 5/6 = 0.833
- 이전 code에서 참고논문들을 참조하여 SD 서열이 될 수 있는 후보를 넓히고, 개시코돈 역시 보고된 가능성이 있는 서열을 추가했습니다. 또한, 기존의 전사,번역 확률을 더해서 최종적으로 전사, 번역될 확률을 제시했다면, 이번 코드는 전사가 일어난 서열중에 번역될 확률을 교집합을P **(Translation | Transcription)=Pt​/100Pt​×Pr​/100​=Pr**​ 의 조건부 확률로 계산해 도출합니다.

#### `get_promoter_features(seq)`
- 입력된 프로모터 서열에서 주요 motif를 탐색하고, 다음 항목들을 계산합니다.

| 항목 | 설명 |
|------|------|
| **-35_box_region** | ATG 기준 약 -35 위치의 실제 서열 |
| **-35_box_similarity** | σ70 promoter의 -35 consensus(`TTGACA`)와의 일치율 |
| **-10_box_region** | ATG 기준 약 -10 위치의 실제 서열 |
| **-10_box_similarity** | σ70 promoter의 -10 consensus(`TATAAT`)와의 일치율 |
| **SD_region** | Shine–Dalgarno(RBS) 후보 구간 (ATG 전 15~5bp) |
| **SD_similarity** | 여러 RBS 변이형과의 최대 일치율 |
| **purine_content(SD)** | SD 구간 내 A/G 비율 (리보솜 결합 효율에 영향) |
| **enhancer_region** | ATG 전 20~13bp 구간의 A/T 풍부 영역 |
| **AU_rich_enhancer** | enhancer 구간의 A+T 비율 |
| **transcription_probability(%)** | (-35, -10) 일치도 기반 전사 효율 (%) |
| **translation_probability(%)** | SD, AU-rich enhancer, purine 비율 기반 번역 효율 (%) |
| **conditional_translation_given_transcription(%)** | 전사된 서열 중 번역될 확률 (%) |

---

## 🧫 생물학적 배경

| 요소 | 기능 | 대표 Consensus | 참고문헌 |
|------|------|----------------|-----------|
| **-35 box** | RNA polymerase 결합 부위 | `TTGACA` | **σ70 promoter (E. coli)** |
| **-10 box** | 전사 개시 위치 조절 | `TATAAT` | σ70 promoter motif |
| **Shine–Dalgarno (RBS)** | 리보솜 16S rRNA와 상보적 결합 → 번역 개시 | `AGGAGG` | PubMed [7528374](https://pubmed.ncbi.nlm.nih.gov/7528374), [PMC139613](https://pmc.ncbi.nlm.nih.gov/articles/PMC139613/), [PMC7263185](https://pmc.ncbi.nlm.nih.gov/articles/PMC7263185/) |
| **AU-rich enhancer** | A/T 풍부한 구간, mRNA 안정성 및 번역 효율 상승 | `A/T-rich` | Translation efficiency studies (BMC Genomics 2015) |
| **Alternative start codons** | GTG, TTG (드물지만 실제 사용됨) | `GTG`, `TTG` | Gene expression in bacteria (Annu Rev Microbiol 1999) |

---

## 💻 사용 방법

### 1️⃣ 코드 실행
```python
# 코드 복사 후 Python 환경에서 실행
promoter_seq = 'GTGACATTTGACANNNNNNNNNNTATAATNNNNAGGAGGNNNNNNNNNNATGCCCCTTAAT'
result = get_promoter_features(promoter_seq)

for k, v in result.items():
    print(f"{k}: {v}")


