import concurrent.futures
import requests
import time
import subprocess

def get_minikube_ip():
    try:
        result = subprocess.run(['minikube', 'ip'], capture_output=True, text=True)
        return result.stdout.strip()
    except Exception as e:
        print(f"Error getting minikube IP: {e}")
        return None

def send_request(url):
    try:
        response = requests.get(url, timeout=5)
        print(f"Request status: {response.status_code}")
    except Exception as e:
        print(f"Request error: {e}")

def run_load_test(url, concurrency=10, duration=60):
    start_time = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=concurrency) as executor:
        while time.time() - start_time < duration:
            futures = [executor.submit(send_request, url) for _ in range(concurrency)]
            concurrent.futures.wait(futures, timeout=5)
            time.sleep(0.1)

if __name__ == "__main__":
    minikube_ip = get_minikube_ip()
    if minikube_ip:
        service_url = f"http://{minikube_ip}/cpu-intensive"
        run_load_test(service_url)
    else:
        print("Failed to get minikube IP")