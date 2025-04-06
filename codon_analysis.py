from Bio import SeqIO
from collections import defaultdict


def get_codon_usage(fasta_file):
    codon_counts = defaultdict(int)
    total_codons = 0

    for record in SeqIO.parse(fasta_file, "fasta"):
        seq = record.seq.upper()

        # Make sure length is a multiple of 3
        seq = seq[:len(seq) - len(seq) % 3]

        for i in range(0, len(seq), 3):
            codon = str(seq[i:i + 3])
            if len(codon) == 3:
                codon_counts[codon] += 1
                total_codons += 1

    # Normalize to frequency
    codon_freq = {codon: count / total_codons for codon, count in codon_counts.items()}

    return codon_freq


# Example usage
codon_usage = get_codon_usage("sequence.fasta")
for codon, freq in sorted(codon_usage.items()):
    print(f"{codon}: {freq:.4f}")
