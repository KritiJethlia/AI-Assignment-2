import pandas as pd
from collections import defaultdict
from tqdm import tqdm
import pickle
import numpy as np
import re

def data_loader():
	data = pd.read_csv("dataset.csv", delimiter = ';', usecols = ['Rank', 'Title', 'Type', 'Categories','Cites / Doc. (2years)'])
	# print(data['Cites / Doc. (2years)'].head())
	cat_conference = defaultdict(set)
	cat_journal = defaultdict(set)
	journal_info = defaultdict(list)
	conference_info = defaultdict(list)

	for i in tqdm(range(len(data))):
		if data.iloc[i]['Type'] == 'journal':
			name = data.iloc[i]['Title']
			categories = data.iloc[i]['Categories'].split(';')
			for i, category in enumerate(categories):
				category = re.sub(r'\s*\(Q\d\)\s*', '', category)
				category = category.strip(' ')
				categories[i] = category

			info = [data.iloc[i]['Rank'], int(data.iloc[i]['Cites / Doc. (2years)'].split(',')[0]), np.random.randint(1,12)]
			
			for category in categories:
				cat_journal[category.lower()].add(name)

			journal_info[name.lower()].extend(info)

		else:
			name = data.iloc[i]['Title']
			categories = data.iloc[i]['Categories'].split(';')
			
			for category in categories:
				cat_conference[category.lower()].add(name)

			info = [data.iloc[i]['Rank'], data.iloc[i]['Cites / Doc. (2years)'], np.random.randint(1,12)]
			conference_info[name.lower()].extend(info)
			

	with open('cat_conference', 'wb') as file:
		pickle.dump(cat_conference, file)

	with open('cat_journal', 'wb') as file:
		pickle.dump(cat_journal, file)

	with open('journal_info', 'wb') as file:
		pickle.dump(journal_info, file)

	with open('conference_info', 'wb') as file:
		pickle.dump(conference_info, file)


	return cat_conference, cat_journal, journal_info, conference_info

		




if __name__ == '__main__':
	cat_conference, cat_journal, journal_info, conference_info = data_loader()
	print(len(cat_journal))
	print(len(journal_info))
	print(len(cat_conference))
	print(len(conference_info))

	max_freq = [0]*5
	
	for key in cat_journal:
		length = len(cat_journal[key])
		for i in range(len(max_freq)):
			if length>max_freq[i]:
				max_freq[i] = length
				break


	print(max_freq)



