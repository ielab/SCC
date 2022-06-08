import collections
import json
from collections import OrderedDict

msg_from_run = []
q_conv_dict = collections.defaultdict(list)

with open("run file containing messages retrieved from msg based index", "r") as f_run:
    for line in f_run.readlines():
        parts = line.split(" ")
        msg_from_run.append((parts[0],parts[2].strip()))


def mapping_q_msg_to_conv(M, json_mapping:str): # M is ranked msgs read from run file
    f_name = json_mapping
    with open(f_name, 'r', encoding='utf-8') as f:
        c = json.load(f, strict=False)
    for q,m in M:
        for conv in c:
            if m in c[conv] and conv not in q_conv_dict[q]:
                if q in q_conv_dict :
                    q_conv_dict[q].append(conv)
                else:
                    q_conv_dict[q] = [conv]

def calculate_MMR(q_C:dict):
    thisq = 0
    rank = 1
    for q,C in q_C.items():
        if thisq != q:
            thisq = q
            rank = 1
        for c in C:
            with open('another run file containing ', 'a') as out_f:
                out_f.write(q+' '+'Q0'+' '+str(c)+' '+str(rank)+' '+str(1/rank)+' '+'conv_run'+'\n')
                rank+=1

mapping_q_msg_to_conv(msg_from_run, 'conv_msgIDs_mapping_v2.json')
calculate_MMR(q_conv_dict)
