def init_file(filename):
	with open(filename) as f:
		content = f.read().splitlines()
		f.close()
	return content

