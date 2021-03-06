# SplitStrains

In this repo, we introduce the tool *SplitStrains* used for
detecting and separating mixed strains of M. tuberculosis.  
Grounded in a rigorous statistical framework, it is based on formulating, for a given set of WGS reads, two alternative hypotheses, namely: the reads belong to a single strain (null hypothesis) or to a mixture of two or more strains (alternative hypothesis). We then use MLE (Maximum Likelihood Estimates) for the parameters of both hypotheses, and compare their likelihoods to draw a conclusion. As a result, we obtain:
    1. A determination on whether the sample represents a simple or mixed infection  
    2. A likelihood ratio for this determination (between the null and the alternative hypothesis)  
    3. If mixed, the proportion of each constituent strain and its identity defined by its SNPs (single-nucleotide polymorphisms) relative to a reference genome.  

### Requirements:
Python 3.6.9  
Python libraries listed in *requirements.txt*. This can be used for automatic pip install.  
Optional: conda 4.5.12  
Additional software:
1. bwa 0.7.17 (read aligner)
2. Trimmomatic-0.36 (read quality trimmer)
3. samtools 1.9 (bam/sam files utility)
4. art_illumina 2.5.8 (read generator)  

### Recommendation:
Use the tool with the bash shell.  

### Usage:
Run *python splitStrains.py -h* to view help.  
The *gsc.sh* is a master shell script that generates 50 mixed synthetic samples with different proportions, alignes them and runs *splitStrain.py*.  


##### Example:  
First run:  
SplitStrains outputs results into stdout.  

```
python splitStrains.py -r ref_file -b gff_file -g 2 -s 100 -e 4000000 -o output_dir -fd min_depth indexed_sorted.bam > result.txt
```
Second run:  
After the first run, it is possible to reuse (`--reuse`) cached data (*freqVec.csv*) for faster analysis and parameter tunning
```
python splitStrains.py --reuse -fe 0.7 -r ref_file -b gff_file -g 2 -s 100 -e 4000000 -o output_dir -fd min_depth indexed_sorted.bam > result.txt
```
The directory *output_dir* contains *freqVec.csv* and plots for visual inspection.
### Notes:    
Before running *splitStrains.py*, make sure that <b>sorted and indexed BAM's</b>  aligned sequences and <b>indexed </b> fasta reference have the same sequence ID. In other words, bam files must be used with the same reference which was used for alignment.
For example, if BAM aligned sequences refer to "*gi|41353971|emb|AL123456.2|* " then the fasta reference file should start with "*>gi|41353971|emb|AL123456.2|* ".

### Tips:
After the first run of *splitStrains.py* it is possible to reuse the results for faster analysis, set *--reuse*.  
Alternatively, set *reuse=1* in *gsc.sh*.  
Always check produced plots for visual inspection and parameter tunning.  

### Alignment guide:
*bwa mem* doesn't do a good job when aligning M. tb. This results in a short genome regions with high rate of false SNPs or ubnormally high number of variants. This can be observed in scatter plots generated by *splitStrains.py*.  
The best alignement results can be achieved using *bwa aln*. This workflow is implemented in *runSplitStrains.sh* which is called from the master script *gsc.sh*.

.

### TODO:
1) Need to run a check on the gff file (version).  
2) Internalize included gff file.  
3) Compute filtering depth based of the provided float value from 0.1 to 1.  (important)  
4) Separate *splitStrains.py* code into files.  
5) Introduce the option of working with single-end reads  

### Possible bad behavior:
When depth coverage is high (300 and greater) it is possibe that likelyhood_ratio_test function can overflow.  
Couldn't reproduce the error so far.  
