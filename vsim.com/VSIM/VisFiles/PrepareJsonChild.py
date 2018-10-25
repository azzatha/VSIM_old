import pandas as pd
import sys

fileName = sys.argv[-1]

f = open("./VisFiles/FinalChild_"+str(fileName),'r').read()
AllData = pd.DataFrame()
# Links = pd.read_csv("./1-ClinVar/Link_"+str(fileName)+".txt",  sep=" ")
# Links = Links.drop_duplicates(subset=None, keep='first')

# Omim = pd.DataFrame()
f1 = f.splitlines()

chr = []
pos = []
info = []
link = []
trackIndex = []
len = []
Likelihood = []

for line in f1:
    sline = line.split("\t")

    if ('OMIM' in sline[7]):
        chr.append(sline[0])
        pos.append(sline[1])
        info.append('CV Disease: '+sline[7].split('CLNDN=')[1].split(';')[0]+'<br />'+
                    'CV Status: '+sline[7].split('ClinVarStatus=')[1].split(';')[0]+'<br />'+
                    'CV Likelihood:'+ sline[10] + '<br />')
        len.append(0)
        trackIndex.append(2)
        link.append(sline[7].split(';CVLink=')[1])
        Likelihood.append(sline[10])

    elif ('GWASdiseaseHit' in sline [7]):
        chr.append(sline[0])
        pos.append(sline[1])
        info.append('GWAS DiseaseHit: '+sline[7].split(';GWASdiseaseHit=')[1].split(';')[0]+'<br />'+
                    'GWAS Likelihood: ' + sline[10] + '<br />')
        len.append(0)
        trackIndex.append(3)
        link.append(sline[7].split(';GwasLink=')[1])
        Likelihood.append(sline[10])

    elif('DidaGeneID' in sline [7]):
        chr.append(sline[0])
        pos.append(sline[1])
        info.append('DIDA DiseaseHit: '+sline[7].split('DidaDiseaseHit=')[1].split(';')[0]+'<br />'+
                    'Combination: '+sline[7].split('Combination=')[1].split(';')[0]+'<br />'+
                    'DIDA Likelihood: ' + sline[10]+'<br />')
        len.append(0)
        trackIndex.append(4)
        link.append(sline[7].split(';DidaLink=')[1])
        Likelihood.append(sline[10])

    elif ('PharmPhenotypesHit' in sline [7]):
        chr.append(sline[0])
        pos.append(sline[1])
        info.append('PharmGKB PhenotypesHit: '+sline[7].split('PharmPhenotypesHit=')[1].split(';')[0]+'<br />'+
                    'ChemicalsAffect: '+sline[7].split('ChemicalsAffect=')[1].split(';')[0].split(';')[0]+'<br />'+
                    'PhGKB Likelihood: ' + sline[10] + '<br />')
        len.append(0)
        trackIndex.append(1)
        link.append(sline[7].split(';PhGLink=')[1])
        Likelihood.append(sline[10])

    elif ('Predicted Pathogenic' in sline [7]):
        chr.append(sline[0])
        pos.append(sline[1])
        info.append('Predicted Pathogenic'+'<br />'+
                    'ScoreType: '+sline[7].split('ScoreType=')[1].split(';')[0]+'<br />'+
                    'Likelihood: ' + sline[10] +'<br />')
        len.append(0)
        trackIndex.append(0)
        link.append(sline[7].split(';McapLink=')[1].split(';')[0])
        Likelihood.append(sline[10])


AllData["chr"] = chr
AllData["pos"] = pos
AllData["info"] = info
AllData["len"] = len
AllData['trackIndex'] = trackIndex
AllData['Link'] = link
AllData['Likelihood'] = Likelihood

# AllData["OMIM"] = AllData["OMIM"].astype(str)
# Links["OMIM"] = Links["OMIM"].astype(str)
# FinalData = AllData.merge(Links, on="OMIM")
# del FinalData['OMIM']
# def convert(v):
#     try:
#         return int(v)
#     except ValueError:
#         return v

x = AllData.sort_values(['chr'],ascending=1)
# x = AllData.sort(['chr']).values
y = x.drop_duplicates(subset=None, keep='first')
# print(y)
y.to_csv("./VisFiles/ToJsonChild_"+str(fileName)+".txt" , index=False, sep=" ")
