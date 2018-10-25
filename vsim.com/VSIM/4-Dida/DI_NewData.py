import pandas as pd
import sys
import os

fileName1 = sys.argv[-1]
fileName = './4-Dida/Di_'+ fileName1

if (os.stat(fileName).st_size == 0):
    print('File is empty! There is no match with Dida')
else:
    didaOrgData = pd.read_csv(fileName,header=None, delim_whitespace=1)

    didaData = pd.DataFrame(columns=['#CHROM', 'POS', 'ID','REF','ALT', 'QUAL', 'FILTER', 'INFO','FORMAT', 'GT',
                                     'DidaGeneID','DidaGeneName','Link'])

    didaData['#CHROM'] = didaOrgData[10]
    didaData['POS'] = didaOrgData[11]
    didaData['ID'] = didaOrgData[12]
    didaData['REF'] = didaOrgData[13]
    didaData['ALT'] = didaOrgData[14]
    didaData['QUAL'] = didaOrgData[15]
    didaData['FILTER'] = didaOrgData[16]
    didaData['INFO'] = didaOrgData[17]
    didaData['FORMAT'] = didaOrgData[18]
    didaData['GT'] = didaOrgData[19]
    didaData['DidaGeneID'] = didaOrgData[4]
    didaData['DidaGeneName'] = didaOrgData[5]

    y = didaData.DidaGeneID.value_counts()
    y.to_csv("./4-Dida/GeneIDCount.txt", sep="\t")

    y2 = pd.read_csv('./4-Dida/GeneIDCount.txt', sep="\t", header=None)
    y2.columns=['DidaGeneID','NumOfCombination']

    didaData = didaData.merge(y2, on='DidaGeneID')

    orginalGenesCount = pd.read_csv('./4-Dida/OriginalCount.txt', delim_whitespace=1, header=None)
    orginalGenesCount.columns=['DidaGeneID','geneA','geneB','geneC','count']

    FindComb = didaData .merge(orginalGenesCount, on='DidaGeneID')
    del FindComb['geneA'],FindComb['geneB'],FindComb['geneC']
    Comb = []

    for i in range(len(FindComb)):
         if (FindComb['count'][i] == FindComb['NumOfCombination'][i]):
             Comb.append('AllGenes')
         else:
             Comb.append('OneGene')

    FindComb['Combination'] = Comb
    del FindComb['count']

    DidaData = pd.read_csv('./AllDataBases/DIDA_Digenic_comb.csv', sep="\t")
    DidaData = DidaData.rename(columns = {'ID':'DidaGeneID'})
    DidaData['Link'] = "http://dida.ibsquare.be/detail/?dc="+DidaData['DidaGeneID']

    FileWithAllinfo = FindComb.merge(DidaData, on='DidaGeneID')
    del FileWithAllinfo['Allele 1 Gene A cDNA change']
    del FileWithAllinfo['Allele 2 Gene A cDNA change']
    del FileWithAllinfo['Allele 1 Gene A protein change']
    del FileWithAllinfo['Allele 2 Gene A protein change']
    del FileWithAllinfo['Allele 1 Gene B cDNA change']
    del FileWithAllinfo['Allele 2 Gene B cDNA change']
    del FileWithAllinfo['Allele 2 Gene B protein change']
    del FileWithAllinfo['Gene relationship']
    del FileWithAllinfo['Allele 1 Gene B protein change']
    del FileWithAllinfo['Unnamed: 14']
    del FileWithAllinfo['Gene A']
    del FileWithAllinfo['Gene B']
    del FileWithAllinfo['Oligogenic effect']
    del FileWithAllinfo['Link_x']

    FileWithAllinfo = FileWithAllinfo.rename(columns = {'Disease name (ORPHANET)':'DidaDiseaseHit'})
    FileWithAllinfo = FileWithAllinfo.rename(columns = {'Link_y':'Link'})

    FileWithAllinfo['INFO'] = FileWithAllinfo.INFO.astype(str).str.cat(FileWithAllinfo.DidaGeneID.astype(str),sep=';DidaGeneID=')
    FileWithAllinfo['INFO'] = FileWithAllinfo.INFO.astype(str).str.cat(FileWithAllinfo.DidaGeneName.astype(str),sep=';DidaGeneName=')
    FileWithAllinfo['INFO'] = FileWithAllinfo.INFO.astype(str).str.cat(FileWithAllinfo.NumOfCombination.astype(str),sep=';NumOfCombination=')
    FileWithAllinfo['INFO'] = FileWithAllinfo.INFO.astype(str).str.cat(FileWithAllinfo.DidaDiseaseHit.astype(str),sep=';DidaDiseaseHit=')
    FileWithAllinfo['INFO'] = FileWithAllinfo.INFO.astype(str).str.cat(FileWithAllinfo.Combination.astype(str),sep=';Combination=')
    FileWithAllinfo['INFO'] = FileWithAllinfo.INFO.astype(str).str.cat(FileWithAllinfo.Link.astype(str),sep=';DidaLink=')

    # FileWithAllinfo = FileWithAllinfo.replace(' ', '_', regex=True)

    del FileWithAllinfo['DidaGeneID']
    del FileWithAllinfo['DidaDiseaseHit']
    del FileWithAllinfo['Combination']
    del FileWithAllinfo['Link']
    del FileWithAllinfo['DidaGeneName']
    del FileWithAllinfo['NumOfCombination']

    FileWithAllinfo.to_csv("./CombineIndvResults/FinalDi_"+str(fileName1), index = False, sep="\t")