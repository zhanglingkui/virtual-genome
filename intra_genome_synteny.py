# -*- coding=utf-8 -*-
# 2020.0804
# @zlk
# 鉴定自己和自己共线性基因对
#python self_self_syn.py ./lajiao/Capsicum_annuum.ASM51225v2.47.gff3.repr.position.sort ./fan_v_lazi/Capsicum_annuum.ASM51225v2.47.gff3.repr.pep_2_Capsicum_annuum.ASM51225v2.47.gff3.repr.pep.out lajiao_self_paralog
import sys

file1=open(sys.argv[1],'r')## 按照顺序排列的gene 列表 第一列为gene名，position.sort文件就可以

file2=open(sys.argv[2],'r')# self_blast_file
file3=open(sys.argv[3],'w')
file4=open(sys.argv[3]+'_tandem','w')
flanking_num=4
total_genome=[]
for line in file1:
    line_list=line.strip().split('\t')
    total_genome.append(line_list[0])
file1.close()
best_hit_dict={}
homo_dict={}
tandem_dict={}
for line in file2:
    line_list=line.strip().split('\t')
    if line_list[1]==line_list[0]: 
        continue
    if line_list[0] in homo_dict.keys():
        if len(homo_dict[line_list[0]])<30:
            homo_dict[line_list[0]].append(line_list[1])
        else:
            continue
    else:
        homo_dict[line_list[0]]=[line_list[1]]
    if line_list[0] not in best_hit_dict.keys():
        best_hit_dict[line_list[0]]=line_list[1]
    if abs(total_genome.index(line_list[0])-total_genome.index(line_list[1]))<=5:
        if line_list[0] in tandem_dict.keys():
            tandem_dict[line_list[0]].append(line_list[1])
        else:
            tandem_dict[line_list[0]]=[line_list[1]]

file2.close()
#检测tandem
tandem_list=[]
tandem_dict2=tandem_dict.copy()
for key,value in tandem_dict.items():
    if key not in tandem_dict2.keys():
        continue
    loop_value=value+[key]
    del tandem_dict2[key]
    for i in list(set(loop_value)):
        if i in tandem_dict2.keys():
            loop_value+=tandem_dict2[i]
            del tandem_dict2[i]
    if len(list(set(loop_value)))<2:
        continue
    else:
        tandem_list.append(list(set(loop_value)))
del_tandem=[]
for i_list in tandem_list:
    del_tandem+=sorted(i_list,key=lambda x:total_genome.index(x))[1:]
    for i in sorted(i_list,key=lambda x:total_genome.index(x)):
        file4.write(i+'\t')
    file4.write('\n')





index=1
out_dict={}
for key,value in homo_dict.items():
    if key in del_tandem:
        continue
    key_index=total_genome.index(key)
    key_list=total_genome[key_index-50:key_index]+total_genome[key_index+1:key_index+51]
    key_best_list=[]
    for gene in key_list:
        if gene in best_hit_dict.keys():
            key_best_list.append(best_hit_dict[gene])
    for i in value:
        try:
            i_index=total_genome.index(i)
        except ValueError:
            continue
        ###过滤tandem
        if abs(total_genome.index(i)-total_genome.index(key))<100:
            continue
        elif i in del_tandem:
            continue
        i_list=[]
        i_list=total_genome[i_index-50:i_index]+total_genome[i_index+1:i_index+51]
        
        num=len(list(set(key_best_list).intersection(i_list)))
        if num>=flanking_num:
            if key in out_dict.keys():
                out_dict[key].append([i,num])
            else:
                out_dict[key]=[[i,num]]
            # file3.write(key+'\t'+i+'\t'+str(num)+'\n')
            index+=1
index1=0
# for key,value in out_dict.items():
#     big_list=[]
#     big_num=0
#     if len(value)==1:
#         file3.write(key+'\t'+value[0][0]+'\t'+str(value[0][1])+'\n')
#         index1+=1
#     else:
#         for i in value:
#             if i[1]>big_num:
#                 big_list=i
#                 big_num=i[1]
#         file3.write(key+'\t'+big_list[0]+'\t'+str(big_list[1])+'\n')
#         index1+=1
out_list=[]
for  key,value in out_dict.items():
    for i in value:
        if [key,i[0]] not in out_list and [i[0],key] not in out_list:
            file3.write(key+'\t'+i[0]+'\n')
            out_list.append([key,i[0]])
print(index)
print(index1)

