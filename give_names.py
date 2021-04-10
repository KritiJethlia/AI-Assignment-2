import pickle

def give_names():
	with open('cat_journal', 'rb') as file:
		cat_journal = pickle.load(file)
	
	with open('journal_info', 'rb') as file:
		journal_info = pickle.load(file)

	with open('cat_conference', 'rb') as file:
		cat_conference = pickle.load(file)
	
	with open('conference_info', 'rb') as file:
		conference_info = pickle.load(file)

	journals = set()
	for key in cat_journal.keys():
		journals = journals.union(cat_journal[key])

	conferences = set()
	for key in cat_conference.keys():
		conferences = conferences.union(cat_conference[key])





	return list(set(cat_journal.keys()).union(set(cat_conference.keys()))), journals, conferences

if __name__ == '__main__':
	categories, journals, conferences = give_names()
	print(conferences)