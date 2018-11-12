import pandas as pd
import sys
import os

fileName1 = sys.argv[1]
NumChild = sys.argv[2]
fileName = "./3-PharmGKP/PhG_"+fileName1

if (os.stat(fileName).st_size == 0):
    print('File is empty! There is no match with PharmGKP')

else:
    Data = pd.read_csv("./3-PharmGKP/PhG_"+fileName1, header=None, sep="\t")
    phData = pd.DataFrame(
        columns=['IndvName','#CHROM', 'POS', 'ID', 'REF', 'ALT', 'QUAL', 'FILTER', 'INFO', 'FORMAT', 'GT',
                 'Chemicals', 'PharmPhenotypesHit'])
    
    phData['IndvName'] = Data[10].str.split('/').str.get(4)
    # print(phData)
    phData['#CHROM'] = Data[11]
    phData['POS'] = Data[12]
    phData['ID'] = Data[13]
    phData['REF'] = Data[14]
    phData['ALT'] = Data[15]
    phData['QUAL'] = Data[16]
    phData['FILTER'] = Data[17]
    phData['INFO'] = Data[18]
    phData['FORMAT'] = Data[19]
    phData['GT'] = Data[22]
    phData['Chemicals'] = Data[6]
    phData['PharmPhenotypesHit'] = Data[7]
    phData['PhGLink'] = "https://www.ncbi.nlm.nih.gov/snp/?term="+Data[13]


    phData = pd.concat(g for _, g in phData.groupby("IndvName") if len(g) > 0)

    IndvNumCount = phData.IndvName.value_counts()

    report2 = phData.groupby(["PharmPhenotypesHit",'IndvName']).size()
    report2.to_csv("./3-PharmGKP/temp/" + str(fileName1) + ".txt", sep="\t")
    finalRep = pd.read_csv("./3-PharmGKP/temp/" + str(fileName1) + ".txt", header=None, sep="\t")
    finalRep = finalRep.groupby([0])[1].count() / int(NumChild)

    finalRep.to_csv("./3-PharmGKP/temp/" + str(fileName1) + ".txt" , sep="\t")

    takeVarInfo = phData.drop_duplicates(subset='PharmPhenotypesHit', keep="first")

    finalRep = pd.read_csv("./3-PharmGKP/temp/" + str(fileName1) + ".txt" , sep="\t",names=['PharmPhenotypesHit','PhGKPLikelihood'])
    finalRep['PhGKPLikelihood'] = (finalRep['PhGKPLikelihood']*100).round(2)

    New = takeVarInfo.merge(finalRep, on='PharmPhenotypesHit')

    New['INFO'] = New.INFO.astype(str).str.cat(New.PharmPhenotypesHit.astype(str), sep=';PharmPhenotypesHit=')
    New['INFO'] = New.INFO.astype(str).str.cat(New.PhGKPLikelihood.astype(str), sep=';PhGKPLikelihood=')
    New['INFO'] =  New.INFO.astype(str).str.cat(New.Chemicals.astype(str),sep=';ChemicalsAffect=')
    New['INFO'] =  New.INFO.astype(str).str.cat(New.PhGLink.astype(str),sep=';PhGLink=')

    New['Likelihood']  = New['PhGKPLikelihood']

    del New['IndvName']
    del New['PharmPhenotypesHit']
    del New['PhGKPLikelihood']
    del New['Chemicals']
    del New['PhGLink']


    print(New)

    New.to_csv("./CombineChildResult/FinalPhG_" + str(fileName1), index=False, sep="\t")

