def similarity(region, motif):
    # motif와 region(실제 서열) 일치도를 계산 (0~1)
    region = region[:len(motif)]
    return sum([region[i]==motif[i] for i in range(len(region))]) / len(motif) if len(region) == len(motif) else 0

def get_promoter_features(seq):
    seq = seq.upper()  # 대소문자 무시, 모두 대문자로 변환
    motifs = {
        'minus_35': 'TTGACA',   # -35 박스 consensus motif
        'minus_10': 'TATAAT',   # -10 박스 consensus motif
        'SD': 'AGGAGG',         # Shine-Dalgarno motif
        'AUG': 'ATG'            # 시작코돈
    }
    
    # 마지막 ATG(시작코돈) 위치 찾기
    aug_pos = seq.rfind(motifs['AUG'])
    
    # -10 박스: ATG 기준 12~6bp upstream (RNA polymerase 결합, 전사 개시점 결정)
    minus_10_start = max(aug_pos - 12, 0)
    minus_10_end = max(aug_pos - 6, 0)
    region_10 = seq[minus_10_start:minus_10_end]
    
    # -35 박스: ATG 기준 40~34bp upstream (RNA polymerase 결합, 전사 효율 결정)
    minus_35_start = max(aug_pos - 40, 0)
    minus_35_end = max(aug_pos - 34, 0)
    region_35 = seq[minus_35_start:minus_35_end]
    
    # motif와 실제 서열의 일치도 계산
    score_10 = similarity(region_10, motifs['minus_10'])  # -10 박스 일치도
    score_35 = similarity(region_35, motifs['minus_35'])  # -35 박스 일치도
    
    # Shine-Dalgarno: ATG 앞 13~5bp (리보솜 결합, 번역 개시 효율)
    SD_region = seq[max(aug_pos-13,0):max(aug_pos-5,0)] if aug_pos > 12 else ''
    SD_score = similarity(SD_region, motifs['SD']) if SD_region else 0
    
    # AU-rich enhancer: ATG 앞 20~13bp (A/T 풍부, 번역 효율에 영향)
    enhancer_window = seq[max(aug_pos-20,0):max(aug_pos-13,0)] if aug_pos > 20 else ''
    AU_rich_enhancer = float(enhancer_window.count('A') + enhancer_window.count('T')) / len(enhancer_window) if enhancer_window else 0
    
    # 전사 확률: -35, -10 박스 motif 일치도 평균 (퍼센티지)
    transcription_percent = ((score_35 + score_10) / 2) * 100
    # 번역 확률: Shine-Dalgarno와 AU-rich enhancer 조합 점수 (퍼센티지)
    translation_percent = ((0.6 * SD_score + 0.4 * AU_rich_enhancer)) * 100
    # 전사+번역 동시 확률: 두 확률의 곱을 100으로 나눈 값 (퍼센티지)
    combined_percent = (transcription_percent * translation_percent) / 100
    
    return {
        '-35_box_region': region_35,                # -35 박스 실제 서열
        '-35_box_similarity': score_35,             # -35 박스 motif와의 일치도
        '-10_box_region': region_10,                # -10 박스 실제 서열
        '-10_box_similarity': score_10,             # -10 박스 motif와의 일치도
        'SD_region': SD_region,                     # Shine-Dalgarno 실제 서열
        'SD_similarity': SD_score,                  # Shine-Dalgarno motif와의 일치도
        'enhancer_region': enhancer_window,         # AU-rich enhancer 실제 서열
        'AU_rich_enhancer': AU_rich_enhancer,       # AU-rich enhancer A/T 비율
        'transcription_probability(%)': transcription_percent,  # 전사 효율 (%)
        'translation_probability(%)': translation_percent,      # 번역 효율 (%)
        'combined_probability(%)': combined_percent             # 두 단계 동시 효율 (%)
    }

# 테스트 시퀀스 예시 (대소문자 혼합 가능)
promoter_seq = 'GTGACATTTGACANNNNNNNNNNTATAATNNNNAGGAGGNNNNNNNNNNATGCCCCTTAAT'
result = get_promoter_features(promoter_seq)
for k, v in result.items():
    print(f"{k}: {v}")

