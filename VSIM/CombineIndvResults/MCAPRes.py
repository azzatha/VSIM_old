import pandas as pd
import sys
import os

fileName1 = sys.argv[-1]
fileName = './CombineIndvResults/FilterMCAP_'+ fileName1

if (os.stat(fileName).st_size == 0):
    print('File is empty! There is no match with MCAP filter')
else:
    mcap = pd.read_csv(fileName, delim_whitespace=1)
    mcap['McapLink'] = "http://exac.broadinstitute.org/variant/" +mcap['#CHROM'].apply(str)+"-"+mcap['POS'].apply(str)+"-"+mcap['REF']+"-"+mcap['ALT']

    mcap['INFO'] ='Predicted Pathogenic'
    mcap['INFO'] =  mcap.INFO.astype(str).str.cat(mcap.McapLink.astype(str),sep=';McapLink=')

    del mcap['McapLink']

    mcap.to_csv("./CombineIndvResults/FinalMCAP_"+str(fileName1), index = False, sep="\t")
