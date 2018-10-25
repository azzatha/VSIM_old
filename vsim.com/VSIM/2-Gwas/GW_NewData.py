import pandas as pd
import sys
import os
import re

fileName1 = sys.argv[-1]
fileName = './2-Gwas/gwas_Data_'+ fileName1

if (os.stat(fileName).st_size == 0):
    print('File is empty! There is no match with Gwas')
else:
    Reports = open("./2-Gwas/Report.txt",'w')

    GwasOrgData = pd.read_csv(fileName, header=None, delim_whitespace=1)
    GwasData = pd.DataFrame(
               columns=['#CHROM', 'POS', 'ID', 'REF', 'ALT', 'QUAL', 'FILTER', 'INFO', 'FORMAT', 'GT','GWASdiseaseHit','Link'])

    GwasData['#CHROM'] = GwasOrgData[11]
    GwasData['POS'] = GwasOrgData[12]
    GwasData['ID'] = GwasOrgData[13]
    GwasData['REF'] = GwasOrgData[14]
    GwasData['ALT'] = GwasOrgData[15]
    GwasData['QUAL'] = GwasOrgData[16]
    GwasData['FILTER'] = GwasOrgData[17]
    GwasData['INFO'] = GwasOrgData[18]
    GwasData['FORMAT'] = GwasOrgData[19]
    GwasData['GT'] = GwasOrgData[20]
    GwasData['GWASdiseaseHit'] = GwasOrgData[3].replace('_', ' ', regex=True)
    GwasData['Link']= "https://www.ncbi.nlm.nih.gov/search/?term="+GwasData['GWASdiseaseHit']

    GwasData['INFO'] =  GwasData.INFO.astype(str).str.cat(GwasData.GWASdiseaseHit.astype(str),sep=';GWASdiseaseHit=')
    GwasData['INFO'] =  GwasData.INFO.astype(str).str.cat(GwasData.Link.astype(str),sep=';GwasLink=')

    del GwasData['GWASdiseaseHit']
    del GwasData['Link']

    GwasData.to_csv("./CombineIndvResults/FinalGW_"+str(fileName1), index = False, sep="\t")

