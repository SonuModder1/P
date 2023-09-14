import socket
import http.client
import time
import sys

def resolve_url_to_ip(url):
    try:
        ip = socket.gethostbyname(url)
        return ip
    except socket.gaierror:
        print("URL resolve karne mein samasya aayi.")
        return None

def http_ping(target_ip_or_url, target_port, interval=0.5):
    while True:
        try:
            if ":" in target_ip_or_url:
                target_ip, target_port = target_ip_or_url.split(":")
                target_port = int(target_port)
            else:
                target_ip = resolve_url_to_ip(target_ip_or_url)

            if target_ip:
                start_time = time.time()
                conn = http.client.HTTPConnection(target_ip, target_port, timeout=5)
                conn.request("HEAD", "/")
                response = conn.getresponse()
                end_time = time.time()
                response_time = (end_time - start_time) * 1000
                print(f"\033[97mConnected to \033[92m{target_ip_or_url}\033[97m: \033[97mtime=\033[92m{response_time:.2f}ms \033[97mprotocol=\033[92mHTTP \033[97mport=\033[92m{target_port}")
                conn.close()
            else:
                print("Invalid IP or URL")
        except Exception as e:
            print("\033[91mConnection timed out")

        time.sleep(interval)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 http_paping.py ip_or_url port")
        sys.exit(1)

    target_ip_or_url = sys.argv[1]
    target_port = int(sys.argv[2])
    interval = 0.4
    http_ping(target_ip_or_url, target_port, interval)
