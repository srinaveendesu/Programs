#from scapy.all import * # Packet manipulation
import pandas as pd # Pandas - Create and Manipulate DataFrames
import numpy as np # Math Stuff (don't worry only used for one line :] )
import binascii # Binary to Ascii 
import seaborn as sns
sns.set(color_codes=True)
#%matplotlib inline
#num_of_packets_to_sniff = 100
"""pcap = sniff(count=num_of_packets_to_sniff)

# sniff() returns packet list
## packetlist object can be enumerated 
print(type(pcap))
print(len(pcap))
print(pcap)
pcap[0]"""

df = pd.read_csv("out4.csv")
print(df['SRC-IP'].describe(),'\n\n')
print("Top Destination Address")
print(df['DST-IP'].describe(),'\n\n')
frequent_address = df['SRC-IP'].describe()['top']
print("who is top address speaking to?")
print(df[df['SRC-IP'] == frequent_address]['DST-IP'].unique(),"\n\n")

# Who is the top address speaking to (dst ports)
print("# Who is the top address speaking to (Destination Ports)")
print(df[df['SRC-IP'] == frequent_address]['DPORT'].unique(),"\n\n")

# Who is the top address speaking to (src ports)
print("# Who is the top address speaking to (Source Ports)")
print(df[df['SRC-IP'] == frequent_address]['SPORT'].unique(),"\n\n")

source_addresses = df.groupby("SRC-IP")['PAYLOAD'].sum()
#source_addresses.plot(kind='hist',title="Addresses Sending Payloads",figsize=(18,15))
source_addresses.plot(kind='bar',title="Addresses Sending Payloads",figsize=(50,25),logy=True)

# Group by Destination Address and Payload Sum
destination_addresses = df.groupby("DST-IP")['PAYLOAD'].sum()
destination_addresses.plot(kind='bar', title="Destination Addresses (Bytes Received)",figsize=(40,25),logy=True)

# Group by Source Port and Payload Sum
source_payloads = df.groupby("SPORT")['PAYLOAD'].sum()
source_payloads.plot(kind='bar',title="Source Ports (Bytes Sent)",figsize=(40,25),logy=True)

# Group by Destination Port and Payload Sum
destination_payloads = df.groupby("DPORT")['PAYLOAD'].sum()
destination_payloads.plot(kind='bar',title="Destination Ports (Bytes Received)",figsize=(40,25),logy=True)

#df.groupby("TIME")['PAYLOAD'].sum().plot(kind='barh',title="Destination Ports (Bytes Received)",figsize=(40,25),logy=True)


frequent_address_df = df[df['SRC-IP'] == frequent_address]
frequent_address_df.describe()
x = frequent_address_df['PAYLOAD'].tolist()
sns.barplot(x="TIME", y="PAYLOAD", data=frequent_address_df[['PAYLOAD','TIME']],
            label="Total", color="b").set_title("History of bytes sent by most frequent address")


