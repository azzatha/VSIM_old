import pandas as pd
import sys
import os

fileName1 = sys.argv[1]
NumChild = sys.argv[2]
fileName = "./2-Gwas/GW_"+fileName1

if (os.stat(fileName).st_size == 0):
    print('File is empty! There is no match with GWAS')

else:
    GwasOrgData = pd.read_csv("./2-Gwas/GW_"+fileName1, header=None, delim_whitespace = 1)
    GwasData = pd.DataFrame(columns=['IndvName','#CHROM','POS','ID','REF','ALT','QUAL','FILTER','INFO',
                                     'FORMAT','GT','GWASdiseaseHit','Link'])

    GwasData['IndvName'] = GwasOrgData[11].str.split('/').str.get(4)
    GwasData['#CHROM'] = GwasOrgData[12]
    GwasData['POS'] = GwasOrgData[13]
    GwasData['ID'] = GwasOrgData[14]
    GwasData['REF'] = GwasOrgData[15]
    GwasData['ALT'] = GwasOrgData[16]
    GwasData['QUAL'] = GwasOrgData[17]
    GwasData['FILTER'] = GwasOrgData[18]
    GwasData['INFO'] = GwasOrgData[19]
    GwasData['FORMAT'] = GwasOrgData[20]
    GwasData['GT'] = GwasOrgData[23]
    GwasData['GWASdiseaseHit'] = GwasOrgData[3].replace('_', ' ', regex=True)
    GwasData['Link'] = "https://www.ncbi.nlm.nih.gov/search/?term=" + GwasData['GWASdiseaseHit']

    GwasData = pd.concat(g for _, g in GwasData.groupby("IndvName") if len(g) > 0)
    IndvNumCount = GwasData.IndvName.value_counts()

    report2 = GwasData.groupby(["GWASdiseaseHit",'IndvName']).size()
    report2.to_csv("./2-Gwas/gwasTimp/" + str(fileName1) + ".txt", sep="\t")

    finalRep = pd.read_csv("./2-Gwas/gwasTimp/" + str(fileName1) + ".txt", header=None, sep="\t")
    finalRep = finalRep.groupby([0])[1].count() / int(NumChild)
    #print(report2)
    finalRep.to_csv("./2-Gwas/gwasTimp/" + str(fileName1) + ".txt" , sep="\t")

    takeVarInfo = GwasData.drop_duplicates(subset='GWASdiseaseHit', keep="first")

    finalRep = pd.read_csv("./2-Gwas/gwasTimp/" + str(fileName1) + ".txt" , sep="\t",names=['GWASdiseaseHit','gwasLikelihood'])
    finalRep['gwasLikelihood'] = (finalRep['gwasLikelihood']*100).round(2)

    New = takeVarInfo.merge(finalRep, on='GWASdiseaseHit')

    New['INFO'] = New.INFO.astype(str).str.cat(New.GWASdiseaseHit.astype(str), sep=';GWASdiseaseHit=')
    New['INFO'] = New.INFO.astype(str).str.cat(New.gwasLikelihood.astype(str), sep=';gwasLikelihood=')
    New['INFO'] =  New.INFO.astype(str).str.cat(New.Link.astype(str),sep=';GwasLink=')
    New['Likelihood']  = New['gwasLikelihood']

    del New['GWASdiseaseHit']
    del New['gwasLikelihood']
    del New['IndvName']
    del New['Link']
    # print(New)
    New.to_csv("./CombineChildResult/FinalGW_" + str(fileName1), index=False, sep="\t")

