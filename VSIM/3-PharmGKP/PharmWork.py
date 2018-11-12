import pandas as pd
import sys
import os

fileName1 = sys.argv[-1]
fileName = './3-PharmGKP/PhG_'+ fileName1

if (os.stat(fileName).st_size == 0):
    print('File is empty! There is no match with PharmGKP')
else:
    Data = pd.read_csv(fileName, header=None, sep="\t")
    phData = pd.DataFrame(
        columns=['#CHROM', 'POS', 'ID', 'REF', 'ALT', 'QUAL', 'FILTER', 'INFO', 'FORMAT', 'GT',
                 'Chemicals', 'PharmPhenotypesHit'])
    phData['#CHROM'] = Data[10]
    phData['POS'] = Data[11]
    phData['ID'] = Data[12]
    phData['REF'] = Data[13]
    phData['ALT'] = Data[14]
    phData['QUAL'] = Data[15]
    phData['FILTER'] = Data[16]
    phData['INFO'] = Data[17]
    phData['FORMAT'] = Data[18]
    phData['GT'] = Data[19]
    phData['Chemicals'] = Data[6]
    #phData['PhGLink'] = "https://www.ncbi.nlm.nih.gov/snp/?term="+Data[12]

    phData['PharmPhenotypesHit'] = Data[7]
    phData['PhGLink'] = "https://www.ncbi.nlm.nih.gov/search/?term=" + phData['PharmPhenotypesHit']

    # phData = phData.replace(' ', '_', regex=True)

    phData['INFO'] =  phData.INFO.astype(str).str.cat(phData.Chemicals.astype(str),sep=';ChemicalsAffect=')
    phData['INFO'] =  phData.INFO.astype(str).str.cat(phData.PharmPhenotypesHit.astype(str),sep=';PharmPhenotypesHit=')
    phData['INFO'] =  phData.INFO.astype(str).str.cat(phData.PhGLink.astype(str),sep=';PhGLink=')

    del phData['Chemicals']
    del phData['PharmPhenotypesHit']
    del phData['PhGLink']

    phData.to_csv("./CombineIndvResults/FinalPhG_"+str(fileName1), index = False, sep="\t")

