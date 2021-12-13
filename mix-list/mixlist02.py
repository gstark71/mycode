# display only the IP addresses to the screen.
iplist = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]

# test 1 - add up the strings
print("IP addresses: " + iplist[3] + ", and " + iplist[4])

# test 2 - using the comma separator
print("IP addreses:", iplist[3], ", and", iplist[4])

# test 3 - using an 'f-string'
print(f"IP addresses: {iplist[3]}, and {iplist[4]}")

