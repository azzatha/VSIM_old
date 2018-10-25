# 1- Update all the DB and process them:
# -------------------------------------
#chmod +x updateDB.sh
#./updateDB.sh

# Take the input file as parameter:
echo "Mother File: $1"
echo "Father File: $2" 
child="$3"

if [ $# -eq 2 ]; then
    child=50
fi

echo "Number of simulated Children: " $child
moth=$(grep -w '#CHROM' $1 |  awk '{ print $10 }')
fath=$(grep -w '#CHROM' $2 |  awk '{ print $10 }')

bgzip $1
tabix -p vcf $1.gz
bgzip $2
tabix -p vcf $2.gz

#1- Merge the two file
/usr/bin/vcf-merge $1.gz $2.gz > ./Simulation/Parent_$1_$2.vcf

bgzip  ./Simulation/Parent_$1_$2.vcf
tabix -p vcf ./Simulation/Parent_$1_$2.vcf.gz

mkdir ./Simulation/CreatedChildren/$1_$2_children; 

#3- Creat Children
for c in $(seq 1 $child)
do
  /var/www/vsim.com/VSIM/Simulation/rtg-tools/rtg childsim --mother $moth --father $fath  -i ./Simulation/Parent_$1_$2.vcf.gz  -o ./Simulation/CreatedChildren/$1_$2_children/child$c.vcf.gz -t ./Simulation/1000g_v37_phase2.sdf -s child$c
done

#4- Apply the prevous work:
# ClivVar 
# Load New OMIM:
#groovy ./1-ClinVar/loadModeInh.groovy | grep "^OMIM" > ./1-ClinVar/omim_mode.txt

# Find the intersect with CV Database,and Run Python of the input file for CV
/var/www/vsim.com/bedtools2/bin/bedtools intersect -wa -wb -f 1.00 -r -a ./AllDataBases/CV_DB.vcf -b ./Simulation/CreatedChildren/$1_$2_children/*.vcf.gz  -filenames > ./1-ClinVar/CV_$1_$2
python ./1-ClinVar/CV_Children.py $1_$2 $child

# GWAS
/var/www/vsim.com/bedtools2/bin/bedtools intersect -wb -wa -f 0.50 -r -a ./AllDataBases/GWAS_DB.vcf -b ./Simulation/CreatedChildren/$1_$2_children/*.vcf.gz  -filenames  > ./2-Gwas/GW_$1_$2
python ./2-Gwas/Gwas_children.py $1_$2 $child

# PharmGKP
/var/www/vsim.com/bedtools2/bin/bedtools intersect -wb -wa  -a  ./AllDataBases/Pharm_DB.vcf -b ./Simulation/CreatedChildren/$1_$2_children/*.vcf.gz  -filenames > ./3-PharmGKP/PhG_$1_$2
python ./3-PharmGKP/Pharm_Children.py $1_$2 $child

# Dida
/var/www/vsim.com/bedtools2/bin/bedtools intersect -wa -wb  -a ./AllDataBases/DIDA_DB.vcf -b ./Simulation/CreatedChildren/$1_$2_children/*.vcf.gz  -filenames > ./4-Dida/Di_$1_$2
python ./4-Dida/Dida_Children.py $1_$2 $child


# 5- MCAP annotation
# Run Annovar to annotae the file with Mendelian Clinically Applicable Pathogenicity (M-CAP) Score
mkdir ./CombineChildResult/mcap_$1_$2; 

rm ./Simulation/CreatedChildren/$1_$2_children/*.vcf.gz.tbi
gunzip ./Simulation/CreatedChildren/$1_$2_children/*
for file in ./Simulation/CreatedChildren/$1_$2_children/* ; do
	x=$(basename $file)	
	#sed -i "" 's/Chr//g' ./Simulation/CreatedChildren/$1_$2_children/$x
 	perl ./annovar/table_annovar.pl ./Simulation/CreatedChildren/$1_$2_children/$x  ./annovar/humandb/ -buildver hg19 -out ./CombineChildResult/mcap_$1_$2/MCAP_$x 	 -remove -protocol mcap -operation f -nastring . -vcfinput
    rm ./CombineChildResult/mcap_$1_$2/MCAP_$x.avinput
	rm ./CombineChildResult/mcap_$1_$2/MCAP_$x.hg19_multianno.txt
	
	perl MCAP_filter.pl ./CombineChildResult/mcap_$1_$2/MCAP_$x.hg19_multianno.vcf 0.025 > ./CombineChildResult/mcap_$1_$2/filtered_$x
	rm  ./CombineChildResult/mcap_$1_$2/MCAP_$x.hg19_multianno.vcf
done

cat ./CombineChildResult/mcap_$1_$2/*.vcf > ./CombineChildResult/mcap_$1_$2/MCAP_AllChild.vcf

python ./CombineChildResult/MCAP_compine.py $1_$2 $child
rm -rfv ./CombineChildResult/mcap_$1_$2
rm -rfv ./Simulation/CreatedChildren/$1_$2_children
rm ./Simulation/Parent_$1_$2.*
rm ./CombineChildResult/temp.txt


# 6- Combine all created files:
python ./CombineChildResult/Combine_child.py $1_$2 

# 7- Vislization
# Prepare the file for Vis
python ./VisFiles/PrepareJsonChild.py $1_$2

# Creat Json File
python ./VisFiles/JsonChild.py $1_$2 > ./VisFiles/$1-$2.json

#echo "Done"
# visualize