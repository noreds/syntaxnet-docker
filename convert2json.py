import json
import pandas as pd
import numpy as np

fname_in = "example_output.txt"
fname_out = "example_output.json"


df = pd.read_csv(fname_in, sep='\t', header=None)


df_words = df[1]
df_type1 = df[3]
df_type2 = df[4]

pos_dots = np.where(np.array(df_type1.str.find(".")) == 0)

sentences = []
last_dot_pos = -1
for dot_pos in pos_dots[0]:
    words = []
    for i in range(last_dot_pos+1, dot_pos+1):
        words.append({"name" : df_words[i], "type1" : df_type1[i], "type2" : df_type2[i]})
    last_dot_pos = dot_pos
    sentences.append({"words" : words})


data = {"output" : {"sentences" : sentences}}

with open(fname_out, 'w') as f:
    json_data = json.dump(data, f)

"""
pen(fname_in) as f:
    lines = f.readlines()


data = {"output" : {"sentences" : [{"words": [{"name" : "I", "type1" : "PRON", "type2" : "PRP"}]}, {}] }}

with open(fname_out, 'w') as f:
    json_data = json.dumps(data, f)


print("Done")




1	I	_	PRON	PRP	_	0		_	_
2	love	_	VERB	VBP	_	0		_	_
3	myself.	_	.	,	_	0		_	_


4	You	_	PRON	PRP	_	0		_	_
5	and	_	CONJ	CC	_	0		_	_
6	I	_	PRON	PRP	_	0		_	_
7	are	_	VERB	VBP	_	0		_	_
8	a	_	DET	DT	_	0		_	_
9	time	_	NOUN	NN	_	0		_	_
10	which	_	DET	WDT	_	0		_	_
11	performs	_	VERB	VBZ	_	0		_	_
12	well	_	ADV	RB	_	0		_	_
13	.	_	.	.	_	0		_	_
"""
