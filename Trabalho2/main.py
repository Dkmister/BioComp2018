from init import *

match_award = 5
mismatch_penalty = -3
gap_penalty = -4

def init_matrix(s1,s2):

	m,n = len(s1),len(s2)
	score = [[0 for x in range(n+1)] for y in range(m+1)]
	for i in range(0,m+1):
		score[i][0] = gap_penalty * i
	for j in range (0,n+1):
		score[0][j] = gap_penalty * j
	for i in range(1,m+1):
		for j in range(1,n+1):
			match = score[i-1][j-1] + match_score(s1[i-1],s2[j-1])
			delete = score[i-1][j] + gap_penalty
			insert = score[i][j-1] + gap_penalty
			score[i][j] = max(match,delete,insert)
	return score

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
	score = []
	human = init_file("human.fasta")
	deer = init_file("deer.fasta")
	pig = init_file("pig.fasta")
	wolf = init_file("wolf.fasta")
	chicken = init_file("chicken.fasta")
	cow = init_file("cow.fasta")
	trout = init_file("trout.fasta")
	horse = init_file("horse.fasta")
	
	lst_comp = []
	lst_comparisons = [deer,pig,wolf,chicken,cow,trout,horse]
	for animal in lst_comparisons:
		animal = ''.join(animal)
		lst_comp.append(animal)

	human = ''.join(human)

	del lst_comparisons
	
	#needle(human,lst_comp[0])

main()
