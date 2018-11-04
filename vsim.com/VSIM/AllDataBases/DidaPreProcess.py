import pandas as pd
import re
import numpy as np

with open("./AllDataBases/DidaAllelsInfo.txt") as file1:
    fp1 = file1.read()

with open("./AllDataBases/DIDA_Variants.csv") as file2:
    fp2 = file2.read()

result = open("./AllDataBases/DIDA_Variants_Update.vcf", 'w')

f1 = fp1.splitlines()
for line in f1:
    sline = line.split()
    f2=fp2.splitlines()
    f2.pop(0)
    for line2 in f2:
        line2 = line2.replace('\"', '')
        sline2 = line2.split("\t")
        if (sline[1] == sline2[6]):
            result.write(line+"\t"+line2)
            result.write("\n")
        if (sline[2] == sline2[6]):
            result.write(line+"\t"+line2)
            result.write("\n")
        if (sline[3] == sline2[6]):
            result.write(line+"\t"+line2)
            result.write("\n")

result.close()

didaData = pd.read_csv('./AllDataBases/DIDA_Variants_Update.vcf' , header=None, sep = "\t")
didaData.columns = ['GeneID', 'a','b', 'c','DidaID','POS','#CHROM','REF','ALT','GeneName','cDNAChange','ProteinChange','VariantEffect','f']
del didaData['a']
del didaData['b']
del didaData['c']
del didaData['f']
didaData = didaData[['#CHROM', 'POS', 'REF', 'ALT', 'GeneID','GeneName','cDNAChange','ProteinChange','VariantEffect','DidaID']]
didaData.to_csv("./AllDataBases/DIDA_DB.vcf", index = False, sep="\t")