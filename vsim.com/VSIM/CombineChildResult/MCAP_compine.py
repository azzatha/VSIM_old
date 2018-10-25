import pandas as pd
import sys
import os

path = sys.argv[1]
childNum = sys.argv[2]

if (os.path.isdir('./CombineChildResult/mcap_'+path)):

    fileName = './CombineChildResult/mcap_'+path+'/MCAP_AllChild.vcf'
    if (os.stat(fileName).st_size == 0):
        print('File is empty! There is no match with MCAP filter')

    else:
        data = pd.read_csv(fileName, header=None, delim_whitespace=1,
                           names=['#CHROM', 'POS', 'ID', 'REF', 'ALT', 'QUAL', 'FILTER', 'INFO', 'FORMAT', 'GT1', 'GT2','GT'])
        del data['GT1']
        del data['GT2']
        data['INFO'] = data['INFO'].str.split('MCAP=').str.get(1).str.split(';').str.get(0)

        # data['Count']  = data.groupby("INFO",'GT').unique()
        # data['Count']= data.groupby(['INFO', 'GT']).size().reset_index().groupby('GT')[[0]].max()
        t = pd.DataFrame(data.groupby(['#CHROM', 'POS', 'ID', 'REF', 'ALT', 'QUAL', 'FILTER', 'INFO', 'FORMAT','GT']).size())
        t.to_csv("./CombineChildResult/temp.txt", sep='\t')

        mcap = pd.read_csv("./CombineChildResult/temp.txt", sep='\t')
        mcap.rename(columns={"INFO": "INFO", "GT": "GT", "0" : "Count"}, inplace=True)
        mcap['ScoreType'] = 'none'

        for index, row in mcap.iterrows():
            if  mcap['GT'][index] == '0|0':
                mcap.at[index,'ScoreType'] =  'Homozygote Ref'

            elif mcap['GT'][index] == '1|0' :
                mcap.at[index, 'ScoreType'] = 'Heterozygote'

            elif mcap['GT'] == '1|1':
                mcap.at[index, 'ScoreType'] = 'Homozygote Alt'

            mcap['Likelihood'] = ((mcap['Count'] / int(childNum)) * 100).round(2)


        mcap['McapLink'] = "http://exac.broadinstitute.org/variant/" +mcap['#CHROM'].apply(str)+"-"+mcap['POS'].apply(str)+"-"+mcap['REF']+"-"+mcap['ALT']
        mcap['INFO'] = 'Predicted Pathogenic'

        mcap['INFO'] =  mcap.INFO.astype(str).str.cat(mcap.McapLink.astype(str),sep=';McapLink=')
        mcap['INFO'] =  mcap.INFO.astype(str).str.cat(mcap.ScoreType.astype(str),sep=';ScoreType=')

        del mcap['McapLink']
        del mcap['ScoreType']
        del mcap['Count']

        # print(mcap)
        mcap.to_csv("./CombineChildResult/FinalMCAP_"+path, index=False, sep="\t")

        # mcap['McapLink'] = "https://www.ncbi.nlm.nih.gov/search/?term="+mcap['ID']
        # mcap['INFO'] ='Predicted Pathogenic'
        # mcap['INFO'] =  mcap.INFO.astype(str).str.cat(mcap.McapLink.astype(str),sep=';McapLink=')
        # del mcap['McapLink']
        # mcap.to_csv('./CombineChildResult/mcap_'+fileName1+'/Child_FinalMCAP_'+str(fileName2), index = False, sep="\t")
else:
    print("No folder exist!")
    exit(0)