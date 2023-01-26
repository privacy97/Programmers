def solution(id_list, report, k):
    
    dic_id_list = {a : [] for a in id_list}
    dic_report_count = {a : 0 for a in id_list}
    dic_email_list = {a : 0 for a in id_list}
    
    for i in report:
        user, report = i.split()
        if report not in dic_id_list[user]:
            dic_id_list[user].append(report)
            dic_report_count[report] += 1
    
    #print(dic_report_count)
    #print(dic_id_list)
    
    for r_user, r_count in dic_report_count.items():
        if r_count >= k:
            #print(r_user)
            for i_user, i_list in dic_id_list.items():
                if r_user in i_list:
                    dic_email_list[i_user] += 1
        
    return list(dic_email_list.values())