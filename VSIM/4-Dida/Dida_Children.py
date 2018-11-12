import pandas as pd
import sys
import os

fileName1 = sys.argv[1]
NumChild = sys.argv[2]
fileName = "./4-Dida/Di_"+fileName1

if (os.stat(fileName).st_size == 0):
    print('File is empty! There is no match with Dida')

else:
    didaOrgData = pd.read_csv(fileName, header=None, delim_whitespace=1)
    didaData = pd.DataFrame(columns=['ChildNames','#CHROM', 'POS', 'ID', 'REF', 'ALT', 'QUAL', 'FILTER', 'INFO', 'FORMAT', 'GT',
                                     'DidaGeneID', 'DidaGeneName', 'Link'])

    didaData['ChildNames'] = didaOrgData[10].str.split('/').str.get(4)
    didaData['#CHROM'] = didaOrgData[11]
    didaData['POS'] = didaOrgData[12]
    didaData['ID'] = didaOrgData[13]
    didaData['REF'] = didaOrgData[14]
    didaData['ALT'] = didaOrgData[15]
    didaData['QUAL'] = didaOrgData[16]
    didaData['FILTER'] = didaOrgData[17]
    didaData['INFO'] = didaOrgData[18]
    didaData['FORMAT'] = didaOrgData[19]
    didaData['GT'] = didaOrgData[22]
    didaData['DidaGeneID'] = didaOrgData[4]
    didaData['DidaGeneName'] = didaOrgData[5]

    didaData = pd.concat(g for _, g in didaData.groupby("ChildNames") if len(g) > 0)

    GidIndv =  didaData.groupby('DidaGeneID')['ChildNames'].value_counts()
    # print(GidIndv)
    GidIndv.to_csv("./4-Dida/didaTimp/childGeneIDCount.txt", sep="\t")

    GidIndv2 = pd.read_csv('./4-Dida/didaTimp/childGeneIDCount.txt', sep="\t", header=None)
    GidIndv2.columns = ['DidaGeneID','ChildNames', 'NumOfCombination']

    finalRep = GidIndv2.groupby(['DidaGeneID','NumOfCombination'])['ChildNames'].count() / int(NumChild)
    # print(GidIndv2)
    finalRep.to_csv("./4-Dida/didaTimp/" + str(fileName1) + ".txt" , sep="\t")
    finalRep = pd.read_csv("./4-Dida/didaTimp/" + str(fileName1) + ".txt", sep="\t",
                           names=['DidaGeneID','NumOfCombination', 'DidaLikelihood'])
    finalRep['DidaLikelihood'] = (finalRep['DidaLikelihood'] * 100).round(2)
    # print(finalRep)

    didaData = didaData.merge(finalRep, on=['DidaGeneID'])

    didaData = didaData.drop_duplicates(subset=['ChildNames','DidaGeneID'], keep="first")

    # print (didaData)
    orginalGenesCount = pd.read_csv('./4-Dida/OriginalCount.txt', delim_whitespace=1, header=None)
    orginalGenesCount.columns=['DidaGeneID','geneA','geneB','geneC','count']
    # print (orginalGenesCount)

    FindComb = didaData .merge(orginalGenesCount, on='DidaGeneID')
    del FindComb['geneA'], FindComb['geneB'], FindComb['geneC']
    Comb = []

    for i in range(len(FindComb)):
        if (FindComb['count'][i] == FindComb['NumOfCombination'][i]):
            Comb.append('AllGenes')
        else:
            Comb.append('OneGene')

    FindComb['Combination'] = Comb
    del FindComb['count']

    DidaData = pd.read_csv('./AllDataBases/DIDA_Digenic_comb.csv', sep="\t")
    DidaData = DidaData.rename(columns={'ID': 'DidaGeneID'})
    DidaData['Link'] = "http://dida.ibsquare.be/detail/?dc=" + DidaData['DidaGeneID']

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
    FileWithAllinfo['INFO'] = FileWithAllinfo.INFO.astype(str).str.cat(FileWithAllinfo.Combination.astype(str),sep=';Combination=')
    FileWithAllinfo['INFO'] = FileWithAllinfo.INFO.astype(str).str.cat(FileWithAllinfo.DidaDiseaseHit.astype(str),sep=';DidaDiseaseHit=')
    FileWithAllinfo['INFO'] = FileWithAllinfo.INFO.astype(str).str.cat(FileWithAllinfo.DidaLikelihood.astype(str),sep=';DidaLikelihood=')
    FileWithAllinfo['INFO'] = FileWithAllinfo.INFO.astype(str).str.cat(FileWithAllinfo.Link.astype(str),sep=';DidaLink=')

    FileWithAllinfo['Likelihood']  = FileWithAllinfo['DidaLikelihood']

    del FileWithAllinfo['DidaGeneID']
    del FileWithAllinfo['DidaDiseaseHit']
    del FileWithAllinfo['Combination']
    del FileWithAllinfo['Link']
    del FileWithAllinfo['DidaGeneName']
    del FileWithAllinfo['NumOfCombination']
    del FileWithAllinfo['DidaLikelihood']
    del FileWithAllinfo['ChildNames']

    # print (FileWithAllinfo)
    FileWithAllinfo.to_csv("./CombineChildResult/FinalDi_" + str(fileName1), index=False, sep="\t")
