from main import *

c7 = init_file("sequence.fasta")

seq = sequence_nucleotid_UFRGS("00242276")
lst_s = create_different_sequences_E(seq)
d = analyse_dna_seq(lst_s,c7)
print(d)
