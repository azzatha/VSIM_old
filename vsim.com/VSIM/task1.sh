#!/bin/bash
# Indv Work: This code will generate the final files for vis:

# 1- Update all the DB and process them:
# -------------------------------------
#./updateDB.sh  

# Take the input file as parameter:
echo "start $1"

# 1- CV Work
# Load New OMIM:
#groovy ./1-ClinVar/loadModeInh.groovy | grep "^OMIM" > ./1-ClinVar/omim_mode.txt

# Find the intersect with CV Database,and Run Python of the input file for CV
/var/www/vsim.com/bedtools2/bin/bedtools intersect -wb -f 1.00 -r -a ./AllDataBases/CV_DB.vcf -b $1 > ./1-ClinVar/clinvar_Data.vcf
cut -f9,10,11,12,13,14,15,16,17,18 ./1-ClinVar/clinvar_Data.vcf > ./1-ClinVar/clinvar_Data2.vcf
egrep -v "^#" ./AllDataBases/CV_DB.vcf > ./AllDataBases/CV_Pathogenic_.vcf
cat ./AllDataBases/headerCV.txt ./AllDataBases/CV_Pathogenic_.vcf >  ./AllDataBases/CV_DB_Anno.vcf
cat ./1-ClinVar/headerInfo.txt ./1-ClinVar/clinvar_Data2.vcf > ./1-ClinVar/clinvar_Data_Annotate.vcf

#Annotate the resulting file:
bgzip ./AllDataBases/CV_DB_Anno.vcf
tabix -p vcf ./AllDataBases/CV_DB_Anno.vcf.gz
/usr/bin/vcfanno_linux64 -permissive-overlap ./AllDataBases/conf_ClinVar.toml  ./1-ClinVar/clinvar_Data_Annotate.vcf > ./1-ClinVar/Annotat_$1
egrep -v "^#" ./1-ClinVar/Annotat_$1 > ./1-ClinVar/Annotat_$1_noHeader.vcf
python ./1-ClinVar/CV_NewData.py $1

rm ./1-ClinVar/clinvar_Data.vcf 
rm ./1-ClinVar/clinvar_Data2.vcf
rm ./1-ClinVar/Annotat_$1
rm ./1-ClinVar/Annotat_$1_noHeader.vcf
rm ./AllDataBases/CV_Pathogenic_.vcf
rm ./AllDataBases/CV_DB_Anno.vcf.gz
rm ./AllDataBases/CV_DB_Anno.vcf.gz.tbi

# 2- GWAS Work
# Find the intersect with GWAS  Database, and Run Python of the input file for GW
/var/www/vsim.com/bedtools2/bin/bedtools intersect -wb -wa -f 1.0 -r -a ./AllDataBases/GWAS_DB.vcf  -b $1 > ./2-Gwas/gwas_Data_$1
python ./2-Gwas/GW_NewData.py $1 

# 3- PharmGKP Work
# Find the intersect with PharmGKP  Database, and Run Python of the input file for PG
/var/www/vsim.com/bedtools2/bin/bedtools intersect -wb -wa -f 1.0 -r -a ./AllDataBases/Pharm_DB.vcf -b  $1 > ./3-PharmGKP/PhG_$1
python ./3-PharmGKP/PharmWork.py $1

# 4- Dida Work
# Find the intersect with Dida  Database, and Run Python of the input file for Di
/var/www/vsim.com/bedtools2/bin/bedtools intersect -wa -wb -f 1.00 -r -a ./AllDataBases/DIDA_DB.vcf -b  $1 > ./4-Dida/Di_$1
python ./4-Dida/DI_NewData.py $1

# 5- MCAP annotation
# Run Annovar to annotae the file with Mendelian Clinically Applicable Pathogenicity (M-CAP) Score
perl ./annovar/table_annovar.pl  $1 ./annovar/humandb/ -buildver hg19 -out MCAP_$1 -remove -protocol mcap -operation f -nastring . -vcfinput

rm MCAP_$1.avinput
rm MCAP_$1.hg19_multianno.txt

# Take all the predicted Pathognic, the Recommended Pathogenicity threshold M-CAP > 0.025
perl MCAP_filter.pl MCAP_$1.hg19_multianno.vcf 0.025 > ./CombineIndvResults/MCAP_$1
rm  MCAP_$1.hg19_multianno.vcf

# Add the header info
cat ./CombineIndvResults/header.txt ./CombineIndvResults/MCAP_$1 > ./CombineIndvResults/FilterMCAP_$1
python ./CombineIndvResults/MCAPRes.py $1

rm ./CombineIndvResults/MCAP_$1
rm ./CombineIndvResults/FilterMCAP_$1

# 6- Combine all created files:
python ./CombineIndvResults/CombineAllInfo.py $1

# 7- Prepare the file for Vis
python ./VisFiles/PrepareJForJson.py $1

# 8- Creat Json File
python ./VisFiles/JsonIndv.py $1 > ./VisFiles/$1.json

#Vislization
#open ./ideogram/examples/vanilla/annotations-tracks.html/annotations-tracks.html
