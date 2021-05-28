# -*- coding=utf-8 -*-
# 2021.0528
# @zlk 
# zhanglk960127@163.com

# file1 virtual_file
# file2 tomato_positon.sort_file
# file3 new_tomato_synteny
import sys


def get_pos_dict(pos_file):
    gene_list=[]
    loop_file=open(pos_file,'r')
    for line in loop_file:
        line_list=line.strip().split('\t')
        gene_list.append(line_list[0])
    return gene_list
        


def get_synteny_dict(synteny_file):
    synteny_dict={}
    loop_file=open(synteny_file,'r')
    for line in loop_file:
        line_list=line.strip().split('\t')
        if line_list[4] in synteny_dict.keys():
            if int(line_list[9].split('|')[0])>int(line_list[10].split('|')[0]):
                big_num=int(line_list[9].split('|')[0])
            else:
                big_num=int(line_list[10].split('|')[0])
            if big_num>synteny_dict[line_list[4]][1]:
                synteny_dict[line_list[4]]=[line_list[0],big_num]
            else:
                continue
        else:
            if int(line_list[9].split('|')[0])>int(line_list[10].split('|')[0]):
                big_num=int(line_list[9].split('|')[0])
            else:
                big_num=int(line_list[10].split('|')[0])
            synteny_dict[line_list[4]]=[line_list[0],big_num]
    return synteny_dict

def get_vir_dict(vir_file):
    virtual_dict={}
    loop_file=open(vir_file,'r')
    for line in loop_file:
        line_list=line.strip().split('\t')
        virtual_dict[line_list[1]]=line_list
    return virtual_dict
def get_rignt_positon(pos_gene,pos_list,vir_dict):
    pos_index=pos_list.index(pos_gene)

    for i in reversed(pos_list[:pos_index]):
        if i in vir_dict.keys():
            add_index=vir_dict[i][-1]
            break
    for i in pos_list[pos_index:]:
        if i in vir_dict.keys():
            add_index=vir_dict[i][-1]
            break
    return add_index        





if __name__ == "__main__":
    gene_list=get_pos_dict(sys.argv[2])
    syn_dict=get_synteny_dict(sys.argv[3])
    vir_dict=get_vir_dict(sys.argv[1])
    out_file=open(sys.argv[4],'w')
    out_list=[]


    for key,value in syn_dict.items():
        if value[0] in vir_dict.keys():
            
            this_list=vir_dict[value[0]]
            if int(this_list[-2])>int(syn_dict[key][-1]):
                out_list.append(this_list)
            elif abs(int(this_list[-2])-int(syn_dict[key][-1]))<=2:
                out_list.append(this_list)
            else:
                add_index=get_rignt_positon(value[0],gene_list,vir_dict)
                this_list[0]=key
                this_list[-2]=syn_dict[key][-1]
                this_list[-1]=add_index
                out_list.append(this_list)
            del vir_dict[value[0]]
        else:
            add_index=get_rignt_positon(value[0],gene_list,vir_dict)
            out_list.append([key,value[0],value[1],add_index])
    for key in vir_dict.keys():
        out_list.append(vir_dict[key])        
    for i_list in sorted(out_list,key=lambda x: int(x[-1])):
        for i in i_list:
            out_file.write(str(i)+'\t')
        out_file.write('\n')
        


