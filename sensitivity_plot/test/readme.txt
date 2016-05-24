In this example, there is one truth file and four test files provided.
You can find these in the tarball 'sample_vcfs.tgz' 

For every truth file, the script draws a new plot.
In this case, since there is one truth file, output is a single plot.
(Sensitivity_summary_truth_set.vcf.png)

::Note: All test file VCFs obtained from 1000 genomes pilot data set SV data 
(samples CEU, YRI and JPT/CHB)
ftp link: ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/pilot_data/paper_data_sets/a_map_of_human_variation/low_coverage/sv/
Multi-sample VCFs *.deletions.genotypes.vcf.gz were downloaded and split into single sample
vcfs using the script pvcf_to_vcf_1000g.py

Usage: 

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
--------
To plot sensitivity with default settings: 

>python del_sensitivity.py -tru truth_set.vcf -tes NA11918_.vcf NA11894_.vcf
NA06994_.vcf NA11992_.vcf 

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
--------
To get a list of all options: 

> python del_sensitivity.py -h 
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

***
