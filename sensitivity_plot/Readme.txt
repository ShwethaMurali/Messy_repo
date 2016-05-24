This script was written to check the sensitivity of structural variant (SV) 
callers, specifically for deletions. The script expects atleast one truth set 
and atleast one test set of variants. Every file in the test set is compared
 against every file in the truth set. The inputs are in form of VCF files 
(version 4.0 and 4.1, untested) and bedfiles.

** Overview **

In case of structural variants, the exact breakpoints are hard to predict 
i.e: for the same event, multiple callers will give multiple different breakpoint 
coordinates. Therefore evaluation of these callers is not straightforward. 

For this method, all calls in the test set are compared to the truth set and the 
percentage of truth recovered (true positive rate) is plotted. 

BEDtools is used to intersect the truth set intervals with the test set in a 
reciprocal fashion i.e: If percentage reciprocal intersect is set to 50%,
 any call in the test set is a true positive if the intersection with any truth
 set call is >= 50% of both the participating calls. 

Sensitivity is calculated for every bin where each bin corresponds to a range of deletion
sizes (1-200,201-400,401-500...). Default bin size is 500 and default min-size and max-size
for the calls are set at 1bp and 3kb respectively. 

*** Usage ***

Before you begin:
1. Make sure bedtools is present in your environment (see dependencies for more information).
2. Python modules for matplotlib,numpy,tempfile are required 
3. If you have a vcf file and the script errors out, use bedfiles containing the coordinates 
 of the calls instead.
4. Every file in the test set is compared against every file in the truth

Usage:
del_sensitivity.py -tru <truth_set1.vcf truth_set2.vcf ..> -tes <test_set1.vcf test_set2.vcf ..>

Required options are -tru and -tes 
For a list of all options, 

> del_sensitivity.py -h  
will give you:
usage: del_sensitivity.py [-h] -tru TRU [TRU ...] -tes TES [TES ...]
                          [--size-min SIZE_MIN] [--size-max SIZE_MAX]
                          [--size-bin SIZE_BIN] [--pct-ovl PCT_OVL]
optional arguments:
  -h, --help           show this help message and exit
  -tru TRU [TRU ...]   The truth set vcf (or vcfs as a space spearated list)
                       all test vcfs are compared against these
  -tes TES [TES ...]   The test set vcf (or vcfs as a space spearated list)
                       Each one of these vcfs is compared against the truth
  --size-min SIZE_MIN  Floor size of the calls in bp to be considered; default
                       = 1
  --size-max SIZE_MAX  Ceiling size of the calls in bp to be considered ;
                       default = 3000
  --size-bin SIZE_BIN  size of the bins for plotting; default = 500
  --pct-ovl PCT_OVL    minimun percentage reciprocal overlap to keep; default
                       = 0.5

Example: 
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

****
