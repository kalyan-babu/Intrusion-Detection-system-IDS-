import numpy as np
import pandas as pd

columns=["duration","protocol_type","service","flag","src_bytes","dst_bytes","land","wrong_fragment","urgent","hot","num_failed_logins","logged_in","num_compromised","root_shell","su_attempted","num_root","num_file_creations","num_shells","num_access_files","num_outbound_cmds","is_host_login","is_guest_login","count","srv_count","serror_rate","srv_serror_rate","rerror_rate","srv_rerror_rate","same_srv_rate","diff_srv_rate","srv_diff_host_rate","dst_host_count","dst_host_srv_count","dst_host_same_srv_rate","dst_host_diff_srv_rate","dst_host_same_src_port_rate","dst_host_srv_diff_host_rate","dst_host_serror_rate","st_host_srv_serror_rate","dst_host_rerror_rate","dst_host_srv_rerror_rate"]

raw_data=pd.read_csv(r'D:\python_projects\IDS-2\NSL_KDD\test.csv',names=columns)

header=np.array(raw_data["dst_host_rerror_rate"])


columns1=["service","flag","src_bytes","dst_bytes","land","wrong_fragment","urgent","hot","num_failed_logins","logged_in","num_compromised","root_shell","su_attempted","num_root","num_file_creations","num_shells","num_access_files","num_outbound_cmds","is_host_login","is_guest_login","count","srv_count","serror_rate","srv_serror_rate","rerror_rate","srv_rerror_rate","same_srv_rate","diff_srv_rate","srv_diff_host_rate","dst_host_count","dst_host_srv_count","dst_host_same_srv_rate","dst_host_diff_srv_rate","dst_host_same_src_port_rate","dst_host_srv_diff_host_rate","dst_host_serror_rate","st_host_srv_serror_rate","dst_host_srv_rerror_rate"]

dataset=np.array(raw_data[columns1])

dos=["back","land","neptune","pod","smurf","teardrop","snmpgetattack"]   #type 1 attack
r2l=["ftp_write","guess_passwd","imap","multihop","phf","spy","warezclient","warezmaster"]   # type 2  
u2r=["buffer_overflow","loadmodule","perl","rootkit"]    #type 3 
probe=["nmap","satan","ipsweep","portsweep"]    # type 4
normal=["normal"]



# List of protocols used 
#Protocols=["tcp","udp","icmp"]

# List of Services used  
#Services=["IRC","X11","Z39_50","aol","auth","bgp","courier","csnet_ns","ctf","daytime","discard","domain","domain_u","echo ","eco_i ","ecr_i ","efs ","finger","ftp","ftp_data","gopher","harvest","hostnames","http","http_2784","http_443","http_8001","imap4","iso_tsap","klogin","kshell","ldap","link","login","mtp","name","netbios_dgm","netbios_ns","netbios_ssn","netstat","nnsp","nntp","ntp_u","other","pm_dump","pop_2"
#"pop_3","printer","private","red_i","remote_job","rje","shell","smtp","sql_net","ssh","sunrpc","supdup","systat","telnet","tftp_u","tim_i","time","urh_i","urp_i","uucp","uucp_path","exec","vmnet","whois"]

# List of Flags used  
#Flag=["OTH","REJ","RSTO","RSTOS0","RSTR","S0","S1","S2","S3","SF ","SH "]




count_normal=0
count_dos=0
count_r2l=0
count_u2r=0
count_probe=0



for i in range(len(header)):
    response=header[i]
    if response in dos:
        count_dos+=1
    if response in r2l:
        count_r2l+=1
    if response in u2r:
        count_u2r+=1
    if response in probe:
        count_probe+=1
    if response in normal:
        count_normal+=1

print("\nTotalTestSet_attackas="+repr(header.shape[0]))
print("TotalTestSet_dos_attackas="+repr(count_dos))
print("TotalTestSet_r2l_attackas="+repr(count_r2l))
print("TotalTestSet_u2r_attackas="+repr(count_u2r))
print("TotalTestSet_probe_attackas="+repr(count_probe))
print("TotalTestSet_normal_attackas="+repr(count_normal))