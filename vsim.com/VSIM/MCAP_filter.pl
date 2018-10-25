use strict;

my ($line, @arr, $mcap, $maf);

if ($ARGV[0] eq "") {print "provide path to the input file - vcf format"; exit;}
if ($ARGV[1] eq "") {print "enter MAF value to filter"; exit;}
else {$maf=$ARGV[1];}

open IN, $ARGV[0] or die "cannot open the input file";

#12      55499792        .       T       C       12203.5 PASS    AC=2;AF=1;AN=2;BaseQRankSum=-1.159;ClippingRankSum=0;DP=36;ExcessHet=0.0167;FS=0.582;InbreedingCoeff=0.3441;MLEAC=49;MLEAF=0.408;MQ=60;MQRankSum=0;QD=18.83;ReadPosRankSum=0.224;SOR=0.73;ANNOVAR_DATE=2017-07-17;Func.knownGene=intergenic;Gene.knownGene=NEUROD4\x3bOR9K2;GeneDetail.knownGene=dist\x3d75991\x3bdist\x3d23761;ExonicFunc.knownGene=.;AAChange.knownGene=.;1000g2015aug_all=0.304912;ExAC_ALL=.;ExAC_AFR=.;ExAC_AMR=.;ExAC_EAS=.;ExAC_FIN=.;ExAC_NFE=.;ExAC_OTH=.;ExAC_SAS=.;gnomAD_genome_ALL=0.3213;gnomAD_genome_AFR=0.3991;gnomAD_genome_AMR=0.2237;gnomAD_genome_ASJ=0.3675;gnomAD_genome_EAS=0.1230;gnomAD_genome_FIN=0.2985;gnomAD_genome_NFE=0.3095;gnomAD_genome_OTH=0.2878;ALLELE_END        GT:AD:DP:GQ:PL  1/1:1,35:36:77:1005,77,0
#1000g2015aug_all=0.48143;ExAC_ALL=.; gnomAD_genome_ALL=0.3213;

while ($line=<IN>)
{ 	chop $line;
	@arr=split('\t', $line);

	if ($arr[7] =~/MCAP=(.*?);/) {$mcap=$1;}

	if ($mcap>$maf)
	{	
		print $line."\n";}
	}
	
close IN;
