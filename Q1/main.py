import pickle 
from data_loader import *

def give_rank(potential_func, func_info, deadline, top_k):
	final_list = []
	if deadline is not None:
		for func in potential_func:
			if func_info[func.lower()][2]<=deadline:
				final_list.append(func)

	else:
		final_list = potential_func[:]

	final_list.sort(reverse = True, key = lambda x:func_info[x.lower()][1]-func_info[x.lower()][0])
	return final_list[:top_k]


def give_functions(functions, cat_func, top_k):
	potential_func = []
	
	for j in range(len(functions)):
		temp = set()
		for i in range(len(functions)-j):
			temp = temp.union(functions[i])

		potential_func.extend(list(temp)[:])	
		# print("potential func",potential_func)
		# print("temp",temp)
		
		if len(potential_func)>=2*top_k:	
			return potential_func
	
	# print(potential_func)
	return potential_func



def give_ans(func_type, keywords, deadline, top_k):
	if func_type == 'journal':
		with open('cat_journal', 'rb') as file:
			cat_func = pickle.load(file)
		
		with open('journal_info', 'rb') as file:
			func_info = pickle.load(file)

	else:
		with open('cat_conference', 'rb') as file:
			cat_func = pickle.load(file)
		
		with open('conference_info', 'rb') as file:
			func_info = pickle.load(file)


	functions = []
	for keyword in keywords:
		functions.append(cat_func[keyword.lower()])

	# print("functions",functions)
	potential_func = give_functions(functions, cat_func, top_k)
	ranked_func = give_rank(potential_func, func_info, deadline, top_k)
	ranked_info = [func_info[i.lower()] for i in ranked_func]
	
	return ranked_func, ranked_info



if __name__ == '__main__':
	ranked_func, ranked_info = give_ans('conference', ['analysis'], None, 5)
	print(ranked_func)
	print(ranked_info)