# *Lactobacillus fermentum* 유전체 간 유사도 분석 (ANI & AAI)

## 1. 개요
*Lactobacillus fermentum* 균주의 완전 유전체 서열을 기반으로  
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

## 3. ANI분석

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


## 3.4 분석 결과 요약 (ANI 기반)

분석 결과, *Lactobacillus fermentum*의 155개 완전 유전체 간 **ANI (Average Nucleotide Identity)** 값은  
대부분 **95% 이상**으로 나타났으며, 이는 거의 모든 균주가 **동일 종 수준**에 해당함을 의미한다.  

> 💡 본 결과는 *L. fermentum* 균주들이 **염기서열 수준에서 매우 높은 유사성**을 가지며,  
> 종 내 유전체 다양성 수준에서 분화되었음을 시사한다.

결과 파일: https://github.com/igchoi/IBT610-CompGen/blob/851efc11fd141ca89215da43de5683fadd4d902c/2025-Fall/mjbaek/ani_heatmap.png

### 🔍 ANI 해석 기준

| 구간 | 분류 기준 | 의미 |
|:-----:|:-----------|:------|
| **ANI ≥ 95%** | 동일 종 (Same species) | 유전체 간 높은 염기 유사성으로 동일 종으로 간주 |
| **83% ≤ ANI < 95%** | 근연종 (Closely related species) | 유사하지만 별개의 종일 가능성 존재 |
| **ANI < 83%** | 다른 종 또는 속 (Different species/genus) | 속 수준 이상의 계통적 차이 |

---

### 📊 결과 요약 
- 분석된 155개 *Lactobacillus fermentum* 유전체 중 **대부분의 쌍이 95% 이상**의 ANI 값을 보임  
- 일부 샘플은 **83~95% 구간**에 위치하여, *L. fermentum* 내에서 **근연종적 다양성** 가능성이 있음  
- 83% 미만의 ANI를 보인 샘플은 거의 없었으며, 이는 대부분이 동일 종임을 뒷받침함  


## 4. AAI 분석  

### 4.1 개요  
**AAI (Average Amino Acid Identity)** 는 두 유전체 간 존재하는 **상동 단백질 서열의 평균 아미노산 일치율**을 의미한다.  
이는 ANI보다 **보다 깊은 진화적 수준(속 또는 과 수준)** 에서의 유연관계를 평가하는 데 사용된다.  


---

### 4.2 분석 도구: [CompareM](https://github.com/dparks1134/CompareM)  
**CompareM**은 여러 유전체 간의 **AAI (Average Amino Acid Identity)** 값을 효율적으로 계산하는 도구로,  
다음과 같은 절차로 동작한다.

1. 각 유전체의 단백질 서열(FASTA 또는 amino acid 파일)을 추출한다.  
2. 유전체 쌍 간 상동 단백질을 **BLASTp 기반**으로 비교한다.  
3. 상호 best hit (**Reciprocal Best Hit, RBH**)을 선별한다.  
4. 일치한 단백질 쌍의 평균 아미노산 일치율을 계산하여 **AAI 값을 산출**한다.  

---

### 4.3 분석 과정  

1. NCBI에서 수집한 *Lactobacillus fermentum* 155개 완전 유전체의 단백질 서열을 준비한다.  
2. `CompareM aai_wf` 모듈을 이용하여 모든 유전체 쌍 간 **AAI 값을 계산**한다.  
3. 결과 매트릭스(AAI matrix)를 **heatmap 형태**로 시각화한다.  

---

### 4.4 분석 결과 요약 (AAI 기반)  

분석 결과, *Lactobacillus fermentum*의 155개 완전 유전체 간 **AAI (Average Amino Acid Identity)** 값은  
대부분 **96% 이상**으로 나타났으며, 이는 단백질 서열 수준에서도 매우 높은 상동성을 보임을 의미한다.  

> 💡 본 결과는 *L. fermentum* 균주들이 **기능적 유전자 수준에서도 동일 종으로 분류될 수 있는 수준의 유사성**을 유지하고 있음을 시사한다.

📁 **결과 파일:** [aai_heatmap.png](https://github.com/igchoi/IBT610-CompGen/blob/main/2025-Fall/mjbaek/aai_heatmap.png)

---

### 🔍 AAI 해석 기준  

| 구간 | 분류 기준 | 의미 |
|:-----:|:-----------|:------|
| **AAI ≥ 95%** | 동일 종 (Same species) | 단백질 수준에서 높은 상동성 → 동일 종으로 간주 |
| **70% ≤ AAI < 95%** | 동일 속 내 다른 종 (Different species within genus) | 유사하나 종 수준에서 구분 가능 |
| **AAI < 70%** | 다른 속 (Different genus) | 속 수준 이상의 계통적 차이 존재 |

---

### 📊 결과 요약  

- 155개 *Lactobacillus fermentum* 유전체 대부분이 **96% 이상 AAI 값**을 나타냄  
- 소수의 샘플이 **90~95% 구간**에 위치, 이는 **속 내 종 간의 미세한 기능적 다양성** 가능성을 시사  
- **70% 미만의 AAI 값은 관찰되지 않음**, 모든 균주가 동일 속 (*Lactobacillus*) 내에서 밀접한 유연관계를 가짐을 확인  

결과 파일: 



