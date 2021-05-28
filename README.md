# virtual-genome
The virtual genome containing more ancestor genes is constructed to solve the disadvantage of synteny analysis of a single reference genome.

#To identify syntenic gene pairs within the genome
#genome.position.sort: Each line of the file is a Gene ID, arranged in the order in which it appears in its genome
#self_blast_out: Result file of BlastP (-outfmt 6).

python intra_genome_synteny.py genome.position.sort self_blast_out out_file_name



