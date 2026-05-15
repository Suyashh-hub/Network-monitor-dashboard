import os
import paramiko

def ping_host(ip):
    response = os.system(f"ping -c 1 {ip} > /dev/null 2>&1")
    return "UP" if response == 0 else "DOWN"


def get_server_stats(ip, username, password):
    try:
        ssh = paramiko.SSHClient()

        ssh.set_missing_host_key_policy(
            paramiko.AutoAddPolicy()
        )

        ssh.connect(
            hostname=ip,
            username=username,
            password=password,
            timeout=5
        )

        commands = {
            "cpu": "top -bn1 | grep 'Cpu' | awk '{print $2 + $4 \"%\"}'",
            "ram": "free -m | awk 'NR==2{printf \"%.2f%%\", $3*100/$2}'",
            "disk": "df -h / | awk 'NR==2 {print $5}'"
        }

        stats = {}

        for key, command in commands.items():
            stdin, stdout, stderr = ssh.exec_command(command)

            stats[key] = stdout.read().decode().strip()

        ssh.close()

        return stats

    except Exception as e:
        return {
            "error": str(e)
        }
