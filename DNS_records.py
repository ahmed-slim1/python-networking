import dns.resolver

target = input("target name :  ")
type = input("type of DNS :  ") #type{A,AAAA,PTR,CNAME,MX,SRV,SDA,SN}
result = dns.resolver.query(target,type,raise_on_no_answer =False)
for value in result:
    print("Host >>> ",value.to_text())