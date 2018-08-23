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

def traceback(s1,s2,score):
	align1,align2 = '',''
	i,j = len(s1),len(s2)
	while i>0 and j>0:
		score_current = score[i][j]
		score_diagonal = score[i-1][j-1]
		score_up = score[i][j-1]
		score_left = score[i-1][j]
		if score_current == score_diagonal + match_score(s1[i-1],s2[j-1]):
			align1 += s1[i-1]
			align2 += s2[j-1]
			i -= 1
			j -= 1
		elif score_current == score_left + gap_penalty:
			align1 += s1[i-1]
			align2 += "-"
			i -= 1
		elif score_current == score_up + gap_penalty:
			align1 += "-"
			align2 += s2[j-1]
			j -= 1

	while i>0:
		align1 += s1[i-1]
		align2 += "-"
		i -= 1
	while j>0:
		align1 += '-'
		align2 += s2[j-1]
		j -= 1
	finalize(align1,align2)

def finalize(a1,a2):
	a1 = a1[::-1]
	a2 = a2[::-1]

	i,j = 0,0

	symbol=''
	found = 0
	score = 0
	identity = 0
	for i in range(0,len(a1)):
		if a1[i] == a2[i]:
			symbol = symbol+a1[1]
			identity += 1
		elif a1[i] != a2[i] and a1!="-" and a2!="-":
			score+=match_score(a1[i],a2[i])
			symbol+=' '
			score+=gap_penalty
		elif a1[i] == 	"-" or a2[i] == "-":
			symbol+=' '
			score+=gap_penalty
	identity = float(identity)/len(a1) * 100

	print("Identity = %f percent" % identity)
	print("Score = " +str(score))
	print (a1)
	print (symbol)
	print (a2)


def needle(seq1,seq2):
	score = init_matrix(seq1,seq2)
	traceback(seq1,seq2,score)

def main():
	i = 0
	lst_animals =["deer","pig","wolf","chicken","cow","trout","horse"]
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
	for animal in lst_comp:
		needle(human,animal)
		print(lst_animals[i])
		print("\n")
		i += 1

main()
