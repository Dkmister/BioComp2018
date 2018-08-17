def substring_occurence(string,substring):
	occurence_substring = string.find(substring)
	if occurence_substring == -1:
		print("Substring not found!\n")
	else:
		print("Substring found in index: " + str(occurence_substring) + " until index: " + str(occurence_substring + len(substring)-1) )
