import json

with open("OpenEnded_mscoco_co-atten_results.json", 'r') as f:
	data_1 = json.load(f)

with open("data/all_qs_dict_release.json", 'r') as f:
	data_2 = json.load(f)

# loss = 0
acc_1 = 0

answers = {}
 
for item in data_1:
	answers[item['question_id']] = item['answer']

for key,val in data_2.iteritems():
	"""Fixing lower case"""
	val['answer'] = val['answer'].lower()

	"""Fixing plurals and random spaces in the beginning"""
	if answers[int(key)] == str(val['answer']) or answers[int(key)] == str(val['answer'][:-1]) or answers[int(key)][:-1] == str(val['answer']) or answers[int(key)][1:] == str(val['answer']) or answers[int(key)] == str(val['answer'][1:]):
		acc_1 = acc_1 + 1
	else:
		print(val['answer'], answers[int(key)])

print(len(data_1), len(data_2), acc_1)
print('FVQA data has TOP-1 classif. accuracy %f percent' \
		% ((acc_1*100.)/(len(data_1))))