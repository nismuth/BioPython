# Transcriplation: with input FASTA file transcribes DNA to RNA, then translates RNA to protein

from Bio import SeqIO

while True:  # While loop needed for return to start
    # Ask user for FASTA file name
    fasta_file = input("\nEnter FASTA file name (with extension): ").strip()
    if ".fasta" not in fasta_file:
        print("Not a usable file type.")
        continue

    # Read the first record from the FASTA file
    record = next(SeqIO.parse(fasta_file, "fasta"))
    dna_seq = record.seq

    # Trim the sequence to a multiple of 3
    trimmed_seq = dna_seq[:len(dna_seq) - len(dna_seq) % 3]

    # Transcription (DNA to mRNA)
    rna_seq = trimmed_seq.transcribe()
    print("\nRNA Sequence:", rna_seq)

    # Translation (mRNA to Protein)
    protein_seq = rna_seq.translate()
    print("Protein Sequence:", protein_seq)

    fin_choice = input("\nWould you live to analyze another file? (Y/N): ").upper()

    if fin_choice == "Y":
        continue
    if fin_choice == "N":
        break
