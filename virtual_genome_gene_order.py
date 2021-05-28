# -*- coding=utf-8 -*-
# 2021.0528
# @zlk 
# zhanglk960127@163.com


import sys
import pick_virtual_genome

# file1 position.sort
# file2 synteny file
out_file=open(sys.argv[3],'w')

synteny_dict=pick_virtual_genome.get_synteny_dict(sys.argv[2])

gene_list=pick_virtual_genome.get_pos_dict(sys.argv[1])
index=0
for i in gene_list:
    if i in synteny_dict.keys():
        index+=1
        out_file.write(i+'\t'+synteny_dict[i][0]+'\t'+str(synteny_dict[i][1])+'\t'+str(index)+'\n')


