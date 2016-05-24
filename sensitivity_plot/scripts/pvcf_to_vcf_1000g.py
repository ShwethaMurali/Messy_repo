#!/usr/bin/python

"""
A quick and dirty script to extract vcfs from the pVCF
"""
import sys
import re 

vcffile=sys.argv[1]
samplelist = []
fin = open(vcffile,'r')
for line in fin.readlines():	
	if line.startswith("#CHROM"):
		samplelist = line.strip().split("\t")[9:]
		break
fin.close()

expEnd = re.compile("^END=")
expLen = re.compile("^SVLEN=")
expSvty = re.compile("^SVTYPE")

for sample in samplelist:
	svpfile = sample+"_.vcf" 
	i = samplelist.index(sample) + 9
	fin,fout = open(vcffile,'r'),open(svpfile,'a+')
	fout.truncate()

	for line in fin.readlines():
		if line.startswith("#CHROM"):
			wrstr = ""
			for lin in line.split("\t")[0:9]:
				wrstr = wrstr+lin+"\t"	
			fout.write(wrstr.strip()+"\t"+sample+"\n")	
			continue	

		elif line.startswith("#"):
			fout.write(line)
			continue
	
		##CHROM  POS     ID      REF     ALT     QUAL    FILTER  INFO    FORMAT  SAMPLE
		fields = line.strip().split("\t")
		GTstr = fields[i].strip()
		GT = fields[i].split(":")[0]
		if(GT=="." or GT=="0/0" or GT=="./."):
			continue
		writestr = ""
		for m in fields[0:9]:
			writestr = writestr+m.strip()+"\t"
		fout.write("%s\t%s\n" % (writestr.strip(),GTstr))
	fout.close()
	fin.close()				
