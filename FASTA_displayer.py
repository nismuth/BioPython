
from Bio import SeqIO

# Path to your FASTA file
fasta_file = input("Enter .fasta File Name: ")
if ".fasta" not in fasta_file:
    print("Not a usable file type.")

# Parse the FASTA file
for record in SeqIO.parse(fasta_file, "fasta"):
    print(f"\nID: {record.id}")
    print(f"Description: {record.description}")
    print(f"Sequence: {record.seq}")
    print("-" * 40)
