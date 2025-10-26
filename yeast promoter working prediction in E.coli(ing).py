def similarity(region, motif):
    region = region[:len(motif)]
    if len(region) != len(motif) or len(motif) == 0:
        return 0
    return sum(region[i] == motif[i] for i in range(len(region))) / len(motif)


def get_promoter_features(seq):
    seq = seq.upper()
    motifs = {
        'minus_35': ['TTGACA', 'TTGAAA', 'CTTGAC'],
        'minus_10': ['TATAAT', 'TATGAT', 'TATACT'],
        'SD': [
            'AGGAGG', 'GGAGG', 'AAGGAGG', 'UAAGGAGGU',
            'AGGA', 'GGAG', 'AAGGA', 'GAGGTT', 'AAAGGAGG'
        ],
        'AUG': ['ATG', 'GTG', 'TTG']
    }

    # Start codon 탐색
    aug_pos = -1
    for codon in motifs['AUG']:
        pos = seq.rfind(codon)
        if pos > aug_pos:
            aug_pos = pos
    if aug_pos == -1:
        return {"Error": "No start codon (ATG/GTG/TTG) found in sequence."}

    # -10 box
    region_10 = seq[max(aug_pos - 12, 0):max(aug_pos - 6, 0)]
    score_10 = max([similarity(region_10, m) for m in motifs['minus_10']])

    # -35 box
    region_35 = seq[max(aug_pos - 40, 0):max(aug_pos - 34, 0)]
    score_35 = max([similarity(region_35, m) for m in motifs['minus_35']])

    # Shine–Dalgarno
    SD_region = seq[max(aug_pos - 15, 0):max(aug_pos - 5, 0)]
    SD_score = max([similarity(SD_region, m) for m in motifs['SD']])

    # AU-rich enhancer
    enhancer_window = seq[max(aug_pos - 20, 0):max(aug_pos - 13, 0)]
    AU_rich_enhancer = (
        (enhancer_window.count('A') + enhancer_window.count('T')) / len(enhancer_window)
        if enhancer_window else 0
    )

    # Purine content
    purine_content = (
        (SD_region.count('A') + SD_region.count('G')) / len(SD_region)
        if SD_region else 0
    )

    # 전사 확률
    transcription_percent = ((score_35 + score_10) / 2) * 100
    # 번역 확률
    translation_percent = ((0.5 * SD_score + 0.3 * AU_rich_enhancer + 0.2 * purine_content)) * 100

    # ✅ 조건부 확률: 전사된 서열 중 번역될 확률
    # 전사가 0이면 division error 방지를 위해 0 처리
    combined_percent = translation_percent if transcription_percent > 0 else 0

    return {
        '-35_box_region': region_35,
        '-35_box_similarity': round(score_35, 3),
        '-10_box_region': region_10,
        '-10_box_similarity': round(score_10, 3),
        'SD_region': SD_region,
        'SD_similarity': round(SD_score, 3),
        'purine_content(SD)': round(purine_content, 3),
        'enhancer_region': enhancer_window,
        'AU_rich_enhancer': round(AU_rich_enhancer, 3),
        'transcription_probability(%)': round(transcription_percent, 2),
        'translation_probability(%)': round(translation_percent, 2),
        'conditional_translation_given_transcription(%)': round(combined_percent, 2)
    }


# ✅ 테스트 예시
promoter_seq = 'catagcttcaaaatgtttctactccttttttactcttccagattttctcggactccgcgcatcgccgtaccacttcaaaacacccaagcacagcatactaaatttcccctctttcttcctctagggtgtcgttaattacccgtactaaaggtttggaaaagaaaaaagagaccgcctcgtttctttttcttcgtcgaaaaaggcaataaaaatttttatcacgtttctttttcttgaaaattttttttttgatttttttctctttcgatgacctcccattgatatttaagttaataaacggtcttcaatttctcaagtttcagtttcatttttcttgttctattacaactttttttacttcttgctcattagaaagaaagcatagcaatctaatctaagTGCG'
result = get_promoter_features(promoter_seq)

for k, v in result.items():
    print(f"{k}: {v}")
