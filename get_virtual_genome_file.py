import sys

file1=open(sys.argv[1],'r') # vir_genome
file2=open(sys.argv[2],'r') # all_positon.sort
file3=open(sys.argv[3],'r') # all_pep
#file4 out file name

gene_length_dict={}
for line in file2:
    line_list=line.strip().split('\t')
    gene_length_dict[line_list[0]]=int(line_list[-2])-int(line_list[-3])
pep_dict={}
for line in file3:
    if line.startswith('>'):
        gene_id=line.strip()[1:]
        pep_dict[gene_id]=''
    else:
        pep_dict[gene_id]+=line
out_file1=open(sys.argv[4]+'pos_vir','w')
out_file2=open(sys.argv[4]+'pep_vir','w')
start=1
for line in file1:
    line_list=line.strip().split('\t')
    out_file1.write(line_list[0]+'\tChr1\t'+str(start)+'\t'+str(start+gene_length_dict[line_list[0]])+'\t+\n')
    out_file2.write('>'+line_list[0]+'\n'+pep_dict[line_list[0]])
    start=start+gene_length_dict[line_list[0]]+1





