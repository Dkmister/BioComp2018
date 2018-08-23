from init import *

match_award = 1
mismatch_penalty = -1
gap_penalty = -2

def finalize(a1,a2):
	a1 = reverse_string(a1)
	a2 = reverse_string(a2)

	i,j = 0,0

	symbol=''
	found = 0
	score = 0
	identity = 0
	for i in range(0,len(a1)):
		if a1[i] == a2[i]:
			symbol = symbol+a1[1]
			identity += 1
			score += match_score(a1[i],a2[i])
		elif a1[i] != a2[i] and a1!="-" and a2!="-":
			score+=match_score(a1[i],a2[i])
			symbol+=' '
			found = 0
		elif a1[i] == 	"-" or a2[i] == "-":
			symbol+=' '
			score+=gap_penalty
	identity = float(identity)/len(a1) * 100

	print("Identity = %f percent" % identity)
	print("Score = " +str(score))
	print (a1)
	print (symbol)
	print (a2)



def reverse_string(s):
	return s[::-1]


def match_score(alpha,beta):
	if alpha == beta:
		return match_award
	elif alpha == "-" or beta == "-":
		return gap_penalty
	else:
		return mismatch_penalty

def water(s1,s2):
	m,n = len(s1),len(s2)
	score = [[0 for x in range(n+1)] for y in range(m+1)]
	pointer = score
	
	max_score = 0
	
	end_path = 0
	trace_left = 2
	trace_up = 1
	trace_diagonal = 3

	for i in range(1,m+1):
		for j in range(1,n+1):
			score_diagonal = score[i-1][j-1] + match_score(s1[i-1],s2[j-1])
			score_up = score[i][j-1] + gap_penalty
			score_left = score[i-1][j] + gap_penalty
			score[i][j] = max(0,score_diagonal,score_up,score_left)
			
			if score[i][j] == 0:
				pointer[i][j] = 0
				
			if score[i][j] == score_left:
				pointer[i][j] = trace_up
				
			if score[i][j] == score_up:
				pointer[i][j] = trace_left
				
			if score[i][j] == score_diagonal:
				pointer[i][j] = trace_diagonal 
				
			if score[i][j] >= max_score:
				max_i =	i
				max_j = j
				max_score = score[i][j]
				
	align1, align2 = '',''
	i,j = max_i, max_j
	
	while pointer[i][j] != 0:
		if pointer[i][j] == trace_diagonal:
			align1+=s1[i-1]
			align2+=s2[j-1]
			i-=1
			j-=1
		elif pointer[i][j] == trace_left:
			align1 += '-' 
			align2 += s2[j-1]
			j-=1
		elif pointer[i][j] == trace_up:
			align1 += s1[i-1]
			align2 += '-'
			i-=1
			
	finalize(align1,align2)

def main():
	water("MEKVPGEMEIERRERSEELSEAERKAVQAMWARL","MFLVKGSVVQAFVLLSIVCLETTDDGVRQYVNANLTD")

main()
