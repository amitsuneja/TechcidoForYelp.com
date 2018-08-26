# import food
# counter = 1
# list_of_report = food.get_reports()
#
# for item in list_of_report:
# 	print(item["Description"])
import nltk
from nltk.corpus import wordnet as wn
nltk.data.path.append('./nltk_data/')


food = wn.synset('food.n.02')
for item in list(set([w for s in food.closure(lambda s:s.hyponyms()) for w in s.lemma_names()])):
	print(item)