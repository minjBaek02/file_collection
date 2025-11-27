import pandas as pd

df = pd.read_csv("genome_cog_category_counts.tsv", sep="\t")

with open("itol_cog_bar.txt", "w") as f:
    f.write("DATASET_BAR\nSEPARATOR TAB\nDATASET_LABEL\taccessory COG profile\nCOLOR\t#ffcc00\n\n")
    f.write("FIELD_LABELS\t" + "\t".join(df.columns[1:]) + "\n")
    # 예시 색상 정해서 넣기(자동 랜덤 혹은 일괄)
    f.write("FIELD_COLORS\t" + "\t".join(["#"+str(hex(3887+i*250))[2:8] for i in range(len(df.columns[1:]))]) + "\n")
    f.write("DATA\n")
    for _, row in df.iterrows():
        f.write(row['genome'] + "\t" + "\t".join(map(str, row[1:])) + "\n")

