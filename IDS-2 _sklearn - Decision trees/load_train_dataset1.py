import numpy as np
import pandas as pd


columns=["value","protocol","service","flag","duration","protocol_type","src_bytes","dst_bytes","land","wrong_fragment","urgent","hot","num_failed_logins","logged_in","num_compromised","root_shell","su_attempted","num_root","num_file_creations","num_shells","num_access_files","num_outbound_cmds","is_host_login","is_guest_login","count","srv_count","serror_rate","srv_serror_rate","rerror_rate","srv_rerror_rate","same_srv_rate","diff_srv_rate","srv_diff_host_rate","dst_host_count","dst_host_srv_count","dst_host_same_srv_rate","dst_host_diff_srv_rate","dst_host_same_src_port_rate","dst_host_srv_diff_host_rate","dst_host_serror_rate","st_host_srv_serror_rate","dst_host_rerror_rate","dst_host_srv_rerror_rate"]

raw_data=pd.read_csv(r'D:\python_projects\IDS-2 _sklearn\NSL_KDD\train.csv',names=columns)

header=np.array(raw_data["dst_host_rerror_rate"])

columns1=["value","protocol","service","flag","duration","protocol_type","src_bytes","dst_bytes","land","wrong_fragment","urgent","hot","num_failed_logins","logged_in","num_compromised","root_shell","su_attempted","num_root","num_file_creations","num_shells","num_access_files","num_outbound_cmds","is_host_login","is_guest_login","count","srv_count","serror_rate","srv_serror_rate","rerror_rate","srv_rerror_rate","same_srv_rate","diff_srv_rate","srv_diff_host_rate","dst_host_count","dst_host_srv_count","dst_host_same_srv_rate","dst_host_diff_srv_rate","dst_host_same_src_port_rate","dst_host_srv_diff_host_rate","dst_host_serror_rate","st_host_srv_serror_rate","dst_host_srv_rerror_rate"]

X=raw_data[columns1]

# List of protocols used 
#Protocols=["tcp","udp","icmp"]

raw_protocol=raw_data["protocol"]

raw_flag=raw_data["flag"]

raw_services=raw_data["service"]

protocol=[]


for i in range(len(raw_protocol)):
    if raw_protocol.iloc[i]=="tcp":
        protocol.append(1)
    if raw_protocol.iloc[i]=="udp":
        protocol.append(2)
    if raw_protocol.iloc[i]=="icmp":
        protocol.append(3)


X["protocol"]=protocol
X["protocol"]=X["protocol"].astype(int)


# List of Flags used  
#Flag=["OTH","REJ","RSTO","RSTOS0","RSTR","S0","S1","S2","S3","SF ","SH "]


flag=[]

for i in range(len(raw_protocol)):
    if raw_flag.iloc[i]=="OTH":
        flag.append(1)
    if raw_flag.iloc[i]=="REJ":
        flag.append(2)
    if raw_flag.iloc[i]=="RSTO":
        flag.append(3)
    if raw_flag.iloc[i]=="RSTOS0":
        flag.append(4)
    if raw_flag.iloc[i]=="RSTR":
        flag.append(5)
    if raw_flag.iloc[i]=="S0":
        flag.append(6)
    if raw_flag.iloc[i]=="S1":
        flag.append(7)
    if raw_flag.iloc[i]=="S2":
        flag.append(8)
    if raw_flag.iloc[i]=="S3":
        flag.append(9)
    if raw_flag.iloc[i]=="SF":
        flag.append(10)
    if raw_flag.iloc[i]=="SH":
        flag.append(11)


X["flag"]=flag
X["flag"]=X["flag"].astype(int)


# List of Services used  
#Services=["IRC","X11","Z39_50","aol","auth","bgp","courier","csnet_ns","ctf","daytime","discard","domain","domain_u","echo ","eco_i ","ecr_i ","efs ","finger","ftp","ftp_data","gopher","harvest","hostnames","http","http_2784","http_443","http_8001","imap4","iso_tsap","klogin","kshell","ldap","link","login","mtp","name","netbios_dgm","netbios_ns","netbios_ssn","netstat","nnsp","nntp","ntp_u","other","pm_dump","pop_2"
#"pop_3","printer","private","red_i","remote_job","rje","shell","smtp","sql_net","ssh","sunrpc","supdup","systat","telnet","tftp_u","tim_i","time","urh_i","urp_i","uucp","uucp_path","exec","vmnet","whois"]

services=[]

