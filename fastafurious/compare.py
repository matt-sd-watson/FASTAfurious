from Bio import SeqIO
from itertools import product
import pandas as pd

# compare the headers of two FASTAs to provide content summaries

fasta_1 = "/home/mwatson/COVID-19/one_off/Oct_2021/01_10_21/with_c23059t_mut.fa"

fasta_2 = "/home/mwatson/COVID-19/master_fasta/complete_all_27-Sep-2021-09-14.fa"

fasta_1_read = SeqIO.parse(open(fasta_1), 'fasta')

fasta_2_read = SeqIO.parse(open(fasta_2), 'fasta')

fasta_1_names = [record.name for record in fasta_1_read]

fasta_2_names = [record.name for record in fasta_2_read]

d = []

for i, j in product(fasta_1_names, fasta_2_names):
    d.append([i, j])

df = pd.DataFrame(d, columns=["fasta_1", "fasta_2"])

same_entries = df[df.fasta_1 == df.fasta_2]

different_entries = df[df.fasta_1 != df.fasta_2]

print(same_entries)
print(different_entries)


