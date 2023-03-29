ip_address = input("Enter an IP address: ")

octets = ip_address.split(".")


binary_octets = []
for octet in octets:
    binary_octet = bin(int(octet))[2:].zfill(8)
    binary_octets.append(binary_octet)



subnet_mask = "255.255.255.0"
prefix = sum([bin(int(i)).count("1") for i in subnet_mask.split(".")])

#reversed_subnet_mask = subnet_mask[::-1]
#binary_ver_list = []
#for n in reversed_subnet_mask.split("."):
    #binary_ver = bin(int(n))[2:].zfill(8)
    #binary_ver_list.append(binary_ver)
#count=0
#for j in binary_ver_list:
    #while j!=1:
        #count=count+1
    #if j==1:
        #break

print("IP Address:", ip_address)
print("Binary Octets:", binary_octets)
print("Subnet Mask:", subnet_mask)
print("Prefix:", prefix)
#print("Host Number: ", count)
