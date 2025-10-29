# *Lactobacillus fermentum* 유전체 간 유사도 분석 (ANI & AAI)

## 1. 개요
본 연구에서는 *Lactobacillus fermentum* 균주의 완전 유전체 서열을 기반으로  
**ANI (Average Nucleotide Identity)** 와 **AAI (Average Amino Acid Identity)** 분석을 수행하여  
균주 간 유전적 유사도 및 진화적 관계를 평가하였다.

---

## 2. 데이터 수집

- **대상 균주:** *Lactobacillus fermentum*  
- **데이터 출처:** [NCBI Genome Database](https://www.ncbi.nlm.nih.gov/genome/)  
- **데이터 유형:** Complete genome FASTA (`.fna`) 파일  
- **수집 개수:** 총 155개  
- FASTA 파일이 존재하는 완전 유전체만 선별하여 분석에 사용하였다.

---

## 3. ANI 분석

### 3.1 개요  
**ANI (Average Nucleotide Identity)** 는 두 유전체 간 **상동 DNA 서열 구간의 평균 염기 일치율**을 의미한다.  
이는 종 수준에서 유전체의 유사성을 정량적으로 평가할 수 있는 가장 널리 사용되는 지표 중 하나이다.

---

### 3.2 분석 도구: [FastANI](https://github.com/ParBLiSS/FastANI)
**FastANI**는 유전체 간 ANI 값을 빠르고 정확하게 계산하는 도구로,  
다음과 같은 원리로 동작한다.

1. 각 유전체를 일정 길이의 **k-mer 단편(fragment)** 으로 분할한다.  
2. k-mer 단편 간의 상호 매핑을 통해 상동 영역을 식별한다.  
3. 일치하는 서열 구간의 평균 염기 일치율을 계산하여 ANI 값을 산출한다.  

---

### 3.3 분석 과정

1. NCBI에서 수집한 155개 유전체의 FASTA 파일을 준비한다.  
2. FastANI를 이용해 모든 유전체 쌍 간의 ANI 값을 계산한다.  

```bash
fastANI --ql genomes_list.txt --rl genomes_list.txt -o fastani_output.txt

결과 파일(fastani_output.txt)은 쌍별 비교 결과를 포함하며,
이를 행렬(matrix) 형태로 변환하여 heatmap 시각화에 활용하였다.

<img width="3600" height="3000" alt="ani_heatmap" src="https://github.com/user-attachments/assets/b627bccf-3a5f-45c3-abc7-13ecb0d0f704" />

