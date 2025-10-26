# 🔬 Promoter / Translation Motif Analyzer (for 5'→3' DNA)
# Works even without ATG — assumes sequence end as reference
# Use inside Jupyter Notebook

from ipywidgets import Text, Button, VBox, Output
from IPython.display import display

# -------------------- Core Functions --------------------

def similarity(region, motif):
    """Calculate simple positional similarity between region and motif (0~1)."""
    region = region[:len(motif)]
    if len(region) != len(motif) or len(motif) == 0:
        return 0
    return sum(region[i] == motif[i] for i in range(len(region))) / len(motif)


def get_promoter_features(seq):
    """Analyze sequence (5'->3') for transcription & translation motifs."""
    seq = seq.upper()
    motifs = {
        'minus_35': ['TTGACA', 'TTGAAA', 'CTTGAC'],
        'minus_10': ['TATAAT', 'TATGAT', 'TATACT'],
        'SD': [
            'AGGAGG', 'GGAGG', 'AAGGAGG', 'AGGA',
            'GGAG', 'AAGGA', 'GAGGTT', 'AAAGGAGG'
        ],
        'AUG': ['ATG', 'GTG', 'TTG']
    }

    # Start codon search
    aug_pos = -1
    for codon in motifs['AUG']:
        pos = seq.rfind(codon)
        if pos > aug_pos:
            aug_pos = pos

    # If no start codon, use end of sequence
    if aug_pos == -1:
        aug_pos = len(seq)
        no_start_codon = True
    else:
        no_start_codon = False

    # Upstream regions
    region_10 = seq[max(aug_pos - 12, 0):max(aug_pos - 6, 0)]
    region_35 = seq[max(aug_pos - 40, 0):max(aug_pos - 34, 0)]
    SD_region = seq[max(aug_pos - 15, 0):max(aug_pos - 5, 0)]

    # Motif similarity
    score_10 = max((similarity(region_10, m) for m in motifs['minus_10']), default=0)
    score_35 = max((similarity(region_35, m) for m in motifs['minus_35']), default=0)
    SD_score = max((similarity(SD_region, m) for m in motifs['SD']), default=0)

    # AU-rich enhancer & purine content
    enhancer_window = seq[max(aug_pos - 20, 0):max(aug_pos - 13, 0)]
    AU_rich_enhancer = (
        (enhancer_window.count('A') + enhancer_window.count('T')) / len(enhancer_window)
        if enhancer_window else 0
    )
    purine_content = (
        (SD_region.count('A') + SD_region.count('G')) / len(SD_region)
        if SD_region else 0
    )

    # Probability calculations
    transcription_percent = ((score_35 + score_10) / 2) * 100
    translation_percent = ((0.5 * SD_score + 0.3 * AU_rich_enhancer + 0.2 * purine_content)) * 100
    both_percent = (transcription_percent * translation_percent) / 100

    return {
        'input_length': len(seq),
        'no_start_codon': no_start_codon,
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
        'both_transcription_and_translation(%)': round(both_percent, 2)
    }


def predict_translation_efficiency(seq):
    """Wrapper for pretty-printed results."""
    result = get_promoter_features(seq)
    report = []
    report.append("===== 🔬 Promoter / Translation Motif Analysis =====")
    report.append(f"Input length: {result['input_length']} bp")
    report.append(f"Start codon: {'❌ Not found' if result['no_start_codon'] else '✅ Found'}")
    report.append("")
    report.append(f"-35 box region: {result['-35_box_region']}")
    report.append(f"-35 similarity: {result['-35_box_similarity']}")
    report.append(f"-10 box region: {result['-10_box_region']}")
    report.append(f"-10 similarity: {result['-10_box_similarity']}")
    report.append(f"SD region: {result['SD_region']}")
    report.append(f"SD similarity: {result['SD_similarity']}")
    report.append(f"Purine content (SD): {result['purine_content(SD)']}")
    report.append(f"Enhancer region: {result['enhancer_region']}")
    report.append(f"AU-rich enhancer: {result['AU_rich_enhancer']}")
    report.append("")
    report.append(f"🧬 Transcription probability (%): {result['transcription_probability(%)']}")
    report.append(f"🧫 Translation probability (%): {result['translation_probability(%)']}")
    report.append(f"🧩 Both (Transcription × Translation) (%): {result['both_transcription_and_translation(%)']}")
    report.append("====================================================")
    return "\n".join(report)

# -------------------- UI Setup --------------------

seq_input = Text(
    value='',
    placeholder="예: ATCGTTAGC...",
    description="5'→3' 서열:",
    layout={'width': '80%'}
)
btn = Button(description="🔍 분석 실행", button_style='success')
out = Output()

def on_button_click(b):
    with out:
        out.clear_output()
        seq = seq_input.value.strip()
        if not seq:
            print("❗ 서열을 입력해주세요.")
            return
        print(predict_translation_efficiency(seq))

btn.on_click(on_button_click)
display(VBox([seq_input, btn, out]))

