import pandas as pd
import sys
import os

fileName1 = sys.argv[-1]
fileName = "./1-ClinVar/Annotat_"+fileName1+"_noHeader.vcf"

if (os.stat(fileName).st_size == 0 or ('OMIM:' not in open(fileName).read())):
    print('File is empty! There is no match with ClinVar')

else:
    Reports = open('./1-ClinVar/Report.txt','w')
    omimMode = pd.read_csv('./1-ClinVar/omim_mode.txt', header=None, delim_whitespace=1)
    omimMode.columns = ['OMIM' , 'Status']
    omimMode['OmimID'] = omimMode['OMIM'].str[5:]

    data = pd.read_csv(fileName, header=None, delim_whitespace=1)
    data.columns = ['#CHROM','POS', 'ID','REF','ALT','QUAL','FILTER','INFO', 'FORMAT','GT']
    data['OmimID'] = data['INFO'].str.split('OMIM:').str.get(1).str[:6]

    newDF = pd.DataFrame(columns=['#CHROM','POS', 'ID','REF','ALT','QUAL','FILTER','INFO', 'FORMAT','GT','modeOfInheritance', 'Status','OmimID','GTNum'])
    newDF = data
    newDF['GTNum'] = data['GT'].str[0:3]
    newDF['OmimID'] = data['OmimID']

    moOfInh = newDF.merge(omimMode, on='OmimID')
    moOfInh['modeOfInheritance'] = moOfInh['Status']
    moOfInh['OMIM'] = moOfInh['OMIM']
    moOfInh = moOfInh.rename(columns = {'Status':'ClinVarStatus'})

    for j in range(len(moOfInh)):
        if (moOfInh['modeOfInheritance'][j] == 'Recessive') and (
            (moOfInh['GTNum'][j] == '1|1') or (moOfInh['GTNum'][j] == '0|1') or  (moOfInh['GTNum'][j] == '1|0')):
            moOfInh['ClinVarStatus'].at[j] = 'Carrier_of_Disease'

        elif (moOfInh['modeOfInheritance'][j] == 'Dominant') and (
            (moOfInh['GTNum'][j] == '1|1')):
            moOfInh['ClinVarStatus'].at[j] = 'Have_the_Disease'

        elif (moOfInh['modeOfInheritance'][j] == 'Dominant') and (
            (moOfInh['GTNum'][j] == '1|0') or (moOfInh['GTNum'][j] == '0|1')):
            moOfInh['ClinVarStatus'].at[j] = 'Carrier_of_Disease'

        else:
            moOfInh['ClinVarStatus'].at[j] = 'None'

    moOfInh = moOfInh[moOfInh.ClinVarStatus != 'None']
    omim =  pd.DataFrame( columns=['OMIM','Link'])
    omim ['OMIM'] = moOfInh['OMIM'].str.split(':').str.get(1).str[:6]
    omim['Link'] = "https://www.omim.org/entry/"+omim['OMIM']
    moOfInh['Link'] = omim['Link']
    # omim.to_csv("./1-ClinVar/Link_"+str(fileName1)+".txt", index=False, sep=" ")

    # del moOfInh['OMIM']

    # countHaveDes = (moOfInh['ClinVarStatus'] == 'Have_the_Disease').sum()
    # countHCarries = (moOfInh['ClinVarStatus'] == 'Carrier_of_Disease').sum()
    # Reports.write("Total number of different variation = " + str(len(moOfInh)) + "\n")
    # Reports.write("Number of varients that Have the Disease = " + str(countHaveDes) + "\n")
    # Reports.write("Varients that Have the Disease (%) = " + str((countHaveDes / len(moOfInh)) * 100) + "\n")
    # Reports.write("Number of varients that Carrier of the Disease = " + str(countHCarries) + "\n")
    # Reports.write("Varients that Carrier of the Disease (%) = " + str(((countHCarries / len(moOfInh)) * 100)) + "\n")
    # Reports.write("------------------------------------------------------------------" + "\n")

    moOfInh['INFO'] =  moOfInh.INFO.astype(str).str.cat(moOfInh.OmimID.astype(str),sep=';OMIMn=')
    moOfInh['INFO'] =  moOfInh.INFO.astype(str).str.cat(moOfInh.modeOfInheritance.astype(str),sep=';modeOfInheritance=')
    moOfInh['INFO'] =  moOfInh.INFO.astype(str).str.cat(moOfInh.ClinVarStatus.astype(str),sep=';CVStatus=')
    moOfInh['INFO'] =  moOfInh.INFO.astype(str).str.cat(moOfInh.Link.astype(str),sep=';CVLink=')

    del moOfInh['OmimID']
    del moOfInh['GTNum']
    del moOfInh['modeOfInheritance']
    del moOfInh['ClinVarStatus']
    del moOfInh['Link']
    del moOfInh['OMIM']


    #print(moOfInh)
    moOfInh = moOfInh.replace(' ', '_', regex=True)
    moOfInh.to_csv("./CombineIndvResults/FinalCV_"+str(fileName1), index = False, sep="\t")