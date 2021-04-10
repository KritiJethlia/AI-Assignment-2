import pickle

def give_names(func):
	if func == 'journal':
		with open('cat_journal', 'rb') as file:
			cat_func = pickle.load(file)
		
		with open('journal_info', 'rb') as file:
			func_info = pickle.load(file)

	else:
		with open('cat_conference', 'rb') as file:
			cat_func = pickle.load(file)
		
		with open('conference_info', 'rb') as file:
			func_info = pickle.load(file)

	funcs = set()
	for key in cat_func.keys():
		funcs = funcs.union(cat_func[key])


	return list(cat_func.keys()), funcs

if __name__ == '__main__':
	categories, journals = give_names('jounal')
	print(categories)