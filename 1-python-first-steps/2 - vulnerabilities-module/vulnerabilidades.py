import socket
from tqdm import tqdm

def sys_init():
    print("Welcome to the vulnerability scanner!\n")
    print("Choose the vulnerability you want to scan:\n")
    print("============================================\n")
    print("1 - Open ports detector\n")
    print("2 - Operational System Checker\n")
    print("============================================\n")
    
    def switch_case(value):
        switch = {
            '1': open_ports_detector,
            '2': operational_system_checker
        }
    
        return switch.get(value, "Please, select a valid number...")
    
    user_choice = input("Desired vulnerability scanner: ")
    function_to_run = switch_case(user_choice)
    function_to_run()

def open_ports_detector():
    print("You chose the Open ports detector!\n")
    def scan_port(ip, port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((ip, port))
            sock.close()
            return result == 0
        except Exception as e:
            print(f"Error: {e}")
            return False

    target_ip = "192.168.0.4"
    print(f"Scanning IP: {target_ip}")

    ports_to_scan = range(1, 1024)
    results = list(map(lambda port: (port, scan_port(target_ip, port)), tqdm(ports_to_scan, desc="Scanning ports...")))

    open_ports = list(filter(lambda x: x[1], results))

    with open('results_scan.txt', 'w') as file:
        for port, status in open_ports:
            file.write(f"Port {port} is open!\n")

    print("Port scan finished!")

def operational_system_checker():
    print("You chose the Operational System Checker!\n")
    print("This feature is under construction... Stay tuned!")

sys_init()