# Lactobacillus fermentum Pan-Genome Analysis Report  
### **Defining L. fermentum Phylogroups Through Accessory Gene Clustering and Functional COG Profiling**

---

# 📌 1. Introduction

*Lactobacillus fermentum*은 유제품, 채소 발효식품, 인체 장·구강 등 다양한 발효 환경에서 반복적으로 분리되며, 대체로 **1.8–2.3 Mb** 크기의 유전체를 가진다(Azmal Ali et al., 2018).  
동일 종 내에서도 균주 간 탄수화물 이용성, 에너지 전환, 아미노산 대사 및 스트레스 내성과 같은 **발효 관련 phenotype과 대응 유전자 조성에서 큰 변이**가 보고되어 왔다(Konyanee et al., 2019).

이러한 기능적 변이의 상당 부분은 보존적인 **core genome**만으로는 설명하기 어렵고, 환경 적응과 niche 특이성을 반영하는 **accessory genome 조합 차이**에서 기인한다는 점이 지적되어 왔다(Tatusov et al., 2001).
그럼에도 불구하고 기존 *L. fermentum* 유전체 연구는 주로 ANI 또는 core genome 기반 계통 분석에 집중되어 있으며,accessory genome 패턴과 발효 관련 기능을 통합하여 phylogroup을 정의한 체계적 분석은 제한적이다.

따라서 본 연구에서는 공개된 *L. fermentum* 유전체 **155개**를 ANI 기준으로 필터링하여 **80개의 high-quality genome**을 선별한 뒤 pan-genome을 구축하고, accessory gene의 존재/부재 패턴을 기반으로 phylogroup을 정의하였다.  
이어 각 균주의 accessory 유전자에 **COG 기반 기능 주석**을 부여하고, 발효와 직접적으로 연관된 **C (Energy), E (Amino acid), G (Carbohydrate)** 카테고리의 조성을 정량화하여 phylogroup 간 발효 대사 시그니처를 비교하였다.

또한, 동일 phylogroup 내에서 관찰되는 **outlier strain**의 경우, outlier로 보이는 이유가 발효와 관련된 특정 COG 기능 유전자의 소실 또는 획득과 관련이 있는지 보고자하였다.

<img width="2000" height="1080" alt="introduction" src="https://github.com/user-attachments/assets/1ba507ea-6724-4b91-9e32-7d4ba39389f8" />

> **Figure 1.** Overview of Functional Divergence and Phylogroup Structure in L. fermentum  

---

# 🧬 2. Materials and Methods

## 2.1 Genome Sequencing Data Acquisition

NCBI RefSeq 데이터베이스에서 *Lactobacillus fermentum*으로 분류된 모든 유전체(총 **155개**)를 FASTA 형식으로 다운로드 하여, fastANI를 이용해 균주 간 쌍별 ANI를 계산하였다.

Figure 2.와 같이 ANI 95% 미만 값을 보이는 종 내 이질적 균주 (예: AP017974.1 등)와 중복 유전체를 제거하고, complete한 genome 수준의 유전체만을 남겨 최종 **81개 균주**로 분석을 시작했다다.

<img width="3200" height="2800" alt="ani_heatmap" src="https://github.com/user-attachments/assets/12dec12e-fa07-4ee5-b7c0-6763e4dad9fe" />

> **Figure 2.** ANI heatmap

**Workflow**  
- **Input**:  
  - [NCBI RefSeq *L. fermentum* genomes (FASTA)](https://www.ncbi.nlm.nih.gov/refseq/)
- **Tool**:  
  - [fastANI](https://github.com/ParBLiSS/FastANI)
- **Output**:   
  - [ANI_matrix.tsv](https://github.com/minjBaek02/file_collection/blob/5fa516d39e5c16e8ae79d74fc3bd6a41baf088d은 해당 분석은 **산업 현장에 적용 가능한 정밀 으로 확장될 수 있다.

- 원료 특성에 맞춘 **데이터 기반 스타터 균주 선별**
- **C/G/E functional profile**을 활용한 발효 품질 예측

이러한 접근은 경험 중심의 스타터 개발을 넘어, **유전체 정보에 기반한 예측형 발효 시스템(precision fermentation)**으로 응용할 수 있을 것 같다.
