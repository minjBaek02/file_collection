# TDH3 Promoter Sequence Analysis

#Input Sequence
promoter_seq = ('CTATTTTCGAGGACCTTGTCACCTTGAGCCCAAGAGAGCCAAGATTTAAATTTTCCTATGACTTGATGCAAATTCCCAAAGCTAATAACATGCAAGACACGTACGGTCAAGAAGACATATTTGACCTCTTAACAGGTTCAGACGCGACTGCCTCATCAGTAAGACCCGTTGAAAAGAACTTACCTGAAAAAAACGAATATATACTAGCGTTGAATGTTAGCGTCAACAACAAGAAGTTTAATGACGCGGAGGCCAAGGCAAAAAGATTCCTTGATTACGTAAGGGAGTTAGAATCATTTTGAATAAAAAACACGCTTTTTCAGTTCGAGTTTATCATTATCAATACTGCCATTTCAAAGAATACGTAAATAATTAATAGTAGTGATTTTCCTAACTTTATTTAGTCAAAAAATTAGCCTTTTAATTCTGCTGTAACCCGTACATGCCCAAAATAGGGGGCGGGTTACACAGAATATATAACATCGTAGGTGTCTGGGTGAACAGTTTATTCCTGGCATCCACTAAATATAATGGAGCCCGCTTTTTAAGCTGGCATCCAGAAAAAAAAAGAATCCCAGCACCAAAATATTGTTTTCTTCACCAACCATCAGTTCATAGGTCCATTCTCTTAGCGCAACTACAGAGAACAGGGGCACAAACAGGCAAAAAACGGGCACAACCTCAATGGAGTGATGCAACCTGCCTGGAGTAAATGATGACACAAGGCAATTGACCCACGCATGTATCTATCTCATTTTCTTACACCTTCTATTACCTTCTGCTCTCTCTGATTTGGAAAAAGCTGAAAAAAAAGGTTGAAACCAGTTCCCTGAAATTATTCCCCTACTTGACTAATAAGTATATAAAGACGGTAGGTATTGATTGTAATTCTGTAAATCTATTTCTTAAACTTCTTAAATTCTACTTTTAAGTTAGTCTTTTTTTTAGTTTTAAAACACCAAGAACTTAGTTTCGAATAAACACACATAAACAAACAAATGCGATG')


#분석 코드 주요 특징
마지막 ATG 기준 검색: 서열에서 마지막 ATG 위치를 기준으로 upstream 영역을 추출

-35 박스: ATG 앞 34~40bp 위치, consensus 서열 TTGACA 와 비교하여 전사 효율 추정

-10 박스: ATG 앞 6~12bp 위치, consensus 서열 TATAAT 와 비교하여 전사 효율 추정

Shine-Dalgarno (SD) 영역: ATG 앞 5~13bp 위치, AGGAGG 와 비교하여 번역 효율 추정

AU-rich enhancer: ATG 앞 13~20bp 위치 A/T 비율 계산, 번역 효율에 영향

결과: 각 구간 서열과 motif 일치도, 전사/번역 확률(퍼센티지), 두 확률의 곱으로 종합 효율 산출

#분석 결과
| **Feature**                            | **Detected Region (6–8 bp)** | **Similarity / Score** | **Interpretation**                                           |
| -------------------------------------- | ---------------------------- | ---------------------- | ------------------------------------------------------------ |
|  **-35 box**                         | `GTCACC`                     | 0.50                   | Moderately conserved promoter recognition site               |
|  **-10 box**                         | `TTAAAT`                     | 0.67                   | Close to consensus `TATAAT`, likely functional               |
|  **Shine–Dalgarno (SD)**             | `TTTAAATT`                   | 0.17                   | Weak match to canonical `AGGAGG`, low translation initiation |
|  **Enhancer region**                  | `GCCAAGA`                    | 0.43                   | AU-rich enhancer sequence                                    |
|  **Transcription probability**       | —                            | **58.33 %**            | Moderate transcription strength                              |
|  **Translation probability**         | —                            | **27.14 %**            | Weak translation efficiency                                  |
|  **Combined expression probability** | —                            | **15.83 %**            | Overall moderate promoter performance                        |
