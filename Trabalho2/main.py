from init import *

match_award = 5
mismatch_penalty = -3
gap_penalty = -4

def init_matrix(n,m):
	M = []
	
	for i in range(0,len(n)+1):
		for j in range(0,len(m)+1):
			M[i][j] = 0
			
	for i in range(0,len(n)+1):
		score[i][0] = gap_penalty * i
	for j in range (0,len(m)+1):
		score[0][j] = gap_penalty * j
		
	return M

def match_score(alpha,beta):
	if alpha == beta:
		return match_award
	elif alpha == "-" or beta == "-":
		return gap_penalty
	else:
		return mismatch_penalty

def needle(seq1,seq2):
	score = init_matrix(seq1,seq2)

def main():
	human = init_file("human.fasta")
	deer = init_file("deer.fasta")
	pig = init_file("pig.fasta")
	wolf = init_file("wolf.fasta")
	chicken = init_file("chicken.fasta")
	cow = init_file("cow.fasta")
	trout = init_file("trout.fasta")
	horse = init_file("horse.fasta")

