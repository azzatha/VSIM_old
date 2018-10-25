import json, random
import pandas as pd
import numpy as np
import sys

fileName = sys.argv[-1]

annots = []

AllData = pd.read_table("./VisFiles/ToJsonChild_"+str(fileName)+".txt",  sep=" ")
# print(len(AllData[AllData['chr'] == 'Y']))
chrs = [
	 "1", "2", "3", "4", "5","6","7","8","9",
	 "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
	 "21", "22","X","Y"
]
ch1 = 1
ch2 = 1
ch3 = 1
ch4 = 1
ch5 = 1
ch6 = 1
ch7 = 1
ch8 = 1
ch9 = 1
ch10 = 1
ch11 = 1
ch12 = 1
ch13 = 1
ch14 = 1
ch15 = 1
ch16 = 1
ch17 = 1
ch18 = 1
ch19 = 1
ch20 = 1
ch21 = 1
ch22 = 1
chX = 1
chY = 1


lengths_GRCh38 = {
	"1": 248956422, "2": 242193529, "3": 198295559,
	"4": 190214555, "5": 181538259, "6": 170805979,
	"7": 159345973, "8": 145138636, "9": 138394717,
	"10": 133797422, "11": 135086622, "12": 133275309,
	"13": 114364328, "14": 107043718, "15": 101991189,
	"16": 90338345,	"17": 83257441, "18": 80373285,
	"19": 58617616, "20": 64444167, "21": 46709983,
	"22": 50818468, "X": 156040895, "Y": 57227415
}
#
lengths_GRCh37 = {
	"1": 249250621, "2": 243199373, "3": 198022430,
	"4": 191154276, "5": 180915260, "6": 171115067,
	"7": 159138663, "8": 146364022, "9": 141213431,
	"10": 135534747, "11": 135006516, "12": 133851895,
	"13": 115169878, "14": 107349540, "15": 102531392,
	"16": 90354753, "17": 81195210, "18": 78077248,
	"19": 59128983, "20": 63025520, "21": 48129895,
	"22": 51304566, "X": 155270560, "Y": 59373566
}

for chr in chrs:
	annots.append({"chr": chr, "annots":[]})

i = 0