for i in range(len(raw_services)):
    if raw_services.iloc[i]=="IRC":
        services.append(1)
    elif raw_services.iloc[i]=="X11":
        services.append(2)
    elif raw_services.iloc[i]=="Z39_50":
        services.append(3)
    elif raw_services.iloc[i]=="aol":
        services.append(4)
    elif raw_services.iloc[i]=="auth":
        services.append(5)
    elif raw_services.iloc[i]=="bgp":
        services.append(6)
    elif raw_services.iloc[i]=="courier":
        services.append(7)
    elif raw_services.iloc[i]=="csnet_ns":
        services.append(8)
    elif raw_services.iloc[i]=="ctf":
        services.append(9)
    elif raw_services.iloc[i]=="daytime":
        services.append(10)
    elif raw_services.iloc[i]=="discard":
        services.append(11)
    elif raw_services.iloc[i]=="domain":
        services.append(12)
    elif raw_services.iloc[i]=="domain_u":
        services.append(13)
    elif raw_services.iloc[i]=="echo ":
        services.append(14)
    elif raw_services.iloc[i]=="eco_i ":
        services.append(15)
    elif raw_services.iloc[i]=="ecr_i ":
        services.append(16)
    elif raw_services.iloc[i]=="efs ":
        services.append(17)
    elif raw_services.iloc[i]=="finger":
        services.append(18)
    elif raw_services.iloc[i]=="ftp":
        services.append(19)
    elif raw_services.iloc[i]=="ftp_data":
        services.append(20)
    elif raw_services.iloc[i]=="gopher":
        services.append(21)
    elif raw_services.iloc[i]=="harvest":
        services.append(22)
    elif raw_services.iloc[i]=="hostnames":
        services.append(23)
    elif raw_services.iloc[i]=="http":
        services.append(24)
    elif raw_services.iloc[i]=="http_2784":
        services.append(25)
    elif raw_services.iloc[i]=="http_443":
        services.append(26)
    elif raw_services.iloc[i]=="http_8001":
        services.append(27)
    elif raw_services.iloc[i]=="imap4":
        services.append(28)
    elif raw_services.iloc[i]=="iso_tsap":
        services.append(29)
    elif raw_services.iloc[i]=="klogin":
        services.append(30)
    elif raw_services.iloc[i]=="kshell":
        services.append(31)
    elif raw_services.iloc[i]=="ldap":
        services.append(32)
    elif raw_services.iloc[i]=="link":
        services.append(33)
    elif raw_services.iloc[i]=="login":
        services.append(34)
    elif raw_services.iloc[i]=="mtp":
        services.append(35)
    elif raw_services.iloc[i]=="name":
        services.append(36)
    elif raw_services.iloc[i]=="netbios_dgm":
        services.append(37)
    elif raw_services.iloc[i]=="netbios_ns":
        services.append(38)
    elif raw_services.iloc[i]=="netbios_ssn":
        services.append(39)
    elif raw_services.iloc[i]=="netstat":
        services.append(40)
    elif raw_services.iloc[i]=="nnsp":
        services.append(41)
    elif raw_services.iloc[i]=="nntp":
        services.append(42)
    elif raw_services.iloc[i]=="ntp_u":
        services.append(43)
    elif raw_services.iloc[i]=="other":
        services.append(44)
    elif raw_services.iloc[i]=="pm_dump":
        services.append(45)
    elif raw_services.iloc[i]=="pop_2":
        services.append(46)
    elif raw_services.iloc[i]=="pop_3":
        services.append(47)
    elif raw_services.iloc[i]=="printer":
        services.append(48)
    elif raw_services.iloc[i]=="private":
        services.append(49)
    elif raw_services.iloc[i]=="red_i":
        services.append(50)
    elif raw_services.iloc[i]=="remote_job":
        services.append(51)
    elif raw_services.iloc[i]=="rje":
        services.append(52)
    elif raw_services.iloc[i]=="shell":
        services.append(53)
    elif raw_services.iloc[i]=="smtp":
        services.append(54)
    elif raw_services.iloc[i]=="sql_net":
        services.append(55)
    elif raw_services.iloc[i]=="ssh":
        services.append(56)
    elif raw_services.iloc[i]=="sunrpc":
        services.append(57)
    elif raw_services.iloc[i]=="supdup":
        services.append(58)
    elif raw_services.iloc[i]=="systat":
        services.append(59)
    elif raw_services.iloc[i]=="telnet":
        services.append(60)
    elif raw_services.iloc[i]=="tftp_u":
        services.append(61)
    elif raw_services.iloc[i]=="tim_i":
        services.append(62)
    elif raw_services.iloc[i]=="time":
        services.append(63)
    elif raw_services.iloc[i]=="urh_i":
        services.append(64)
    elif raw_services.iloc[i]=="urp_i":
        services.append(65)
    elif raw_services.iloc[i]=="uucp":
        services.append(66)
    elif raw_services.iloc[i]=="uucp_path":
        services.append(67)
    elif raw_services.iloc[i]=="exec":
        services.append(68)
    elif raw_services.iloc[i]=="vmnet":
        services.append(69)
    elif raw_services.iloc[i]=="whois":
        services.append(70)
    else:
        services.append(71)
 
        
X["service"]=services
X["service"]=X["service"].astype(int)

Y=raw_data["dst_host_rerror_rate"]

X=np.array(X)
Y=np.array(Y)
#Protocols=["tcp","udp","icmp"]


