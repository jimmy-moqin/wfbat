# 蛋白序列文件路径
PROTEINS_FILE_PATH = []
# 允许的蛋白序列格式
ALLOW_PROTEIN_FORMAT = ['fasta', 'fastq']

# 蛋白序列对齐输出格式设置
PROTEIN_ALIGN_INLINE = 60
PROTEIN_ALIGN_BLOCK = 10
BLANKLINES = 1

# 氨基酸缩写全称以及分子量
AMINOACIDS = {
    "A": ("Ala", "Alanine",71.0788),
    "C": ("Cys", "Cysteine", 103.1429),
    "D": ("Asp", "Aspartic acid", 115.0874),
    "E": ("Glu", "Glutamic acid", 129.1155),
    "F": ("Phe", "Phenylalanine", 147.1766),
    "G": ("Gly", "Glycine", 57.0519),
    "H": ("His", "Histidine", 137.1411),
    "I": ("Ile", "Isoleucine", 113.1594),
    "K": ("Lys", "Lysine", 128.1741),
    "L": ("Leu", "Leucine", 113.1594),
    "M": ("Met", "Methionine", 131.1926),
    "N": ("Asn", "Asparagine", 114.1039),
    "P": ("Pro", "Proline", 97.1167),
    "Q": ("Gln", "Glutamine", 128.1307),
    "R": ("Arg", "Arginine", 156.1875),
    "S": ("Ser", "Serine", 87.0782),
    "T": ("Thr", "Threonine", 101.1051),
    "V": ("Val", "Valine", 99.1326),
    "W": ("Trp", "Tryptophan", 186.2132),
    "Y": ("Tyr", "Tyrosine", 163.1760),
    "O": ("Pyl", "Pyrrolysine", 165.1890),
    "U": ("Sec", "Selenocysteine", 150.0379),
    "X": ("", "Unknown", 111.3248),
    "Z": ("", "Glutamine or Glutamic acid", 128.746),
    "B": ("", "Asparagine or Aspartic acid", 114.6448),
}