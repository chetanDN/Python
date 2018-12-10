misra_dic={}
name="Adc"
violation_list = [1,2,3]
misra_dic[name]=[]
for sub_ele in violation_list:
    if sub_ele in misra_dic[name]:
        continue
    else:
        misra_dic[name].append(sub_ele)

print(misra_dic)
