import pandas as pd
import sys
import os

fileName1 = sys.argv[1]
NumChild = sys.argv[2]
fileName = "./1-ClinVar/CV_"+fileName1

if (os.stat(fileName).st_size == 0 or ('OMIM:' not in open(fileName).read())):
    print('File is empty! There is no match with ClinVar')

else:
    #Reports = open("/home/althagat/PycharmProjects/FinalReports/1-ClinVar/CVFinalReportSim/AllParentsStatistics.txt",'w')
    omimMode = pd.read_csv('./1-ClinVar/omim_mode.txt', header=None, delim_whitespace=1)
    omimMode.columns = ['OMIM', 'Status']
    omimMode['OmimID'] = omimMode['OMIM'].str[5:]

    data = pd.read_csv("./1-ClinVar/CV_"+fileName1, header=None, delim_whitespace=1)
    data['FileName'] = data[8].str.split('/').str.get(4)
    if (data[7].str.contains('OMIM:').any()):
        data['OmimID'] = data[7].str.split('OMIM:').str.get(1).str[0:6]
    data['CLNDN'] = data[7].str.split(';CLNDN=').str.get(1).str.split(';').str.get(0)
    newDF = pd.DataFrame(columns=['#CHROM','POS', 'ID','REF','ALT','QUAL','FILTER','INFO',
                                  'FORMAT','GT','modeOfInheritance','Status','OmimID','GTNum'])
    newDF = pd.DataFrame(
    columns=['IndvName', '#CHROM', 'POS', 'ID', 'REF', 'ALT', 'QUAL', 'FILTER', 'INFO', 'FORMAT', 'GT', 'GTNum',
    'OmimID', 'modeOfInheritance', 'Status','CLNDN'])

    newDF['IndvName'] = data['FileName']  # newDF.append(data, ignore_index = True) # ignoring index is optional
    newDF['#CHROM'] = data[9]
    newDF['POS'] = data[10]
    newDF['ID'] = data[11]
    newDF['REF'] = data[12]
    newDF['ALT'] = data[13]
    newDF['QUAL'] = data[14]
    newDF['FILTER'] = data[15]
    newDF['INFO'] = data[16]
    newDF['FORMAT'] = data[17]
    newDF['GT'] = data[20]

    newDF['GTNum'] = data[20]
    newDF['OmimID'] = data['OmimID']
    newDF['CLNDN'] = data['CLNDN']
    moOfInh = newDF.merge(omimMode, on='OmimID')
    moOfInh['modeOfInheritance'] = moOfInh['Status_y']

    del moOfInh['Status_y']
    del moOfInh['OMIM']

    moOfInh = moOfInh.rename(columns = {'Status_x':'ClinVarStatus'})

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
    omim = pd.DataFrame(columns=['OMIM', 'Link'])
    omim['OMIM'] = moOfInh['OmimID']
    omim['Link'] = "https://www.omim.org/entry/" + omim['OMIM']
    moOfInh['Link'] = omim['Link']
    # omim.to_csv("./1-ClinVar/Link_" + str(fileName1)+".txt", index=False, sep=" ")

    y = pd.concat(g for _, g in moOfInh.groupby("IndvName") if len(g) > 0)
    countHaveDes = (y['ClinVarStatus'] == 'Have the Disease').sum()
    countHCarries = (y['ClinVarStatus'] == 'Carrier_of_Disease').sum()

    report2 = y.groupby(["ClinVarStatus", "OmimID", 'IndvName']).size()
    report2.to_csv("./1-ClinVar/CVTimp/"+ str(fileName1)+".txt", sep="\t")
    finalRep = pd.read_csv("./1-ClinVar/CVTimp/"+ str(fileName1)+".txt", header=None, sep="\t")
    finalRep = finalRep.groupby([0, 1])[2].count() / int(NumChild)
    finalRep.columns=['CV_Class','OmimID','CVLikelihood']
    finalRep.to_csv("./1-ClinVar/CVTimp/"+ str(fileName1)+".txt", sep="\t")

    finalRep2 = pd.read_csv('./1-ClinVar/CVTimp/'+ str(fileName1)+".txt", sep="\t",names=['CV_Class','OmimID','CVLikelihood'])
    finalRep2['CVLikelihood'] = (finalRep2['CVLikelihood']*100).round(2)


    takeVarInfo = y.drop_duplicates(subset='OmimID', keep="first")
    del takeVarInfo['IndvName']
    del takeVarInfo['modeOfInheritance']
    del takeVarInfo['GTNum']
    del takeVarInfo['ClinVarStatus']

    finalRep2['OmimID'] = finalRep2['OmimID'].astype(str)

    New = finalRep2.merge(takeVarInfo, on='OmimID')
    New['INFO'] = New.INFO.astype(str).str.cat(New.OmimID.astype(str), sep=';OMIM=')
    New['INFO'] = New.INFO.astype(str).str.cat(New.CLNDN.astype(str), sep=';CLNDN=')
    New['INFO'] = New.INFO.astype(str).str.cat(New.CV_Class.astype(str),sep=';ClinVarStatus=')
    New['INFO'] = New.INFO.astype(str).str.cat(New.CVLikelihood.astype(str),sep=';CVLikelihood=')
    New['INFO'] = New.INFO.astype(str).str.cat(New.Link.astype(str),sep=';CVLink=')

    New['Likelihood']  = New['CVLikelihood']

    del New['CV_Class']
    del New['CVLikelihood']
    del New['OmimID']
    del New['CLNDN']
    del New['Link']
    New.to_csv("./CombineChildResult/FinalCV_" + str(fileName1), index=False, sep="\t")