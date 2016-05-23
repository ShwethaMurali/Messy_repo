In this example, there is one truth file and four test files provided. 
(VCFs obtained from 1000 genomes project SV data
 ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/release/20110521/)

Usage:
>python del_sensitivity.py -tru truth_set.vcf -tes NA11918_.vcf NA11894_.vcf
NA06994_.vcf NA11992_.vcf --size-bin 200 --pct-ovl 0.3 

Bin size is set to 200 and percent reciprocal overlap is set to 30% 

Output: 
For every truth file, the script draws a new plot. 
In this case, since we only mentioned one, output is a single plot
(Sensitivity_summary_truth_set.vcf.png)

comaparing truth_set.vcf NA11992_.vcf
comaparing truth_set.vcf NA06994_.vcf
comaparing truth_set.vcf NA11894_.vcf
comaparing truth_set.vcf NA11918_.vcf

Done!
