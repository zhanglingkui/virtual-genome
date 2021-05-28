# virtual-genome
The virtual genome containing more ancestor genes is constructed to solve the disadvantage of synteny analysis of a single reference genome.

## To identify syntenic gene pairs within the genome.  
### #genome.position.sort: Each line of the file is a Gene ID, arranged in the order in which it appears in its genome.  
#### #self_blast_out: Result file of BlastP (-outfmt 6).  
```
python3 intra_genome_synteny.py genome.position.sort self_blast_out out_file_name
```

## Bulit virtual-genome
### Select a reference genome to be used as the order of the virtual genome.  
#re1_genome.position.sort: Each line of the file is a Gene ID, arranged in the order in which it appears in reference genome.  
#target_ref1.syn: The result file of SynOrths software, syntenic file of target genome and reference genome, the first column is the target genome gene ID, and the fifth column is the reference genome gene ID.  
#virtual_genome1.txt : name of output file.    
```
python3 virtual_genome_gene_order.py re1_genome.position.sort target_ref1.syn virtual_genome1.txt
```
### Add reference genomes to the virtual genome.
#target.genome.position.sort: Each line of the file is a Gene ID, arranged in the order in which it appears in target genome.   
#target_re2.syn: The result file of Synorths software, syntenic file of target genome and reference genome, the first column is the target genome gene ID, and the fifth column is the reference genome gene ID.   
#virtual_genome2.txt : name of output file.  

```
python3 bulit_virtual_genome.py virtual_genome1.txt target.genome.position.sort target_re2.syn virtual_genome2.txt
python3 bulit_virtual_genome.py virtual_genome2.txt target.genome.position.sort target_ref3.syn virtual_genome3.txt
```

........




