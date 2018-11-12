import pandas as pd
import sys

fileName = sys.argv[-1]

f = open("./VisFiles/Final_"+str(fileName),'r').read()
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

for line in f1:
    sline = line.split()
    if ('OMIMn' in sline[7]):
        chr.append(sline[0])
        pos.append(sline[1])
        info.append('CV Disease: '+sline[7].split('CLNDN=')[1].split(';')[0]+'<br />'+
                    'CV Status: '+sline[7].split('CVStatus=')[1].split(';')[0]+'<br />')
        len.append(0)
        trackIndex.append(2)
        link.append(sline[7].split(';CVLink=')[1])

    elif ('GWASdiseaseHit' in sline [7]):
        chr.append(sline[0])
        pos.append(sline[1])
        info.append('GWAS diseaseHit: '+sline[7].split('GWASdiseaseHit=')[1].split(';')[0]+'<br />') # +","+ sline[7].split(';')[4])
        len.append(0)
        trackIndex.append(3)
        link.append(sline[7].split(';GwasLink=')[1])

    elif('DidaDiseaseHit' in sline [7]):
        chr.append(sline[0])
        pos.append(sline[1])
        info.append('Dida DiseaseHit: '+sline[7].split('DidaDiseaseHit=')[1].split(';')[0]+'<br />'+
                    'Combination: '+sline[7].split('Combination=')[1].split(';')[0]+'<br />')
        len.append(0)
        trackIndex.append(4)
        link.append(sline[7].split(';DidaLink=')[1])

    elif ('PharmPhenotypesHit' in sline [7]):
        chr.append(sline[0])
        pos.append(sline[1])
        info.append('PharmGKB PhenotypesHit: '+sline[7].split('PharmPhenotypesHit=')[1].split(';')[0]+'<br />'+
                    'Chemicals Affect: '+sline[7].split('ChemicalsAffect=')[1].split(';')[0].split(';')[0]+'<br />')
        len.append(0)
        trackIndex.append(1)
        link.append(sline[7].split(';PhGLink=')[1])

    elif ('Predicted' in sline [7]):
        chr.append(sline[0])
        pos.append(sline[1])
        info.append('Predicted Pathogenic'+'<br />')
        len.append(0)
        trackIndex.append(0)
        link.append(sline[7].split(';McapLink=')[1])


AllData["chr"] = chr
AllData["pos"] = pos
AllData["info"] = info
AllData["len"] = len
AllData['trackIndex'] = trackIndex
AllData['Link'] = link

x = AllData.sort_values(['chr'],ascending=1)
y = x.drop_duplicates(subset=None, keep='first')#need revew
y.to_csv("./VisFiles/ToJson_"+str(fileName)+".txt" , index=False, sep=" ")
