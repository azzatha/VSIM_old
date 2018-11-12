import shutil
import re
import csv

with  open("./AllDataBases/GWASData22.vcf", "r" ) as file : #GWASData2.vcf
    data = file.read()

result = open("./AllDataBases/GWASDataSeprate.vcf", "w")
result.write('##fileformat=VCFv4.1\n#CHROM\tPOS\tID\tDISEASE/TRAIT\tREGION\tREPORTED\tGENE(S)\tMAPPED_GENE\tCONTEXT\tRISK_ALLELE_FREQUENCY\tP-VALUE\tMAPPED_TRAIT_URI\n')

file2 = data.split('\n')
file2.pop(0)
for line in file2:
    #print (line)
    sline = line.split('\t')
    if (sline[0] != '0'):
        if (len (sline)==11) and (len(sline[0].split(";")) <=1 ) and (len(sline[1].split(";")) <=1 ) and (len(sline[2].split(";")) <=1 ) and (len(sline[6].split(";")) <=1 ) and (len(sline[7].split(";")) <=1 ):
            result.write(line)
            result.write('\n')
        elif (len (sline)==11) and (len(sline[0].split(";")) >1 ) and (len(sline[1].split(";")) >1 ) and (len(sline[2].split(";")) >1 ) and (len(sline[6].split(";")) >1 ) and (len(sline[7].split(";")) >1 ):
            for x in range(len(sline[0].split(";"))):
                result.write (sline[0].split(";")[x]+'\t' + sline[1].split(";")[x]+'\t'
                              +sline[2].split(";")[x]+'\t'+sline[3]+'\t'+sline[4]+'\t'+sline[5]+
                              '\t'+sline[6].split(";")[x]+'\t'+sline[7].split(";")[x]+'\t'+sline[8]+'\t'+sline[9]+'\t'+sline[10])
                result.write('\n')