while i < len(AllData):
	# j = str(i + 1)
	chr = i % 24
	# print(chr)
	# start = int((i * lengths_GRCh37[chrs[chr]])/37 + 1)

	if (AllData['chr'][i] == 1):
		chrlength1 = len(AllData[AllData['chr'] == 1])
		if (ch1 != chrlength1):
			# a = int((ch1 * lengths_GRCh37[chrs[0]])/chrlength1 + 1)#100
			a = int((ch1 * lengths_GRCh37[chrs[0]])/chrlength1 + 1)
			annot = [
				AllData['info'][i]+'\n'+
				'<a target=\"_blank\" href=\"'+AllData['Link'][i]+'\">'+'More Info'+'</a>' ,
				AllData['pos'][i],
				AllData['len'][i],
				AllData['trackIndex'][i],
				AllData['Likelihood'][i]
			]
			annots[0]["annots"].append(annot)
			ch1 += 1

	if (AllData['chr'][i] == 2):
		chrlength2 = len(AllData[AllData['chr'] == 2])
		if (ch2 != chrlength2):
			b = int((ch2 * lengths_GRCh37[chrs[1]])/chrlength2 + 1)#100
			annot = [
				AllData['info'][i]+'\n'+
				'<a target=\"_blank\" href=\"'+AllData['Link'][i]+'\">'+'More Info'+'</a>' ,
				AllData['pos'][i],
				AllData['len'][i],
				AllData['trackIndex'][i],
				AllData['Likelihood'][i]

			]
			annots[1]["annots"].append(annot)
			ch2 += 1
			

	if (AllData['chr'][i] == 3):
		chrlength3 = len(AllData[AllData['chr'] == 3])
		if (ch3 != chrlength3):
			c = int((ch3 * lengths_GRCh37[chrs[2]])/chrlength3 + 1)#100
			annot = [
				AllData['info'][i]+'\n'+'<a target=\"_blank\" href=\"'+AllData['Link'][i]+'\">'+'More Info'+'</a>' ,
				AllData['pos'][i],
				AllData['len'][i],
				AllData['trackIndex'][i],
				AllData['Likelihood'][i]
			]
			annots[2]["annots"].append(annot)
			ch3 += 1


	if (AllData['chr'][i] == 4):
		chrlength4 = len(AllData[AllData['chr'] == 4])
		if (ch4 != chrlength4):
			d = int((ch4 * lengths_GRCh37[chrs[3]])/chrlength4 + 1) 
			annot = [
				AllData['info'][i]+'\n'+'<a target=\"_blank\" href=\"'+AllData['Link'][i]+'\">'+'More Info'+'</a>' ,
				AllData['pos'][i],
				AllData['len'][i],
				AllData['trackIndex'][i],
				AllData['Likelihood'][i]
			]
			annots[3]["annots"].append(annot)
			ch4 += 1


	if (AllData['chr'][i] == 5):
		chrlength5 = len(AllData[AllData['chr'] == 5])
		if (ch5 != chrlength5):
			e = int((ch5 * lengths_GRCh37[chrs[4]])/chrlength5 + 1)#100
			annot = [
				AllData['info'][i]+'\n'+'<a target=\"_blank\" href=\"'+AllData['Link'][i]+'\">'+'More Info'+'</a>' ,
				AllData['pos'][i],
				AllData['len'][i],
				AllData['trackIndex'][i],
				AllData['Likelihood'][i]
			]
			annots[4]["annots"].append(annot)
			ch5 += 1

	if (AllData['chr'][i] == 6):
		chrlength6 = len(AllData[AllData['chr'] == 6])
		if (ch6 != chrlength6):
			f = int((ch6 * lengths_GRCh37[chrs[5]])/chrlength6 + 1) #100
			annot = [
				AllData['info'][i]+'\n'+'<a target=\"_blank\" href=\"'+AllData['Link'][i]+'\">'+'More Info'+'</a>' ,
				AllData['pos'][i],
				AllData['len'][i],
				AllData['trackIndex'][i],
				AllData['Likelihood'][i]
			]
			annots[5]["annots"].append(annot)
			ch6+=1

	if (AllData['chr'][i] == 7):
		chrlength7 = len(AllData[AllData['chr'] == 7])
		if (ch7 != chrlength7 ):
			g = int((ch7 * lengths_GRCh37[chrs[6]])/chrlength7 + 1 ) #200
			annot = [
				AllData['info'][i]+'\n'+'<a target=\"_blank\" href=\"'+AllData['Link'][i]+'\">'+'More Info'+'</a>' ,
				AllData['pos'][i],
				AllData['len'][i],
				AllData['trackIndex'][i],
				AllData['Likelihood'][i]
			]
			annots[6]["annots"].append(annot)
			ch7+=1

	if (AllData['chr'][i] == 8):
		chrlength8 = len(AllData[AllData['chr'] == 8])
		if (ch8 != chrlength8 ):
			h = int((ch8 * lengths_GRCh37[chrs[7]])/chrlength8 + 1 ) #200
			annot = [
				AllData['info'][i]+'\n'+'<a target=\"_blank\" href=\"'+AllData['Link'][i]+'\">'+'More Info'+'</a>' ,
				AllData['pos'][i],
				AllData['len'][i],
				AllData['trackIndex'][i],
				AllData['Likelihood'][i]
			]
			annots[7]["annots"].append(annot)
			ch8+=1

	if (AllData['chr'][i] == 9):
		chrlength9 = len(AllData[AllData['chr'] == 9])
		if (ch9 != chrlength9 ):
			z = int((ch9 * lengths_GRCh37[chrs[8]])/chrlength9 + 1) 
			annot = [
				AllData['info'][i]+'\n'+'<a target=\"_blank\" href=\"'+AllData['Link'][i]+'\">'+'More Info'+'</a>' ,
				AllData['pos'][i],
				AllData['len'][i],
				AllData['trackIndex'][i],
				AllData['Likelihood'][i]
			]
			annots[8]["annots"].append(annot)
			ch9+=1

	if (AllData['chr'][i] == 10):
		chrlength10 = len(AllData[AllData['chr'] == 10])
		if( ch10 != chrlength10 ):
			j = int((ch10 * lengths_GRCh37[chrs[9]])/chrlength10 +1 )#60
			annot = [
				AllData['info'][i]+'\n'+'<a target=\"_blank\" href=\"'+AllData['Link'][i]+'\">'+'More Info'+'</a>' ,
				AllData['pos'][i],
				AllData['len'][i],
				AllData['trackIndex'][i],
				AllData['Likelihood'][i]
			]
			annots[9]["annots"].append(annot)
			ch10+=1


	if (AllData['chr'][i] == 11):
		chrlength11 = len(AllData[AllData['chr'] == 11])
		if (ch11 != chrlength11):
			k = int((ch11 * lengths_GRCh37[chrs[10]])/chrlength11 + 1 )
			annot = [
				AllData['info'][i]+'\n'+'<a target=\"_blank\" href=\"'+AllData['Link'][i]+'\">'+'More Info'+'</a>' ,
				AllData['pos'][i],
				AllData['len'][i],
				AllData['trackIndex'][i],
				AllData['Likelihood'][i]
			]
			annots[10]["annots"].append(annot)
			ch11+=1


	if (AllData['chr'][i] == 12):
		chrlength12 = len(AllData[AllData['chr'] == 12])
		if (ch12 != chrlength12):
			l = int((ch12 * lengths_GRCh37[chrs[11]])/chrlength12 + 1 )
			annot = [
				AllData['info'][i]+'\n'+'<a target=\"_blank\" href=\"'+AllData['Link'][i]+'\">'+'More Info'+'</a>' ,
				AllData['pos'][i],
				AllData['len'][i],
				AllData['trackIndex'][i],
				AllData['Likelihood'][i]
			]
			annots[11]["annots"].append(annot)
			ch12+=1


	if (AllData['chr'][i] == 13):
		chrlength13 = len(AllData[AllData['chr'] == 13])
		if (ch13 != chrlength13 ):
			m = int((ch13 * lengths_GRCh37[chrs[12]])/chrlength13 + 1  )
			annot = [
				AllData['info'][i]+'\n'+'<a target=\"_blank\" href=\"'+AllData['Link'][i]+'\">'+'More Info'+'</a>' ,
				AllData['pos'][i],
				AllData['len'][i],
				AllData['trackIndex'][i],
				AllData['Likelihood'][i]
			]
			annots[12]["annots"].append(annot)
			ch13+=1


	if (AllData['chr'][i] == 14):
		chrlength14 = len(AllData[AllData['chr'] == 14])
		if (ch14 != chrlength14):
			n = int((ch14 * lengths_GRCh37[chrs[13]])/chrlength14 + 1  )
			annot = [
				AllData['info'][i]+'\n'+'<a target=\"_blank\" href=\"'+AllData['Link'][i]+'\">'+'More Info'+'</a>' ,
				AllData['pos'][i],
				AllData['len'][i],
				AllData['trackIndex'][i],
				AllData['Likelihood'][i]
			]
			annots[13]["annots"].append(annot)
			ch14+=1


	if (AllData['chr'][i] == 15):
		chrlength15 = len(AllData[AllData['chr'] == 15])
		if (ch15 != chrlength15):
			o = int((ch15 * lengths_GRCh37[chrs[14]])/chrlength15 + 1  )
			annot = [
				AllData['info'][i]+'\n'+'<a target=\"_blank\" href=\"'+AllData['Link'][i]+'\">'+'More Info'+'</a>' ,
				AllData['pos'][i],
				AllData['len'][i],
				AllData['trackIndex'][i],
				AllData['Likelihood'][i]
			]
			annots[14]["annots"].append(annot)
			ch15+=1


	if (AllData['chr'][i] == 16):
		chrlength16 = len(AllData[AllData['chr'] == 16])
		if (ch16 != chrlength16):
			p = int((ch16 * lengths_GRCh37[chrs[15]])/chrlength16 + 1  )
			annot = [
				AllData['info'][i]+'\n'+'<a target=\"_blank\" href=\"'+AllData['Link'][i]+'\">'+'More Info'+'</a>' ,
				AllData['pos'][i],
				AllData['len'][i],
				AllData['trackIndex'][i],
				AllData['Likelihood'][i]
			]
			annots[15]["annots"].append(annot)
			ch16+=1


	if (AllData['chr'][i] == 17):
		chrlength17 = len(AllData[AllData['chr'] == 17])
		if (ch17 != chrlength17 ):
			q = int((ch17 * lengths_GRCh37[chrs[16]])/chrlength17 + 1  )
			annot = [
				AllData['info'][i]+'\n'+'<a target=\"_blank\" href=\"'+AllData['Link'][i]+'\">'+'More Info'+'</a>' ,
				AllData['pos'][i],
				AllData['len'][i],
				AllData['trackIndex'][i],
				AllData['Likelihood'][i]
			]
			annots[16]["annots"].append(annot)
			ch17 +=1

	if (AllData['chr'][i] == 18):
		chrlength18 = len(AllData[AllData['chr'] == 18])
		if (ch18 !=chrlength18 ):
			r = int((ch18 * lengths_GRCh37[chrs[17]])/chrlength18 + 1  )
			annot = [
				AllData['info'][i]+'\n'+'<a target=\"_blank\" href=\"'+AllData['Link'][i]+'\">'+'More Info'+'</a>' ,
				AllData['pos'][i],
				AllData['len'][i],
				AllData['trackIndex'][i],
				AllData['Likelihood'][i]
			]
			annots[17]["annots"].append(annot)
			ch18+=1

	if (AllData['chr'][i] == 19):
		chrlength19 = len(AllData[AllData['chr'] == 19])
		if (ch19 != chrlength19):
			s = int((ch19 * lengths_GRCh37[chrs[18]])/chrlength19 + 1 )
			annot = [
				AllData['info'][i]+'\n'+'<a target=\"_blank\" href=\"'+AllData['Link'][i]+'\">'+'More Info'+'</a>' ,
				AllData['pos'][i],
				AllData['len'][i],
				AllData['trackIndex'][i],
				AllData['Likelihood'][i]
			]
			annots[18]["annots"].append(annot)
			ch19+=1


	if (AllData['chr'][i] == 20):
		chrlength20 = len(AllData[AllData['chr'] == 20])
		if (ch20 != chrlength20):
			t = int((ch20 * lengths_GRCh37[chrs[19]])/chrlength20 + 1 )
			annot = [
				AllData['info'][i]+'\n'+'<a target=\"_blank\" href=\"'+AllData['Link'][i]+'\">'+'More Info'+'</a>' ,
				AllData['pos'][i],
				AllData['len'][i],
				AllData['trackIndex'][i],
				AllData['Likelihood'][i]
			]
			annots[19]["annots"].append(annot)
			ch20+=1

	if (AllData['chr'][i] == 21):
		chrlength21 = len(AllData[AllData['chr'] == 21])
		if (ch21 != chrlength21):
			u = int((ch21 * lengths_GRCh37[chrs[20]])/chrlength21 + 1 )
			annot = [
				AllData['info'][i]+'\n'+'<a target=\"_blank\" href=\"'+AllData['Link'][i]+'\">'+'More Info'+'</a>' ,
				AllData['pos'][i],
				AllData['len'][i],
				AllData['trackIndex'][i],
				AllData['Likelihood'][i]
			]
			annots[20]["annots"].append(annot)
			ch21+=1


	if (AllData['chr'][i] == 22):
		chrlength22 = len(AllData[AllData['chr'] == 22])
		if (ch22 != chrlength22):
			v = int((ch22 * lengths_GRCh37[chrs[21]])/chrlength22 + 1  )
			annot = [
				AllData['info'][i]+'\n'+'<a target=\"_blank\" href=\"'+AllData['Link'][i]+'\">'+'More Info'+'</a>' ,
				AllData['pos'][i],
				AllData['len'][i],
				AllData['trackIndex'][i],
				AllData['Likelihood'][i]
			]
			annots[21]["annots"].append(annot)
			ch22+=1


	if (AllData['chr'][i] == 'X'):
		chrlength23 = len(AllData[AllData['chr'] == 'X'])
		if (chX != chrlength23):
			w = int((chX * lengths_GRCh37[chrs[22]])/chrlength23 + 1 )
			annot = [
				AllData['info'][i]+'\n'+'<a target=\"_blank\" href=\"'+AllData['Link'][i]+'\">'+'More Info'+'</a>' ,
				AllData['pos'][i],
				AllData['len'][i],
				AllData['trackIndex'][i],
				AllData['Likelihood'][i]
			]
			annots[22]["annots"].append(annot)
			chX +=1 


	if (AllData['chr'][i] == 'Y'):
		chrlength24 = len(AllData[AllData['chr'] == 'X'])
		if (chY != chrlength24):
			x = int((chY * lengths_GRCh37[chrs[23]])/chrlength24 + 1)
			annot = [
				AllData['info'][i]+'\n'+'<a target=\"_blank\" href=\"'+AllData['Link'][i]+'\">'+'More Info'+'</a>' ,
				AllData['pos'][i],
				AllData['len'][i],
				AllData['trackIndex'][i],
				AllData['Likelihood'][i]
			]
			annots[23]["annots"].append(annot)
			chY += 1

	i += 1

top_annots = {}
top_annots["keys"] = ["name", "start", "length", "trackIndex","Likelihood"]
top_annots["annots"] = annots
#annots=json.dumps(top_annots.serialize())

def default(o):
    if isinstance(o, np.int64): return int(o)
    raise TypeError

annots = json.dumps(top_annots, default=default,indent=4)

#annots = json.dumps(top_annots, indent=4)
print(annots)