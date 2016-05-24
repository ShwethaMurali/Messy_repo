In this example, there is one truth file and four test files provided. 

(Note: All test file VCFs obtained from 1000 genomes pilot data set SV data 
(samples CEU, YRI and JPT/CHB) ftp link:  ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/release/20110521/
pvcfs *.deletions.genotypes.vcf.gz were downloaded and split into single sample
vcfs using the script pvcf_to_vcf_1000g.py)

For every truth file, the script draws a new plot.
In this case, since we only mentioned one, output is a single plot
(Sensitivity_summary_truth_set.vcf.png)

To plot sensitivity with bin size 200 and minimum reciprocal overlap set to
30%: 

>python del_sensitivity.py -tru truth_set.vcf -tes NA11918_.vcf NA11894_.vcf
NA06994_.vcf NA11992_.vcf --size-bin 200 --pct-ovl 0.3 

Extracting bed coordinates from  NA11992_.vcf

Extracting bed coordinates from  NA06994_.vcf

Extracting bed coordinates from  NA11894_.vcf

Extracting bed coordinates from  NA11918_.vcf

Extracting bed coordinates from  truth_set.vcf

Intersecting calls from truth_set.vcf,NA11992_.vcf

Intersecting calls from truth_set.vcf,NA06994_.vcf

Intersecting calls from truth_set.vcf,NA11894_.vcf

Intersecting calls from truth_set.vcf,NA11918_.vcf

Plotting

Done!
