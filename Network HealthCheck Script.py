

from netmiko import ConnectHandler

cisco_881 = {
    'device_type': 'cisco_ios',
    'host':   'mad6-co-acc-v1.amazon.com',
    'username': 'NotRealID',
    'password': 'NotMyPassword',
    'secret': 'NotMyPassword'
}

net_connect = ConnectHandler(**cisco_881)
net_connect.enable()

output = net_connect.send_command('show clock')
print(output)

output = net_connect.send_command('show bgp sum')
print(output)

output = net_connect.send_command('show int des')
print(output)

Tunnel_Interface = input("Enter Tunnel Interface: ")
output = net_connect.send_command(f"show int {Tunnel_Interface} | i des")
print(output)

Destination_IP = input("Enter Destination IP: ")
Source_IP = input("Enter Source IP: ")

output = net_connect.send_command(f"ping {Destination_IP} so {Source_IP} re 500 si 1400")
print(output)

output = net_connect.send_command(f"traceroute {Destination_IP} time 1")
print(output)

input("Press 'Enter' to exit")

