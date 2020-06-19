

from netmiko import ConnectHandler

cisco_881 = {
    'device_type': 'cisco_ios',
    'host': 'hostname.com',
    'username': 'notRealUser',
    'password': 'notRealPass',
    'secret': 'notRealPass'
}

commands = ['show clock', 'sh ver | section uptime', 'show bgp sum', 'show int des']
output = ''

net_connect = ConnectHandler(**cisco_881)
net_connect.enable()

for command in commands:
    output += net_connect.send_command(command) + '\n'

search_tunnel = net_connect.send_command('sh int desc | I Prod')
interface = search_tunnel.split()
destination = net_connect.send_command(f"show int {interface[0]} | i des")
output += destination

get_ips = destination.split()
source_ip = get_ips[2]
destination_ip = get_ips[5]

output += net_connect.send_command(f"ping {destination_ip} so {source_ip} re 500 si 1400")
output += net_connect.send_command(f"traceroute {destination_ip} time 1")

with open('C:/User/Desktop/logs.txt', 'a+') as file:
    file.write(output)
    file.close()

print(output)

print("Done! Closing Connection")
input("Press 'Enter' to exit")