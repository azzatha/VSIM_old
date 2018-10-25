import pandas as pd
import sys
from pathlib import Path

fileName = sys.argv[1]

cvf = Path("./CombineChildResult/FinalCV_"+str(fileName))
gwf = Path("./CombineChildResult/FinalGW_"+str(fileName))
phf = Path("./CombineChildResult/FinalPhG_" + str(fileName))
dif = Path("./CombineChildResult/FinalDi_"+str(fileName))
mcapf = Path("./CombineChildResult/FinalMCAP_"+str(fileName))

print (cvf)
print (gwf)
print (phf)
print (dif)

if cvf.is_file():
    cv = pd.read_csv("./CombineChildResult/FinalCV_"+str(fileName),sep="\t")
else:
    cv = pd.DataFrame(columns=['#CHROM','POS','ID','REF','ALT','QUAL','FILTER','INFO','FORMAT','GT','Likelihood'])

if gwf.is_file():
    gwas = pd.read_csv("./CombineChildResult/FinalGW_"+str(fileName),sep="\t")
else:
    gwas = pd.DataFrame(columns=['#CHROM','POS','ID','REF','ALT','QUAL','FILTER','INFO','FORMAT','GT','Likelihood'])

if phf.is_file():
    pharm = pd.read_csv("./CombineChildResult/FinalPhG_" + str(fileName), sep="\t")
else:
    pharm = pd.DataFrame(columns=['#CHROM','POS','ID','REF','ALT','QUAL','FILTER','INFO','FORMAT','GT','Likelihood'])

if dif.is_file():
    dida = pd.read_csv("./CombineChildResult/FinalDi_" + str(fileName), sep="\t")
else:
    dida = pd.DataFrame(columns=['#CHROM','POS','ID','REF','ALT','QUAL','FILTER','INFO','FORMAT','GT','Likelihood'])
    
if mcapf.is_file():
    mcap = pd.read_csv("./CombineChildResult/FinalMCAP_" + str(fileName), sep="\t")
else:
    mcap = pd.DataFrame(columns=['#CHROM','POS','ID','REF','ALT','QUAL','FILTER','INFO','FORMAT','GT','Likelihood'])

#mcap = pd.read_csv("./CombineChildResult/FinalMCAP_"+str(fileName), sep="\t")
#mcap['#CHROM'].astype(str)
#dida['#CHROM']= dida['#CHROM'].astype(str)
#pharm['#CHROM']= pharm['#CHROM'].astype(str)
#gwas['#CHROM']= gwas['#CHROM'].astype(str)
#cv['#CHROM']= cv['#CHROM'].astype(str)

Combine = pd.merge =  pd.concat([cv,gwas,pharm,dida,mcap], axis=0)

Combine = Combine.sort_values('#CHROM')
Combine = Combine.drop_duplicates(subset=None, keep='first', inplace=False)

# Combine = Combine.replace(' ', '_', regex=True)
Combine.to_csv("./VisFiles/FinalChild_"+str(fileName), index = False, sep="\t")
