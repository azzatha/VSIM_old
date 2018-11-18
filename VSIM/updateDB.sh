#!/bin/bash
#!/usr/bin/python2.7

#dir1=$(pwd)
#dir2=$(/var/www/vsim.com/VSIM)

#cd $dir2

# 1- Update all the DB and process them:
# -------------------------------------
# 1- ClinVar
CV_file_name=$(curl ftp://ftp.ncbi.nlm.nih.gov/pub/clinvar/vcf_GRCh37/ | grep -o 'clinvar_[0-9]*\.vcf\.gz$' | sort -u)
wget  -O ./AllDataBases/CLV.vcf.gz  ftp://ftp.ncbi.nlm.nih.gov/pub/clinvar/vcf_GRCh37/$CV_file_name
zless ./AllDataBases/CLV.vcf.gz | grep 'CLNSIG=Pathogenic\|CLNSIG=Likely_pathogenic' > ./AllDataBases/CV_DB1.vcf
#sed '1i ##fileformat=VCFv4.1 ' ./AllDataBases/CV_DB1.vcf > ./AllDataBases/CV_DB.vcf

sed '1i\
##fileformat=VCFv4.1
' ./AllDataBases/CV_DB1.vcf >  ./AllDataBases/CV_DB.vcf

#sed  '1 i\ 
#fileformat=VCFv4.1\n' ./AllDataBases/CV_DB1.vcf > ./AllDataBases/CV_DB.vcf
 
#sed 's/regexp/\\\n/g' ./AllDataBases/CV_DB1.vcf > ./AllDataBases/CV_DB.vcf
#sed '1s/^/##fileformat=VCFv4.1/&\n/g' ./AllDataBases/CV_DB1.vcf > ./AllDataBases/CV_DB.vcf
#ex -sc '1i|##fileformat=VCFv4.1' -cx ./AllDataBases/CV_DB.vcf

## Add Chr for the simulation
#sed 's/^/Chr/' ./AllDataBases/CV_DB.vcf | sed 's/^.*\(##.*\)/\1/g' | sed 's/^.*\(#CH.*\)/\1/g' > ./AllDataBases/CV_DB_Chr.vcf
#rm ./AllDataBases/CLV.vcf.gz

# 2- GWAS
wget -O ./AllDataBases/GW.tsv http://www.ebi.ac.uk/gwas/api/search/downloads/full 
cut -f12,13,8,11,14,15,22,25,27,28,36 ./AllDataBases/GW.tsv | sed -e '1s/CHR_ID/#CHROM/' -e '1s/CHR_POS/POS/' -e '1s/SNPS/ID/'  > ./AllDataBases/GWA2.tsv
paste <(cut -f3 ./AllDataBases/GWA2.tsv) <(cut -f4 ./AllDataBases/GWA2.tsv)   <(cut -f7 ./AllDataBases/GWA2.tsv)  <(cut -f1,2,5,6,8,9,10,11 ./AllDataBases/GWA2.tsv) > ./AllDataBases/GWASData.vcf
cat ./AllDataBases/GWASData.vcf  | tr '\t' ',' > ./AllDataBases/TEST.vcf
sed -e "s/^,/0,/" -e "s/,,/,0,/g" -e "s/,$/,0/" ./AllDataBases/TEST.vcf | tr ',' '\t' > ./AllDataBases/TEST2.vcf
sed 's/ /_/g' ./AllDataBases/TEST2.vcf > ./AllDataBases/GWASData22.vcf
python ./AllDataBases/GwasSeprate.py

awk -F'\t' '$1!=""' ./AllDataBases/GWASDataSeprate.vcf | grep -v '_x_' > ./AllDataBases/GWAS_DB.vcf
#sed 's/^/Chr/' ./AllDataBases/GWAS_DB.vcf | sed 's/^.*\(##.*\)/\1/g' | sed 's/^.*\(#CH.*\)/\1/g' > ./AllDataBases/GWAS_DB_Chr.vcf
rm ./AllDataBases/GW.tsv
rm ./AllDataBases/GWA2.tsv 
rm ./AllDataBases/TEST.vcf
rm ./AllDataBases/TEST2.vcf
rm ./AllDataBases/GWASData.vcf
rm ./AllDataBases/GWASDataSeprate.vcf 
rm ./AllDataBases/GWASData22.vcf

# 4- DIDA
curl http://dida.ibsquare.be/browse/download/DIDA_Variants_75f75773803e45027c7ad57aa5fe6dd82c0d52e371dfe78fa17317e2833566dd.csv.zip  -o ./AllDataBases/DidaVar.csv.zip
unzip ./AllDataBases/DidaVar.csv.zip  -d ./AllDataBases/

curl http://dida.ibsquare.be/browse/download/DIDA_Digenic-Combinations_16ddf22644411874a6371d3aa056d1c69159b9eab87f2553e5c9e166657adf3c.csv.zip -o ./AllDataBases/DidaComb.csv.zip
unzip ./AllDataBases/DidaComb.csv.zip -d ./AllDataBases/

mv ./AllDataBases/DIDA_Variants_* ./AllDataBases/DIDA_Variants.csv

python ./AllDataBases/DidaPreProcess.py
ex -sc '1i|##fileformat=VCFv4.1' -cx ./AllDataBases/DIDA_DB.vcf
#sed 's/^/Chr/' ./AllDataBases/DIDA_DB.vcf | sed 's/^.*\(##.*\)/\1/g'| sed 's/^.*\(#CH.*\)/\1/g'  >  ./AllDataBases/DIDA_DB_Chr.vcf

mv ./AllDataBases/DIDA_Digenic-Combinations_* ./AllDataBases/DIDA_Digenic_comb.csv
rm ./AllDataBases/DIDA_Variants.csv
rm ./AllDataBases/DidaVar.csv.zip
rm ./AllDataBases/DidaComb.csv.zip
rm ./AllDataBases/DIDA_Variants_Update.vcf
